# app.py
# ------------------------------------------------------------
# Interactive AI Quiz Game - DSC401-6 Artificial Intelligence (Units I & II)
#
# Run it with:   streamlit run app.py
#
# How Streamlit works (in one paragraph):
# Streamlit runs this whole file from top to bottom every time the user
# clicks a button or changes an input. Normal variables are therefore reset
# on every click. Anything we need to REMEMBER between clicks (the current
# question, the score, the answers given) is stored in st.session_state,
# which works like a dictionary that survives each re-run.
# ------------------------------------------------------------

import csv
import os
import random
import time
from datetime import datetime

import streamlit as st

from questions import QUESTIONS

st.set_page_config(page_title="AI Quiz Game", page_icon="🤖", layout="centered")

# The leaderboard is saved in a small CSV file next to this script.
LEADERBOARD_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leaderboard.csv")

# Questions of these types have options that we shuffle.
# True/False and Assertion-Reason options are NOT shuffled, because their
# order (True, False / A, B, C, D) is part of the format.
SHUFFLE_TYPES = ["MCQ", "Scenario", "Problem-Solving"]


# ============================================================
# 1. Small helper functions
# ============================================================

def normalise(text):
    """Make typed answers easy to compare: lower case, letters and digits only.
    Example: ' A, B -> C ' becomes 'abc' and 'Breadth-First' becomes 'breadthfirst'."""
    text = str(text).lower()
    cleaned = ""
    for ch in text:
        if ch.isalnum():
            cleaned = cleaned + ch
    return cleaned


def prepare_question(question):
    """Make a copy of a question for this quiz round and shuffle its choices.
    We shuffle a COPY, so the original question bank never changes.
    The correct answer is stored as text (not as a position), so shuffling
    the options can never change which answer is correct."""
    q = dict(question)
    if q["type"] == "Match the Following":
        right_side = list(q["answer"].values())
        random.shuffle(right_side)
        q["choices"] = right_side
    elif q["type"] in SHUFFLE_TYPES and "options" in q:
        options = list(q["options"])
        random.shuffle(options)
        q["options"] = options
    return q


def check_answer(q, response):
    """Return True if the student's response is correct."""
    if q["type"] == "Match the Following":
        # Every pair must match the answer key exactly.
        return response == q["answer"]
    if "options" in q:
        # Choice question: compare the chosen option text with the answer text.
        return response == q["answer"]
    # Typed question: compare with every accepted answer after cleaning.
    for accepted in q["answer"]:
        if normalise(response) == normalise(accepted):
            return True
    return False


def is_answered(q, response):
    """Return True if the student has actually given an answer."""
    if q["type"] == "Match the Following":
        for value in response.values():
            if value is None:
                return False
        return True
    if response is None:
        return False
    return str(response).strip() != ""


def answer_to_text(q, value):
    """Turn an answer (or a response) into readable text for feedback and review."""
    if value is None:
        return "(no answer)"
    if q["type"] == "Match the Following":
        lines = []
        for left, right in value.items():
            lines.append(f"- **{left}** → {right}")
        return "\n".join(lines)
    if isinstance(value, list):          # accepted answers for typed questions
        return value[0]
    return str(value)


def format_time(seconds):
    seconds = int(seconds)
    return f"{seconds // 60}m {seconds % 60}s"


# ============================================================
# 2. Leaderboard (a simple CSV file)
# ============================================================

def save_to_leaderboard(name, score, total, percent, seconds):
    file_exists = os.path.exists(LEADERBOARD_FILE)
    with open(LEADERBOARD_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Score", "Out of", "Percent", "Time (s)", "Date"])
        writer.writerow([name, score, total, percent, int(seconds),
                         datetime.now().strftime("%d-%m-%Y %H:%M")])


def show_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        st.write("No scores yet. Be the first!")
        return
    with open(LEADERBOARD_FILE, newline="") as f:
        rows = list(csv.DictReader(f))
    # Highest percentage first; if two players tie, the faster one comes first.
    rows.sort(key=lambda row: (-float(row["Percent"]), int(row["Time (s)"])))
    st.table(rows[:10])


# ============================================================
# 3. Session state: starting, moving through and restarting the quiz
# ============================================================

def start_quiz(name, how_many, difficulty):
    # Pick the questions that match the chosen difficulty.
    pool = []
    for q in QUESTIONS:
        if difficulty == "Mixed" or q["difficulty"] == difficulty:
            pool.append(q)
    random.shuffle(pool)                          # random question order
    if how_many != "All":
        pool = pool[:how_many]

    st.session_state.player = name.strip() or "Player"
    st.session_state.quiz = [prepare_question(q) for q in pool]
    st.session_state.index = 0                    # which question we are on
    st.session_state.score = 0.0
    st.session_state.records = []                 # one record per answered question
    st.session_state.submitted = False            # has the current question been answered?
    st.session_state.hint_used = False            # was the hint shown for this question?
    st.session_state.start_time = time.time()
    st.session_state.saved = False                # has this result been saved to the leaderboard?
    st.session_state.page = "quiz"


def submit_answer(q, response, skipped=False):
    # Guard: never score the same question twice.
    if st.session_state.submitted:
        return
    correct = (not skipped) and check_answer(q, response)
    points = 0.0
    if correct:
        points = 0.5 if st.session_state.hint_used else 1.0
    st.session_state.score += points
    st.session_state.records.append({
        "q": q,
        "response": None if skipped else response,
        "correct": correct,
        "skipped": skipped,
        "hint_used": st.session_state.hint_used,
        "points": points,
    })
    st.session_state.submitted = True


def next_question():
    st.session_state.index += 1
    st.session_state.submitted = False
    st.session_state.hint_used = False
    if st.session_state.index >= len(st.session_state.quiz):
        st.session_state.end_time = time.time()
        st.session_state.page = "result"


def restart():
    # Clearing session state sends the app back to the welcome screen.
    for key in list(st.session_state.keys()):
        del st.session_state[key]


def show_sidebar():
    """A small 'player profile' panel on the left, shown during and after the quiz."""
    records = st.session_state.records
    with st.sidebar:
        st.header("🏆 Player Profile")
        st.write(f"**Player:** {st.session_state.player}")
        st.metric("Score", f"{st.session_state.score:g}")
        st.progress(len(records) / len(st.session_state.quiz))
        st.caption(f"Answered {len(records)} of {len(st.session_state.quiz)}")
        correct = sum(1 for r in records if r["correct"])
        hints = sum(1 for r in records if r["hint_used"])
        st.write(f"✅ Correct: {correct}")
        st.write(f"💡 Hints used: {hints}")
        st.divider()
        st.info("Think before you click. Read the explanation after every question, "
                "even when you get it right.")


def get_badges(records, percent):
    """Simple achievement badges shown on the results screen."""
    badges = []
    if percent >= 80:
        badges.append("🏆 AI Expert: scored 80% or more")
    if all(not r["hint_used"] for r in records):
        badges.append("🧠 Independent Thinker: no hints used")
    if all(not r["skipped"] for r in records):
        badges.append("💪 Never Gave Up: no questions skipped")
    search_records = [r for r in records if "search" in r["q"]["tags"]]
    if search_records and all(r["correct"] for r in search_records):
        badges.append("🔍 Search Master: every search question right")
    return badges


# First run: show the welcome screen.
if "page" not in st.session_state:
    st.session_state.page = "welcome"


# ============================================================
# 4. Screen 1 - Welcome
# ============================================================

def welcome_page():
    st.title("🤖 AI Quiz Game")
    st.subheader("DSC401-6 Artificial Intelligence · Units I & II")

    topics = sorted(set(q["topic"] for q in QUESTIONS))
    types = sorted(set(q["type"] for q in QUESTIONS))
    c1, c2, c3 = st.columns(3)
    c1.metric("Questions in bank", len(QUESTIONS))
    c2.metric("Topics", len(topics))
    c3.metric("Question formats", len(types))

    st.markdown(
        """
**How to play**
1. Enter your name and choose how many questions you want and the difficulty.
2. Questions appear one at a time in a random order.
3. Choose or type your answer and press **Submit answer**. You will see straight away
   whether you are right, the correct answer and a short explanation.
4. Stuck? Press **Show hint**. A correct answer after a hint earns **½ point** instead of 1.
5. You can **Skip** a question (0 points). At the end you get your score, a full review
   and a place on the leaderboard.
"""
    )

    name = st.text_input("Your name", placeholder="e.g. Rahul")
    col1, col2 = st.columns(2)
    how_many = col1.selectbox("Number of questions", [10, 20, 30, "All"])
    difficulty = col2.selectbox("Difficulty", ["Mixed", "Easy", "Medium", "Hard"])

    if st.button("▶ Start quiz", type="primary"):
        start_quiz(name, how_many, difficulty)
        st.rerun()

    with st.expander("🏆 Leaderboard"):
        show_leaderboard()
    with st.expander("📚 Topics covered"):
        for t in topics:
            st.write("•", t)


# ============================================================
# 5. Screen 2 - The quiz (one question at a time)
# ============================================================

def show_answer_input(q, disabled):
    """Draw the right input widget for the question format and return the response.
    Each widget gets a key based on the question id, so Streamlit remembers
    the student's choice while the page re-runs."""
    key = "answer_" + q["id"]

    if q["type"] == "Match the Following":
        st.write("**Column A** → choose the matching item from **Column B**")
        response = {}
        for left in q["answer"]:
            response[left] = st.selectbox(
                left, q["choices"], index=None, placeholder="Choose a match...",
                key=key + "_" + left, disabled=disabled,
            )
        return response

    if "options" in q:   # MCQ, True/False, Assertion-Reason, Scenario, some Problem-Solving
        return st.radio("Choose your answer:", q["options"], index=None,
                        key=key, disabled=disabled)

    # Fill in the Blank and typed Problem-Solving questions
    return st.text_input("Type your answer:", key=key, disabled=disabled)


def show_feedback(record):
    q = record["q"]
    if record["skipped"]:
        st.warning("⏭ Skipped. 0 points.")
    elif record["correct"]:
        if record["hint_used"]:
            st.success("✅ Correct! +0.5 point (hint used)")
        else:
            st.success("✅ Correct! +1 point")
    else:
        st.error("❌ Not quite. 0 points.")

    # For matching questions, show which pairs were right.
    if q["type"] == "Match the Following" and not record["skipped"]:
        for left, right in q["answer"].items():
            mark = "✔" if record["response"].get(left) == right else "✘"
            st.write(f"{mark} **{left}** → {right}")
    else:
        st.markdown(f"**Correct answer:** {answer_to_text(q, q['answer'])}")
    st.info(f"**Explanation:** {q['explanation']}")


def quiz_page():
    quiz = st.session_state.quiz
    i = st.session_state.index
    q = quiz[i]

    # Progress indicator, score so far and time so far.
    st.progress(i / len(quiz))
    c1, c2, c3 = st.columns(3)
    c1.write(f"**Question {i + 1} of {len(quiz)}**")
    c2.write(f"**Score:** {st.session_state.score:g}")
    c3.write(f"⏱ {format_time(time.time() - st.session_state.start_time)}")

    st.caption(f"Unit {q['unit']} · {q['topic']} · {q['type']} · {q['difficulty']}")
    st.markdown(q["question"])

    response = show_answer_input(q, disabled=st.session_state.submitted)

    if st.session_state.hint_used:
        st.info(f"💡 **Hint:** {q['hint']}")

    if not st.session_state.submitted:
        b1, b2, b3 = st.columns(3)
        if b1.button("Submit answer", type="primary"):
            if is_answered(q, response):
                submit_answer(q, response)
                st.rerun()
            else:
                st.warning("Please give an answer first, or press Skip.")
        if b2.button("💡 Show hint", disabled=st.session_state.hint_used):
            st.session_state.hint_used = True
            st.rerun()
        if b3.button("⏭ Skip"):
            submit_answer(q, None, skipped=True)
            st.rerun()
    else:
        show_feedback(st.session_state.records[-1])
        last = (i == len(quiz) - 1)
        if st.button("See my results 🏁" if last else "Next question ➡", type="primary"):
            next_question()
            st.rerun()

    st.divider()
    if st.button("↺ Quit and restart"):
        restart()
        st.rerun()


# ============================================================
# 6. Screen 3 - Results, review and leaderboard
# ============================================================

def result_page():
    records = st.session_state.records
    total = len(records)
    score = st.session_state.score
    percent = round(score / total * 100, 1) if total else 0
    seconds = st.session_state.end_time - st.session_state.start_time

    correct = sum(1 for r in records if r["correct"])
    skipped = sum(1 for r in records if r["skipped"])
    wrong = total - correct - skipped
    hints = sum(1 for r in records if r["hint_used"])

    # Save the result once (re-runs of this page must not add it again).
    if not st.session_state.saved:
        save_to_leaderboard(st.session_state.player, score, total, percent, seconds)
        st.session_state.saved = True

    st.title("🏁 Quiz finished!")
    st.subheader(f"{st.session_state.player}, you scored {score:g} out of {total} ({percent}%)")

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Correct", correct)
    c2.metric("Wrong", wrong)
    c3.metric("Skipped", skipped)
    c4.metric("Hints used", hints)
    c5.metric("Time", format_time(seconds))

    if percent >= 80:
        st.success("Excellent! You have a strong grasp of Units I and II.")
    elif percent >= 50:
        st.info("Good effort. Revise the topics below and try again.")
    else:
        st.warning("Keep practising. Go through the explanations below carefully.")

    badges = get_badges(records, percent)
    if badges:
        st.markdown("**Badges earned:**")
        for badge in badges:
            st.write(badge)

    # Topics where the student lost marks.
    weak_topics = sorted(set(r["q"]["topic"] for r in records if not r["correct"]))
    if weak_topics:
        st.markdown("**Topics to revise:** " + ", ".join(weak_topics))

    st.header("📝 Review your answers")
    for number, r in enumerate(records, start=1):
        q = r["q"]
        if r["correct"]:
            icon = "✅"
        elif r["skipped"]:
            icon = "⏭"
        else:
            icon = "❌"
        with st.expander(f"{icon} {number}. {q['topic']} ({q['type']})"):
            st.markdown(q["question"])
            st.markdown("**Your answer:**")
            st.markdown(answer_to_text(q, r["response"]))
            st.markdown("**Correct answer:**")
            st.markdown(answer_to_text(q, q["answer"]))
            st.markdown(f"**Explanation:** {q['explanation']}")

    st.header("🏆 Leaderboard (top 10)")
    show_leaderboard()

    if st.button("↺ Play again", type="primary"):
        restart()
        st.rerun()


# ============================================================
# 7. Show the right screen
# ============================================================

if st.session_state.page == "welcome":
    welcome_page()
elif st.session_state.page == "quiz":
    show_sidebar()
    quiz_page()
else:
    show_sidebar()
    result_page()
