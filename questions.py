# questions.py
# ------------------------------------------------------------
# The complete question bank for the AI Quiz Game (Units I & II).
#
# Every question is a Python dictionary with these keys:
#   id          - unique question number, e.g. "Q01"
#   unit        - "I" or "II"
#   topic       - one of the 20 syllabus topics
#   type        - one of the 7 question formats
#   difficulty  - "Easy", "Medium" or "Hard"
#   question    - the text shown to the student
#   options     - list of choices (only for questions with choices)
#   answer      - the correct answer:
#                   * choice questions -> the exact text of the correct option
#                   * typed questions  -> a list of accepted answers
#                   * match questions  -> a dictionary {left item: right item}
#   explanation - why the answer is correct (shown after answering)
#   hint        - a small clue the student can ask for
#   tags        - "real-world" and/or "search" labels for the assignment rules
# ------------------------------------------------------------

# The four standard Assertion-Reason choices. Every Assertion-Reason
# question uses exactly these options, in this order.
AR_A = "A. Both Assertion and Reason are true, and Reason correctly explains Assertion."
AR_B = "B. Both Assertion and Reason are true, but Reason does not correctly explain Assertion."
AR_C = "C. Assertion is true, but Reason is false."
AR_D = "D. Assertion is false, but Reason is true."
AR_OPTIONS = [AR_A, AR_B, AR_C, AR_D]

TRUE_FALSE = ["True", "False"]

# A small search tree used by the BFS, DFS and IDS problems.
SEARCH_TREE = """
```
            A
          /   \\
         B     C
        / \\   / \\
       D   E F   G
           |     |
           H     I
```
Children are always visited **left to right**. A node is goal-tested when it is
taken out of the frontier (when it is visited).
"""

# A small weighted graph used by the Greedy Best-First and A* problems.
WEIGHTED_GRAPH = """
```
Edges (one way, with step cost):     Heuristic h(n):
  S -> A  cost 2                       h(S) = 6
  S -> B  cost 3                       h(A) = 2
  A -> G  cost 9                       h(B) = 4
  B -> C  cost 2                       h(C) = 2
  C -> G  cost 2                       h(G) = 0
```
Start = **S**, Goal = **G**. The goal test is done when a node is taken out
of the frontier.
"""


QUESTIONS = [
    # ==========================================================
    # UNIT I
    # ==========================================================

    # ---------- Topic 1: Foundations and Applications of AI ----------
    {
        "id": "Q01", "unit": "I", "topic": "Foundations and Applications of AI",
        "type": "MCQ", "difficulty": "Easy",
        "question": "Who coined the term 'Artificial Intelligence', and for which event?",
        "options": [
            "Alan Turing, for his 1950 paper on machine intelligence",
            "John McCarthy, for the 1956 Dartmouth workshop",
            "Marvin Minsky, for the first MIT robotics lab",
            "Herbert Simon, for the General Problem Solver project",
        ],
        "answer": "John McCarthy, for the 1956 Dartmouth workshop",
        "explanation": "John McCarthy proposed the name 'Artificial Intelligence' for the 1956 "
                       "Dartmouth summer workshop, which is usually treated as the birth of AI as a "
                       "field. Turing wrote about machine intelligence earlier (1950) but did not "
                       "coin the term.",
        "hint": "The event was a summer workshop at an American college in the mid-1950s.",
        "tags": [],
    },
    {
        "id": "Q02", "unit": "I", "topic": "Foundations and Applications of AI",
        "type": "Match the Following", "difficulty": "Medium",
        "question": "Match each approach to AI (Column A) with what it focuses on (Column B).",
        "answer": {
            "Thinking humanly": "Modelling how the human mind actually works (cognitive modelling)",
            "Thinking rationally": "Using logic and correct rules of reasoning ('laws of thought')",
            "Acting humanly": "Behaving like a human well enough to pass the Turing Test",
            "Acting rationally": "Building agents that do the right thing to achieve the best outcome",
        },
        "explanation": "These are the four approaches described by Russell and Norvig. Thinking "
                       "humanly = cognitive science; thinking rationally = logic; acting humanly = "
                       "Turing Test; acting rationally = the rational agent approach, which most "
                       "modern AI follows.",
        "hint": "The Turing Test is about behaviour, not thought processes.",
        "tags": [],
    },
    {
        "id": "Q03", "unit": "I", "topic": "Foundations and Applications of AI",
        "type": "MCQ", "difficulty": "Medium",
        "question": "AI borrowed decision theory (choosing actions by combining probability with "
                    "how much each outcome is worth) mainly from which field?",
        "options": [
            "Linguistics",
            "Neuroscience",
            "Computer engineering",
            "Economics",
        ],
        "answer": "Economics",
        "explanation": "Economics studies how to make decisions that maximise payoff (utility). "
                       "Decision theory, which combines probability theory with utility, came into "
                       "AI from economics. Linguistics gave us work on language, neuroscience on "
                       "the brain, and computer engineering gave us the hardware.",
        "hint": "Think about the field that talks about 'utility' and 'maximising payoff'.",
        "tags": [],
    },

    # ---------- Topic 2: Turing Test ----------
    {
        "id": "Q04", "unit": "I", "topic": "Turing Test",
        "type": "MCQ", "difficulty": "Easy",
        "question": "In the standard Turing Test, when is the machine said to pass?",
        "options": [
            "When the machine solves a mathematical problem faster than a human",
            "When the machine can physically walk and pick up objects like a human",
            "When a human interrogator, chatting by text, cannot reliably tell the machine from a human",
            "When the machine never makes a single mistake in conversation",
        ],
        "answer": "When a human interrogator, chatting by text, cannot reliably tell the machine from a human",
        "explanation": "Turing (1950) proposed the 'imitation game': an interrogator asks written "
                       "questions to a hidden human and a hidden machine. If the interrogator cannot "
                       "reliably tell which is which, the machine passes. Speed, physical skill and "
                       "perfection are not part of the test.",
        "hint": "The test is about whether a judge can tell the difference.",
        "tags": [],
    },
    {
        "id": "Q05", "unit": "I", "topic": "Turing Test",
        "type": "Assertion-Reason", "difficulty": "Medium",
        "question": "**Assertion (A):** To pass the Total Turing Test, a machine needs computer vision "
                    "and robotics, not just language skills.\n\n"
                    "**Reason (R):** In the Total Turing Test, the interrogator can test the subject's "
                    "ability to see and can pass physical objects to it.",
        "options": AR_OPTIONS,
        "answer": AR_A,
        "explanation": "Both statements are true. The Total Turing Test adds a video signal and the "
                       "passing of objects 'through the hatch'. Because of exactly that (the Reason), "
                       "the machine needs computer vision to perceive and robotics to handle "
                       "objects. So R correctly explains A.",
        "hint": "Ask yourself: why would vision and robotics be needed at all?",
        "tags": [],
    },
    {
        "id": "Q06", "unit": "I", "topic": "Turing Test",
        "type": "Scenario", "difficulty": "Medium",
        "question": "Before you can create an account, a website shows you blurred letters and asks you "
                    "to type them (a CAPTCHA). How is this related to the Turing Test?",
        "options": [
            "It is a reverse Turing Test: a computer is judging whether the user is a human",
            "It is the standard Turing Test: a human is judging whether the website is a machine",
            "It is the Total Turing Test, because it involves vision",
            "It is not related to the Turing Test at all",
        ],
        "answer": "It is a reverse Turing Test: a computer is judging whether the user is a human",
        "explanation": "In the normal Turing Test a human judges a machine. A CAPTCHA flips this "
                       "around: the website (a machine) acts as the judge and tries to tell humans "
                       "from bots. That is why CAPTCHA stands for 'Completely Automated Public "
                       "Turing test to tell Computers and Humans Apart'.",
        "hint": "Who is the judge here, a person or a computer?",
        "tags": ["real-world"],
    },

    # ---------- Topic 3: Rational Agents ----------
    {
        "id": "Q07", "unit": "I", "topic": "Rational Agents",
        "type": "MCQ", "difficulty": "Medium",
        "question": "What is rational for an agent at any moment depends on four things. Which of "
                    "these is NOT one of them?",
        "options": [
            "The performance measure that defines success",
            "Knowing in advance the actual outcome of every action",
            "The agent's prior knowledge of the environment",
            "The agent's percept sequence to date",
        ],
        "answer": "Knowing in advance the actual outcome of every action",
        "explanation": "Rationality depends on (1) the performance measure, (2) prior knowledge of "
                       "the environment, (3) the actions the agent can perform and (4) the percept "
                       "sequence so far. Knowing the actual outcome in advance would be omniscience, "
                       "which no real agent has and rationality does not require.",
        "hint": "One option describes being all-knowing.",
        "tags": [],
    },
    {
        "id": "Q08", "unit": "I", "topic": "Rational Agents",
        "type": "True/False", "difficulty": "Easy",
        "question": "A rational agent always chooses the action that turns out to be the best one in "
                    "hindsight.",
        "options": TRUE_FALSE,
        "answer": "False",
        "explanation": "A rational agent chooses the action that is expected to give the best result "
                       "based on what it has perceived and knows. It cannot see the future, so an "
                       "action can be rational and still turn out badly. Being right in hindsight "
                       "every time would require omniscience.",
        "hint": "Rational is not the same as all-knowing.",
        "tags": [],
    },
    {
        "id": "Q09", "unit": "I", "topic": "Rational Agents",
        "type": "Assertion-Reason", "difficulty": "Medium",
        "question": "**Assertion (A):** An agent that relies only on the knowledge its designer built "
                    "into it lacks autonomy.\n\n"
                    "**Reason (R):** A rational agent should learn what it can to make up for partial "
                    "or incorrect prior knowledge.",
        "options": AR_OPTIONS,
        "answer": AR_A,
        "explanation": "Both are true. Autonomy means the agent's behaviour depends on its own "
                       "experience, not only on built-in knowledge. The Reason states exactly why: a "
                       "rational agent is expected to learn and correct its prior knowledge. So R "
                       "explains A.",
        "hint": "What does an autonomous agent do that a fixed, pre-programmed one does not?",
        "tags": [],
    },

    # ---------- Topic 4: Intelligent Agents ----------
    {
        "id": "Q10", "unit": "I", "topic": "Intelligent Agents",
        "type": "Match the Following", "difficulty": "Medium",
        "question": "Match each type of agent (Column A) with how it decides what to do (Column B).",
        "answer": {
            "Simple reflex agent": "Uses condition-action rules on the current percept only",
            "Model-based reflex agent": "Keeps an internal state to track parts of the world it cannot see now",
            "Goal-based agent": "Thinks about which future actions will reach a desired goal",
            "Utility-based agent": "Chooses between ways of reaching a goal by how good (useful) each outcome is",
            "Learning agent": "Improves its own performance using feedback from a critic",
        },
        "explanation": "These are the five agent designs. Each one adds something to the previous: "
                       "reflex (rules only), model-based (memory of the world), goal-based (a goal), "
                       "utility-based (a measure of how good outcomes are) and learning (ability to "
                       "improve over time).",
        "hint": "'Utility' means how good or useful an outcome is.",
        "tags": [],
    },
    {
        "id": "Q11", "unit": "I", "topic": "Intelligent Agents",
        "type": "Scenario", "difficulty": "Easy",
        "question": "A basic room thermostat follows one rule: if the temperature is below 20 °C, "
                    "turn the heater on; otherwise turn it off. It keeps no history and has no "
                    "goals beyond this rule. Which type of agent is it?",
        "options": [
            "Model-based reflex agent",
            "Goal-based agent",
            "Learning agent",
            "Simple reflex agent",
        ],
        "answer": "Simple reflex agent",
        "explanation": "The thermostat reacts only to its current percept (the current temperature) "
                       "using a single condition-action rule. It stores no internal state, plans "
                       "nothing and does not learn. That is exactly a simple reflex agent.",
        "hint": "Does it remember anything or plan ahead?",
        "tags": ["real-world"],
    },
    {
        "id": "Q12", "unit": "I", "topic": "Intelligent Agents",
        "type": "MCQ", "difficulty": "Hard",
        "question": "In a learning agent, which component suggests new, exploratory actions that may "
                    "lead to useful experiences, even if they are not the best actions right now?",
        "options": [
            "Critic",
            "Learning element",
            "Problem generator",
            "Performance element",
        ],
        "answer": "Problem generator",
        "explanation": "A learning agent has four parts. The performance element chooses actions, "
                       "the critic says how well the agent is doing, the learning element makes "
                       "improvements, and the problem generator suggests exploratory actions so the "
                       "agent can discover better ways of behaving.",
        "hint": "This part 'generates' new things to try.",
        "tags": [],
    },

    # ---------- Topic 5: Agents and Environments ----------
    {
        "id": "Q13", "unit": "I", "topic": "Agents and Environments",
        "type": "Fill in the Blank", "difficulty": "Easy",
        "question": "An agent perceives its environment through ________ and acts upon that "
                    "environment through actuators.",
        "answer": ["sensors", "sensor"],
        "explanation": "This is the basic definition of an agent. Sensors take information in "
                       "(for example cameras, microphones, keyboard input). Actuators carry out "
                       "actions (for example motors, wheels, screen output).",
        "hint": "A camera on a robot is an example of one.",
        "tags": [],
    },
    {
        "id": "Q14", "unit": "I", "topic": "Agents and Environments",
        "type": "MCQ", "difficulty": "Medium",
        "question": "What is the difference between an agent function and an agent program?",
        "options": [
            "The agent function is an abstract mapping from percept sequences to actions; the agent program is the actual code that implements it on a machine",
            "The agent function is the hardware; the agent program is the environment",
            "They are two names for exactly the same thing",
            "The agent program maps actions to percepts; the agent function stores the percepts",
        ],
        "answer": "The agent function is an abstract mapping from percept sequences to actions; the agent "
                  "program is the actual code that implements it on a machine",
        "explanation": "The agent function is a mathematical description: for every possible percept "
                       "sequence, which action should be taken. The agent program is the concrete "
                       "implementation that runs on the agent's architecture. In short: "
                       "agent = architecture + program.",
        "hint": "One is a description on paper, the other actually runs.",
        "tags": [],
    },
    {
        "id": "Q15", "unit": "I", "topic": "Agents and Environments",
        "type": "Problem-Solving", "difficulty": "Easy",
        "question": "In the two-square vacuum world (squares A and B), a simple reflex agent follows "
                    "these rules in order:\n\n"
                    "1. If the current square is Dirty → **Suck**\n"
                    "2. Else if in square A → **Right**\n"
                    "3. Else if in square B → **Left**\n\n"
                    "The agent starts in square **A** and **both squares are dirty**. Which sequence "
                    "of actions makes both squares clean?",
        "options": [
            "Right, Suck, Left, Suck",
            "Suck, Right, Suck",
            "Suck, Left, Suck",
            "Suck, Suck, Right",
        ],
        "answer": "Suck, Right, Suck",
        "explanation": "Step 1: A is dirty, so Suck (A is now clean). Step 2: A is clean and the "
                       "agent is in A, so Right (move to B). Step 3: B is dirty, so Suck. Both "
                       "squares are now clean after 3 actions.",
        "hint": "Apply rule 1 first whenever the current square is dirty.",
        "tags": [],
    },

    # ---------- Topic 6: Good Behaviour in Intelligent Agents ----------
    {
        "id": "Q16", "unit": "I", "topic": "Good Behaviour in Intelligent Agents",
        "type": "Assertion-Reason", "difficulty": "Medium",
        "question": "**Assertion (A):** A vacuum-cleaner agent should be rewarded for having a clean "
                    "floor, not for the amount of dirt it sucks up.\n\n"
                    "**Reason (R):** An agent rewarded for the amount of dirt it sucks up could dump "
                    "the dirt back on the floor and clean it again to earn more reward.",
        "options": AR_OPTIONS,
        "answer": AR_A,
        "explanation": "Both are true, and R explains A. The rule is: design the performance measure "
                       "around what you actually want in the environment (a clean floor), not around "
                       "how you think the agent should behave. Otherwise the agent may 'game' the "
                       "measure.",
        "hint": "Think about how a badly designed reward can be cheated.",
        "tags": [],
    },
    {
        "id": "Q17", "unit": "I", "topic": "Good Behaviour in Intelligent Agents",
        "type": "Scenario", "difficulty": "Hard",
        "question": "A company rewards its customer-service chatbot for keeping calls short. After a "
                    "few weeks, the chatbot starts ending conversations before customers' problems "
                    "are solved. What is the main design mistake?",
        "options": [
            "The chatbot's environment is fully observable",
            "The chatbot does not have enough sensors",
            "The chatbot is a utility-based agent instead of a goal-based agent",
            "The performance measure rewards a behaviour (short calls) instead of the outcome the company actually wants (problems solved)",
        ],
        "answer": "The performance measure rewards a behaviour (short calls) instead of the outcome the "
                  "company actually wants (problems solved)",
        "explanation": "The agent is doing exactly what it was rewarded for. The fault is in the "
                       "performance measure. Good behaviour needs a measure based on the desired "
                       "result in the environment (satisfied customers, solved problems), just like "
                       "the 'clean floor' rule for the vacuum cleaner.",
        "hint": "The chatbot is behaving 'rationally' for the reward it was given.",
        "tags": ["real-world"],
    },
    {
        "id": "Q18", "unit": "I", "topic": "Good Behaviour in Intelligent Agents",
        "type": "True/False", "difficulty": "Easy",
        "question": "A rational agent may sometimes take an action only to gather information, such as "
                    "looking both ways before crossing a road.",
        "options": TRUE_FALSE,
        "answer": "True",
        "explanation": "Information gathering is part of rational behaviour. Looking before crossing "
                       "does not move you forward, but it improves the information you use to choose "
                       "the next action. Crossing without looking would not be rational.",
        "hint": "Is 'looking' a sensible thing for a careful agent to do?",
        "tags": [],
    },

    # ---------- Topic 7: Nature of Environments ----------
    {
        "id": "Q19", "unit": "I", "topic": "Nature of Environments",
        "type": "Scenario", "difficulty": "Easy",
        "question": "You are writing the PEAS description for a self-driving taxi. Which of the "
                    "following belongs under **Actuators**?",
        "options": [
            "Cameras, GPS, speedometer and LIDAR",
            "Safe, fast, legal and comfortable trips",
            "Steering, accelerator, brake, horn and indicators",
            "Roads, other traffic, pedestrians and weather",
        ],
        "answer": "Steering, accelerator, brake, horn and indicators",
        "explanation": "PEAS = Performance measure, Environment, Actuators, Sensors. Actuators are "
                       "what the agent uses to act (steering, accelerator, brake, horn). Cameras and "
                       "GPS are sensors, 'safe, fast, legal' is the performance measure, and roads "
                       "and traffic are the environment.",
        "hint": "Actuators are the parts that let the taxi DO something.",
        "tags": ["real-world"],
    },
    {
        "id": "Q20", "unit": "I", "topic": "Nature of Environments",
        "type": "Match the Following", "difficulty": "Hard",
        "question": "Match each task environment (Column A) with the property that best describes it "
                    "(Column B).",
        "answer": {
            "Crossword puzzle": "Fully observable, deterministic and static",
            "Automated taxi driving": "Partially observable, stochastic, multi-agent and dynamic",
            "Chess played with a clock": "Semi-dynamic (the board waits, but the clock keeps running)",
            "Part-picking robot on a conveyor belt": "Episodic (each part is a separate, independent decision)",
        },
        "explanation": "A crossword shows everything and never changes by itself. Taxi driving has "
                       "hidden information, other drivers and constant change. In timed chess the "
                       "board does not change while you think, but your score is affected by time, "
                       "so it is semi-dynamic. A part-picking robot decides about each part "
                       "independently, so its experience is episodic.",
        "hint": "Which one is affected by time passing even though the board stays still?",
        "tags": [],
    },
    {
        "id": "Q21", "unit": "I", "topic": "Nature of Environments",
        "type": "Assertion-Reason", "difficulty": "Medium",
        "question": "**Assertion (A):** Poker is a partially observable environment.\n\n"
                    "**Reason (R):** Poker is deterministic, because the cards cannot change once "
                    "they have been dealt.",
        "options": AR_OPTIONS,
        "answer": AR_C,
        "explanation": "The Assertion is true: you cannot see your opponents' cards, so poker is "
                       "partially observable. The Reason is false: the cards are dealt randomly and "
                       "you cannot predict what will come next, so poker is stochastic, not "
                       "deterministic.",
        "hint": "Is shuffling and dealing cards predictable?",
        "tags": [],
    },

    # ==========================================================
    # UNIT II
    # ==========================================================

    # ---------- Topic 8: Problems and Problem Spaces ----------
    {
        "id": "Q22", "unit": "II", "topic": "Problems and Problem Spaces",
        "type": "MCQ", "difficulty": "Easy",
        "question": "Which of these is NOT a required part of a well-defined search problem?",
        "options": [
            "A heuristic function",
            "An initial state",
            "A set of actions (operators)",
            "A goal test",
        ],
        "answer": "A heuristic function",
        "explanation": "A problem is defined by its initial state, the actions (operators) and their "
                       "results, a goal test and a path cost. A heuristic is optional: it helps "
                       "informed search go faster, but uninformed methods like BFS solve problems "
                       "without one.",
        "hint": "BFS can solve a problem without this.",
        "tags": [],
    },
    {
        "id": "Q23", "unit": "II", "topic": "Problems and Problem Spaces",
        "type": "Fill in the Blank", "difficulty": "Hard",
        "question": "The 8-puzzle has 9! = 362,880 possible arrangements, but only half of them can "
                    "be reached from any given start state. So the number of reachable states is "
                    "________.",
        "answer": ["181440", "181,440"],
        "explanation": "9! / 2 = 362,880 / 2 = 181,440. The arrangements split into two groups that "
                       "cannot be reached from each other (because of tile parity), so from any "
                       "start state only half of the arrangements are reachable.",
        "hint": "Divide 362,880 by 2.",
        "tags": ["search"],
    },
    {
        "id": "Q24", "unit": "II", "topic": "Problems and Problem Spaces",
        "type": "Scenario", "difficulty": "Easy",
        "question": "A sat-nav app is designed as a search problem to find a route from Coventry to "
                    "London. What is the most sensible choice for a **state** in this problem?",
        "options": [
            "The complete list of every road in the UK",
            "The town or road junction where the car currently is",
            "The speed limit of the current road",
            "The destination, London",
        ],
        "answer": "The town or road junction where the car currently is",
        "explanation": "A state should describe the situation at one moment, and it should change "
                       "as actions are taken. Here the car's current location is the state, driving "
                       "along a road is the action, and 'location = London' is the goal test. The "
                       "list of roads is part of the problem description, not a state.",
        "hint": "A state changes every time an action is taken.",
        "tags": ["real-world", "search"],
    },

    # ---------- Topic 9: State Space Search ----------
    {
        "id": "Q25", "unit": "II", "topic": "State Space Search",
        "type": "Problem-Solving", "difficulty": "Hard",
        "question": "**Water jug problem.** You have a 4-litre jug and a 3-litre jug, both empty, "
                    "with no markings. Allowed actions: fill a jug completely, empty a jug, or pour "
                    "from one jug into the other until the first is empty or the second is full. "
                    "The state is (x, y) = (litres in 4-L jug, litres in 3-L jug), starting at (0, 0). "
                    "What is the **minimum number of actions** needed to get exactly 2 litres in "
                    "the 4-litre jug?",
        "options": [
            "4",
            "5",
            "6",
            "7",
        ],
        "answer": "6",
        "explanation": "One shortest solution: (0,0) → (0,3) fill 3-L → (3,0) pour into 4-L → (3,3) "
                       "fill 3-L → (4,2) pour until 4-L is full → (0,2) empty 4-L → (2,0) pour the "
                       "2 litres into 4-L. That is 6 actions. A breadth-first search of the state "
                       "space confirms that no 5-action solution exists.",
        "hint": "Try getting 2 litres into the 3-litre jug first, then moving it.",
        "tags": ["search"],
    },
    {
        "id": "Q26", "unit": "II", "topic": "State Space Search",
        "type": "Problem-Solving", "difficulty": "Medium",
        "question": "In the water jug problem (4-litre jug, 3-litre jug), the state is written as "
                    "(x, y) = (litres in 4-L jug, litres in 3-L jug). The current state is **(2, 3)**. "
                    "Apply this rule: *pour water from the 3-L jug into the 4-L jug until the 4-L "
                    "jug is full*. Type the new state in the form x,y",
        "answer": ["4,1", "(4,1)", "4 1"],
        "explanation": "The 4-L jug has 2 litres, so it has room for 2 more. Pouring 2 litres from "
                       "the 3-L jug fills the 4-L jug (2 + 2 = 4) and leaves 3 − 2 = 1 litre in the "
                       "3-L jug. New state: (4, 1).",
        "hint": "How much space is left in the 4-litre jug?",
        "tags": ["search"],
    },
    {
        "id": "Q27", "unit": "II", "topic": "State Space Search",
        "type": "Assertion-Reason", "difficulty": "Medium",
        "question": "**Assertion (A):** Chess can be represented as a state space search problem.\n\n"
                    "**Reason (R):** Chess is a game played between two players.",
        "options": AR_OPTIONS,
        "answer": AR_B,
        "explanation": "Both statements are true, but R does not explain A. Chess can be a state "
                       "space problem because each board position is a state and each legal move is "
                       "an operator that changes one state into another. Having two players is a "
                       "true fact, but it is not the reason it fits the state space model.",
        "hint": "Both may be true. Is the second one really the reason for the first?",
        "tags": ["search"],
    },

    # ---------- Topic 10: Production Systems ----------
    {
        "id": "Q28", "unit": "II", "topic": "Production Systems",
        "type": "Match the Following", "difficulty": "Medium",
        "question": "Match each part of a production system (Column A) with its job (Column B).",
        "answer": {
            "Set of rules": "Condition-action pairs: a left side (pattern) and a right side (action)",
            "Knowledge database (working memory)": "Holds the facts that describe the current state of the task",
            "Control strategy": "Decides which rule to apply next and settles conflicts",
            "Rule applier": "Actually carries out the chosen rule",
        },
        "explanation": "A production system has these four parts. The rules say what can be done, "
                       "the database holds the current situation, the control strategy chooses the "
                       "rule, and the rule applier executes it.",
        "hint": "Which part makes the decision, and which part just does the work?",
        "tags": [],
    },
    {
        "id": "Q29", "unit": "II", "topic": "Production Systems",
        "type": "MCQ", "difficulty": "Hard",
        "question": "A production system in which applying one rule never prevents the later use of "
                    "another rule that could also have been applied when the first rule was chosen "
                    "is called:",
        "options": [
            "Non-monotonic production system",
            "Partially commutative production system",
            "Monotonic production system",
            "Irrecoverable production system",
        ],
        "answer": "Monotonic production system",
        "explanation": "In a monotonic system, using a rule never blocks other rules that were "
                       "already applicable, so nothing is 'lost'. A partially commutative system is "
                       "about the order of rules not mattering. 'Irrecoverable' describes a problem "
                       "type, not a production system.",
        "hint": "'Mono' suggests things only ever get added, never taken away.",
        "tags": [],
    },
    {
        "id": "Q30", "unit": "II", "topic": "Production Systems",
        "type": "Assertion-Reason", "difficulty": "Hard",
        "question": "**Assertion (A):** A control strategy that is systematic but does not cause "
                    "motion is good enough to solve a problem.\n\n"
                    "**Reason (R):** A good control strategy should be systematic, so that it does "
                    "not keep exploring the same useless sequences of states.",
        "options": AR_OPTIONS,
        "answer": AR_D,
        "explanation": "The Assertion is false: the first requirement of a good control strategy is "
                       "that it causes motion (changes the state). A strategy that keeps applying "
                       "the same rule and never changes the state never reaches the goal. The Reason "
                       "is true: the second requirement is that the strategy is systematic.",
        "hint": "Rich & Knight give two requirements for a good control strategy.",
        "tags": [],
    },

    # ---------- Topic 11: Problem Characteristics ----------
    {
        "id": "Q31", "unit": "II", "topic": "Problem Characteristics",
        "type": "Match the Following", "difficulty": "Hard",
        "question": "Match each problem (Column A) with how its solution steps can be treated "
                    "(Column B).",
        "answer": {
            "Theorem proving": "Ignorable: a useless step can simply be ignored",
            "8-puzzle": "Recoverable: a wrong move can be undone",
            "Chess": "Irrecoverable: a move cannot be taken back",
        },
        "explanation": "In theorem proving, a proved lemma that turns out to be useless can just be "
                       "ignored. In the 8-puzzle, you can slide a tile back to undo a move. In chess, "
                       "once a move is made it cannot be taken back, so each move needs careful "
                       "planning.",
        "hint": "Can you take back a move in chess?",
        "tags": [],
    },
    {
        "id": "Q32", "unit": "II", "topic": "Problem Characteristics",
        "type": "MCQ", "difficulty": "Medium",
        "question": "For which problem is a good solution **relative** (we must find the best "
                    "solution, not just any solution)?",
        "options": [
            "Travelling salesman: find the shortest route that visits every city once",
            "Water jug: find any sequence of moves that leaves 2 litres in the 4-L jug",
            "Find any valid proof of a given theorem",
            "Check whether a given chess position is checkmate",
        ],
        "answer": "Travelling salesman: find the shortest route that visits every city once",
        "explanation": "For the travelling salesman problem, a route is only 'good' when compared "
                       "with other routes: we want the shortest one, so it is a best-path problem. "
                       "For the water jug or theorem proving, any correct answer is acceptable "
                       "(any-path problems).",
        "hint": "Look for the word 'shortest'.",
        "tags": [],
    },
    {
        "id": "Q33", "unit": "II", "topic": "Problem Characteristics",
        "type": "Scenario", "difficulty": "Medium",
        "question": "A factory robot arm places parts on a fixed jig and always lands exactly where "
                    "planned. A delivery drone flying in gusty wind often ends up somewhere slightly "
                    "different from where it planned. Which problem characteristic best explains the "
                    "difference between them?",
        "options": [
            "Whether the problem can be broken into smaller sub-problems",
            "Whether the universe is predictable (certain outcome vs uncertain outcome)",
            "Whether the solution is a state or a path",
            "Whether the task needs interaction with a person",
        ],
        "answer": "Whether the universe is predictable (certain outcome vs uncertain outcome)",
        "explanation": "The robot arm works in a predictable universe: an action always gives the "
                       "expected result, so a full plan can be made in advance. The drone works in "
                       "an unpredictable universe, so it has to keep checking where it is and revise "
                       "its plan as it goes.",
        "hint": "Can the drone be sure what will happen after each action?",
        "tags": ["real-world"],
    },

    # ---------- Topic 12: Issues in Search Program Design ----------
    {
        "id": "Q34", "unit": "II", "topic": "Issues in Search Program Design",
        "type": "MCQ", "difficulty": "Medium",
        "question": "Which of the following is NOT one of the main issues in the design of search "
                    "programs?",
        "options": [
            "The direction of search (forward from the start or backward from the goal)",
            "How to choose which rules can be applied (matching)",
            "Whether to search a tree or a graph (handling repeated states)",
            "The speed of the computer's processor",
        ],
        "answer": "The speed of the computer's processor",
        "explanation": "The design issues are: the direction of search, how to select applicable "
                       "rules (matching), how to represent each node, and whether to treat the "
                       "search as a tree or a graph. Processor speed is a hardware matter, not a "
                       "search design decision.",
        "hint": "One option is about hardware, not about the search method.",
        "tags": [],
    },
    {
        "id": "Q35", "unit": "II", "topic": "Issues in Search Program Design",
        "type": "Scenario", "difficulty": "Hard",
        "question": "A medical diagnosis system knows hundreds of possible symptoms. A doctor suspects "
                    "one particular disease and wants the system to confirm or reject it, and to "
                    "explain its reasoning in the order a doctor would think. Which search direction "
                    "suits this best?",
        "options": [
            "Forward reasoning: start from all known symptoms and derive every possible conclusion",
            "Random search through the symptoms until the disease is found",
            "Backward reasoning: start from the suspected disease (goal) and check for the symptoms it needs",
            "Direction does not matter, because both always take the same effort",
        ],
        "answer": "Backward reasoning: start from the suspected disease (goal) and check for the symptoms it needs",
        "explanation": "There is one goal to check but many possible starting facts, so reasoning "
                       "backward from the goal has a much smaller branching factor. It also matches "
                       "how the doctor thinks ('if it is this disease, I should see these symptoms'), "
                       "which makes the explanation easier to follow.",
        "hint": "Move from the smaller set of states towards the larger set.",
        "tags": ["real-world"],
    },
    {
        "id": "Q36", "unit": "II", "topic": "Issues in Search Program Design",
        "type": "True/False", "difficulty": "Easy",
        "question": "Treating a search as a graph (checking whether a newly generated node has been "
                    "seen before) can save effort when the same state can be reached by different "
                    "paths.",
        "options": TRUE_FALSE,
        "answer": "True",
        "explanation": "In a tree search, the same state can be generated and explored many times. "
                       "Graph search keeps a record of generated nodes, so a repeated state is "
                       "recognised and not explored again. This costs some memory but can save a "
                       "lot of time.",
        "hint": "What happens if the same state is explored again and again?",
        "tags": [],
    },

    # ---------- Topic 13: Breadth-First Search (BFS) ----------
    {
        "id": "Q37", "unit": "II", "topic": "Breadth-First Search (BFS)",
        "type": "Problem-Solving", "difficulty": "Medium",
        "question": "Use **Breadth-First Search** on the tree below, starting at **A**, to find the goal "
                    "**G**.\n" + SEARCH_TREE +
                    "\nType the order in which the nodes are visited, ending with G "
                    "(for example: A B C ...).",
        "answer": ["A B C D E F G"],
        "explanation": "BFS uses a FIFO queue and visits the tree level by level. Level 0: A. "
                       "Level 1: B, C. Level 2: D, E, F, G. G is found at level 2, so the visit "
                       "order is A, B, C, D, E, F, G.",
        "hint": "Finish each level completely before going deeper.",
        "tags": ["search"],
    },
    {
        "id": "Q38", "unit": "II", "topic": "Breadth-First Search (BFS)",
        "type": "True/False", "difficulty": "Medium",
        "question": "Breadth-First Search always finds the lowest-cost path, even when different "
                    "steps have different costs.",
        "options": TRUE_FALSE,
        "answer": "False",
        "explanation": "BFS finds the path with the fewest steps (the shallowest goal). That is the "
                       "cheapest path only when every step costs the same. If step costs differ, a "
                       "longer path with cheaper steps may cost less, and Uniform Cost Search is "
                       "needed instead.",
        "hint": "Fewest steps and lowest cost are not always the same.",
        "tags": ["search"],
    },
    {
        "id": "Q39", "unit": "II", "topic": "Breadth-First Search (BFS)",
        "type": "Scenario", "difficulty": "Easy",
        "question": "A social networking site wants to show 'how you are connected' to another user: "
                    "the shortest chain of friends between you and them (fewest connections). Every "
                    "friendship link counts the same. Which search method fits best?",
        "options": [
            "Breadth-First Search",
            "Depth-First Search",
            "Hill Climbing",
            "Greedy Best-First Search",
        ],
        "answer": "Breadth-First Search",
        "explanation": "BFS explores friends, then friends of friends, and so on, level by level. "
                       "Because each link has the same cost, the first time BFS reaches the other "
                       "user it has found the chain with the fewest connections. DFS might find a "
                       "very long chain first.",
        "hint": "Explore all direct friends first, then friends of friends.",
        "tags": ["real-world", "search"],
    },

    # ---------- Topic 14: Depth-First Search (DFS) ----------
    {
        "id": "Q40", "unit": "II", "topic": "Depth-First Search (DFS)",
        "type": "Problem-Solving", "difficulty": "Medium",
        "question": "Use **Depth-First Search** on the tree below, starting at **A**, to find the goal "
                    "**F**.\n" + SEARCH_TREE +
                    "\nType the order in which the nodes are visited, ending with F "
                    "(for example: A B ...).",
        "answer": ["A B D E H C F"],
        "explanation": "DFS uses a stack (LIFO) and always goes deeper first. A → B → D (dead end) → "
                       "back to E → H (dead end) → back up to C → F (goal). Visit order: A, B, D, E, "
                       "H, C, F.",
        "hint": "Go as deep as possible down the left side before trying the right side.",
        "tags": ["search"],
    },
    {
        "id": "Q41", "unit": "II", "topic": "Depth-First Search (DFS)",
        "type": "Assertion-Reason", "difficulty": "Hard",
        "question": "**Assertion (A):** Depth-First Search usually needs much less memory than "
                    "Breadth-First Search.\n\n"
                    "**Reason (R):** Depth-First Search always finds the shallowest goal first.",
        "options": AR_OPTIONS,
        "answer": AR_C,
        "explanation": "The Assertion is true: DFS stores only the current path plus the unexplored "
                       "siblings along it, which is O(b·m) memory, while BFS stores whole levels, "
                       "which is O(b^d). The Reason is false: finding the shallowest goal first is a "
                       "property of BFS, not DFS.",
        "hint": "Which algorithm goes level by level?",
        "tags": ["search"],
    },
    {
        "id": "Q42", "unit": "II", "topic": "Depth-First Search (DFS)",
        "type": "True/False", "difficulty": "Medium",
        "question": "Depth-First Search is guaranteed to find a solution even in a state space that "
                    "contains infinitely deep paths.",
        "options": TRUE_FALSE,
        "answer": "False",
        "explanation": "If DFS goes down an infinitely deep path that has no goal, it will keep "
                       "going forever and never come back to try other branches. So DFS is not "
                       "complete in infinite state spaces. Depth-limited search or IDS fixes this.",
        "hint": "What happens if the first path DFS chooses never ends?",
        "tags": ["search"],
    },

    # ---------- Topic 15: Iterative Deepening Search ----------
    {
        "id": "Q43", "unit": "II", "topic": "Iterative Deepening Search",
        "type": "Problem-Solving", "difficulty": "Hard",
        "question": "Use **Iterative Deepening Search** on the tree below, starting at **A**, to find "
                    "the goal **F**. The depth limit starts at 0 and goes up by 1 each round.\n"
                    + SEARCH_TREE +
                    "\nCounting every visit in every round (repeats included), how many node visits "
                    "happen in total, up to and including finding F?",
        "options": [
            "6",
            "9",
            "10",
            "13",
        ],
        "answer": "10",
        "explanation": "Limit 0: A (1 visit). Limit 1: A, B, C (3 visits). Limit 2: A, B, D, E, C, F "
                       "(6 visits, F found). Total = 1 + 3 + 6 = 10. Note that in the last round "
                       "the search stops at F, so G is never visited.",
        "hint": "Write out each round separately, then add them up.",
        "tags": ["search"],
    },
    {
        "id": "Q44", "unit": "II", "topic": "Iterative Deepening Search",
        "type": "MCQ", "difficulty": "Medium",
        "question": "What is the space (memory) complexity of Iterative Deepening Search? "
                    "(b = branching factor, d = depth of the shallowest goal)",
        "options": [
            "O(b^d)",
            "O(d^b)",
            "O(b^(d+1))",
            "O(b·d)",
        ],
        "answer": "O(b·d)",
        "explanation": "Each round of IDS is a depth-limited DFS, so it only stores one path plus "
                       "the siblings along it: O(b·d). This is the main advantage of IDS over BFS, "
                       "which needs O(b^d) memory.",
        "hint": "Each round of IDS is really a DFS.",
        "tags": ["search"],
    },
    {
        "id": "Q45", "unit": "II", "topic": "Iterative Deepening Search",
        "type": "True/False", "difficulty": "Hard",
        "question": "Even though Iterative Deepening Search re-generates the upper levels of the tree "
                    "in every round, its total work is usually not much more than BFS, because most "
                    "nodes of a tree are on the bottom level.",
        "options": TRUE_FALSE,
        "answer": "True",
        "explanation": "With branching factor b = 10 and depth d = 5, BFS generates 111,110 nodes "
                       "while IDS generates 123,450, only about 11% more. The bottom level holds "
                       "most of the nodes and is generated only once, so repeating the small upper "
                       "levels costs little.",
        "hint": "Where are most of the nodes in a tree with a large branching factor?",
        "tags": ["search"],
    },

    # ---------- Topic 16: Hill Climbing and Its Variations ----------
    {
        "id": "Q46", "unit": "II", "topic": "Hill Climbing and Its Variations",
        "type": "Problem-Solving", "difficulty": "Medium",
        "question": "Seven states lie in a line. Each state's neighbours are the states directly to "
                    "its left and right. Their values are:\n\n"
                    "| S1 | S2 | S3 | S4 | S5 | S6 | S7 |\n|---|---|---|---|---|---|---|\n"
                    "| 3 | 5 | 8 | 6 | 7 | 12 | 10 |\n\n"
                    "Using **steepest-ascent hill climbing** to **maximise** the value, starting "
                    "from **S2**, where does the search stop?",
        "options": [
            "S6, which is the global maximum",
            "S7, the last state",
            "S3, which is a local maximum",
            "S1, the lowest state",
        ],
        "answer": "S3, which is a local maximum",
        "explanation": "From S2 (5), the neighbours are S1 (3) and S3 (8). The best is S3, so move to "
                       "S3. From S3 (8), the neighbours are S2 (5) and S4 (6). Neither is better, so "
                       "the search stops at S3. It is stuck on a local maximum, even though S6 (12) "
                       "is higher.",
        "hint": "Hill climbing only moves if a neighbour is strictly better.",
        "tags": ["search"],
    },
    {
        "id": "Q47", "unit": "II", "topic": "Hill Climbing and Its Variations",
        "type": "Match the Following", "difficulty": "Hard",
        "question": "Match each hill-climbing problem (Column A) with a common way to deal with it "
                    "(Column B).",
        "answer": {
            "Local maximum": "Backtrack to an earlier state and try a different direction",
            "Plateau": "Make a big jump to a new part of the search space",
            "Ridge": "Apply two or more rules (move in several directions) before testing",
        },
        "explanation": "At a local maximum all neighbours are worse, so going back and trying "
                       "another direction helps. On a plateau all neighbours have the same value, so "
                       "a big jump is needed to find a slope. On a ridge, single moves all go down, "
                       "but combining moves can still go up.",
        "hint": "On a flat plateau, small steps tell you nothing.",
        "tags": ["search"],
    },
    {
        "id": "Q48", "unit": "II", "topic": "Hill Climbing and Its Variations",
        "type": "Scenario", "difficulty": "Hard",
        "question": "A delivery company uses hill climbing to improve the order of stops for its vans. "
                    "It often gets stuck on routes that are good but not the best. The team decides to "
                    "run hill climbing many times, each time from a different randomly chosen route, "
                    "and keep the best result. Which variation is this?",
        "options": [
            "Random-restart hill climbing",
            "Simulated annealing",
            "Steepest-ascent hill climbing",
            "Simple hill climbing",
        ],
        "answer": "Random-restart hill climbing",
        "explanation": "Random-restart hill climbing runs a series of hill-climbing searches from "
                       "random starting points and keeps the best answer found. Each run may get "
                       "stuck on a local maximum, but with enough restarts the chance of finding a "
                       "very good route is high. Simulated annealing instead allows some downhill "
                       "moves within one run.",
        "hint": "The key words are 'many times' and 'randomly chosen start'.",
        "tags": ["real-world", "search"],
    },
    {
        "id": "Q49", "unit": "II", "topic": "Hill Climbing and Its Variations",
        "type": "Assertion-Reason", "difficulty": "Medium",
        "question": "**Assertion (A):** Hill climbing is guaranteed to find the global maximum.\n\n"
                    "**Reason (R):** Hill climbing only looks at the neighbours of the current state "
                    "and does not keep a search tree.",
        "options": AR_OPTIONS,
        "answer": AR_D,
        "explanation": "The Assertion is false: hill climbing can get stuck on local maxima, plateaus "
                       "and ridges. The Reason is true: it only looks at neighbouring states and "
                       "remembers nothing else, which is exactly why it can get stuck.",
        "hint": "Look back at the S1 to S7 problem.",
        "tags": ["search"],
    },

    # ---------- Topic 17: Heuristic Search ----------
    {
        "id": "Q50", "unit": "II", "topic": "Heuristic Search",
        "type": "Problem-Solving", "difficulty": "Medium",
        "question": "Look at this 8-puzzle (0 is the blank):\n\n"
                    "```\nCurrent state      Goal state\n 2 8 3              1 2 3\n"
                    " 1 6 4              8 0 4\n 7 0 5              7 6 5\n```\n"
                    "Heuristic h1 = the number of **misplaced tiles** (do not count the blank). "
                    "What is h1 for the current state?",
        "answer": ["4", "four"],
        "explanation": "Compare each tile with the goal: 2 (wrong), 8 (wrong), 3 (correct), "
                       "1 (wrong), 6 (wrong), 4 (correct), 7 (correct), 5 (correct). Four tiles are "
                       "out of place, so h1 = 4.",
        "hint": "Go through tiles 1 to 8 one by one and compare positions.",
        "tags": ["search"],
    },
    {
        "id": "Q51", "unit": "II", "topic": "Heuristic Search",
        "type": "Problem-Solving", "difficulty": "Hard",
        "question": "Using the same 8-puzzle (0 is the blank):\n\n"
                    "```\nCurrent state      Goal state\n 2 8 3              1 2 3\n"
                    " 1 6 4              8 0 4\n 7 0 5              7 6 5\n```\n"
                    "Heuristic h2 = the **Manhattan distance**: for each tile, count how many rows plus "
                    "columns it is away from its goal position, then add them up (ignore the blank). "
                    "What is h2?",
        "options": [
            "4",
            "5",
            "6",
            "7",
        ],
        "answer": "5",
        "explanation": "Tile 2: 1 move (one column). Tile 8: 2 moves (one row + one column). "
                       "Tile 1: 1 move (one row). Tile 6: 1 move (one row). Tiles 3, 4, 5, 7 are "
                       "already in place (0). Total = 1 + 2 + 1 + 1 = 5. Note that h2 (5) ≥ h1 (4): "
                       "Manhattan distance is the more informed heuristic.",
        "hint": "Tile 8 needs to move both up/down and left/right.",
        "tags": ["search"],
    },
    {
        "id": "Q52", "unit": "II", "topic": "Heuristic Search",
        "type": "MCQ", "difficulty": "Medium",
        "question": "When is a heuristic function h(n) called **admissible**?",
        "options": [
            "When it always gives exactly the true cost to the goal",
            "When it always gives a value larger than the true cost",
            "When it gives the same value for every node",
            "When it never overestimates the true cost of reaching the goal from n",
        ],
        "answer": "When it never overestimates the true cost of reaching the goal from n",
        "explanation": "An admissible heuristic is optimistic: h(n) ≤ true cost to the goal. "
                       "Straight-line distance on a map is a classic example, since no road can be "
                       "shorter than a straight line. With an admissible heuristic, A* tree search "
                       "is guaranteed to find an optimal path.",
        "hint": "Think of straight-line distance compared with road distance.",
        "tags": ["search"],
    },
    {
        "id": "Q53", "unit": "II", "topic": "Heuristic Search",
        "type": "True/False", "difficulty": "Easy",
        "question": "Any heuristic function guarantees that the search will find the best (optimal) "
                    "solution.",
        "options": TRUE_FALSE,
        "answer": "False",
        "explanation": "A heuristic is a rule of thumb. It usually makes search much faster, but it "
                       "can trade away the guarantee of the best solution. Optimality is only "
                       "guaranteed in special cases, such as A* with an admissible heuristic.",
        "hint": "A heuristic is a 'rule of thumb'. Are rules of thumb always right?",
        "tags": [],
    },

    # ---------- Topic 18: Best-First Search ----------
    {
        "id": "Q54", "unit": "II", "topic": "Best-First Search",
        "type": "Problem-Solving", "difficulty": "Medium",
        "question": "Use **Greedy Best-First Search**, which always expands the node with the lowest "
                    "**h(n)**, on this graph.\n" + WEIGHTED_GRAPH +
                    "\nWhich path does Greedy Best-First Search return, and what is its total cost?",
        "options": [
            "S → B → C → G, cost 7",
            "S → A → G, cost 2",
            "S → A → G, cost 11",
            "S → B → C → G, cost 11",
        ],
        "answer": "S → A → G, cost 11",
        "explanation": "Expand S: frontier = A (h=2), B (h=4). Lowest h is A, so expand A: it adds "
                       "G (h=0). Lowest h is now G, so G is taken out and the goal is found. Path "
                       "S → A → G with cost 2 + 9 = 11. Greedy only looks at h(n), so it ignores "
                       "that the path through B is cheaper.",
        "hint": "Ignore the step costs while choosing; only look at h(n).",
        "tags": ["search"],
    },
    {
        "id": "Q55", "unit": "II", "topic": "Best-First Search",
        "type": "Problem-Solving", "difficulty": "Hard",
        "question": "Now use **A\\* search**, which expands the node with the lowest "
                    "**f(n) = g(n) + h(n)**, on the same graph.\n" + WEIGHTED_GRAPH +
                    "\nWhich path does A* return, and what is its total cost?",
        "options": [
            "S → B → C → G, cost 7",
            "S → A → G, cost 11",
            "S → B → C → G, cost 9",
            "S → A → G, cost 4",
        ],
        "answer": "S → B → C → G, cost 7",
        "explanation": "Expand S: A f = 2+2 = 4, B f = 3+4 = 7. Expand A (4): G f = 11+0 = 11. "
                       "Frontier: B (7), G (11). Expand B (7): C f = 5+2 = 7. Expand C (7): G f = "
                       "7+0 = 7, which is better than the old G (11). Take out G (7): goal found. "
                       "Path S → B → C → G, cost 7. The heuristic is admissible, so A* finds the "
                       "optimal path, unlike Greedy.",
        "hint": "g(n) is the cost so far; add it to h(n) every time.",
        "tags": ["search"],
    },
    {
        "id": "Q56", "unit": "II", "topic": "Best-First Search",
        "type": "Fill in the Blank", "difficulty": "Easy",
        "question": "In Best-First Search, nodes that have been generated but not yet expanded are "
                    "kept in the ________ list, while nodes that have already been expanded are kept "
                    "in the CLOSED list.",
        "answer": ["open", "open list"],
        "explanation": "The OPEN list is a priority queue of nodes waiting to be expanded, ordered "
                       "by their heuristic (or f) value. The CLOSED list stores nodes already "
                       "expanded, so the search can tell when it has met a node before.",
        "hint": "It is the opposite of CLOSED.",
        "tags": ["search"],
    },
    {
        "id": "Q57", "unit": "II", "topic": "Best-First Search",
        "type": "Assertion-Reason", "difficulty": "Medium",
        "question": "**Assertion (A):** Greedy Best-First Search is not guaranteed to find the "
                    "lowest-cost path.\n\n"
                    "**Reason (R):** Greedy Best-First Search uses only h(n), the estimated cost to "
                    "the goal, and ignores g(n), the cost already spent.",
        "options": AR_OPTIONS,
        "answer": AR_A,
        "explanation": "Both are true and R explains A. Because Greedy ignores how much a path has "
                       "already cost, it can rush towards a node that looks close to the goal but "
                       "is reached by an expensive route (as in the S, A, B, C, G example). A* fixes "
                       "this by using f(n) = g(n) + h(n).",
        "hint": "What does A* add that Greedy does not have?",
        "tags": ["search"],
    },

    # ---------- Topic 19: Constraint Satisfaction Problems (CSP) ----------
    {
        "id": "Q58", "unit": "II", "topic": "Constraint Satisfaction Problems (CSP)",
        "type": "Problem-Solving", "difficulty": "Medium",
        "question": "Four regions P, Q, R and S must be coloured so that no two neighbouring regions "
                    "have the same colour. The neighbours are: **P–Q, Q–R, R–S, S–P and P–R**. "
                    "What is the **minimum** number of colours needed?",
        "options": [
            "2",
            "3",
            "4",
            "5",
        ],
        "answer": "3",
        "explanation": "P, Q and R are all neighbours of each other (a triangle), so they need 3 "
                       "different colours. S touches P and R but not Q, so S can use Q's colour. "
                       "Example: P = red, Q = green, R = blue, S = green. So 3 colours are enough, "
                       "and 2 are not.",
        "hint": "Look for three regions that all touch each other.",
        "tags": ["search"],
    },
    {
        "id": "Q59", "unit": "II", "topic": "Constraint Satisfaction Problems (CSP)",
        "type": "Problem-Solving", "difficulty": "Hard",
        "question": "In the cryptarithmetic puzzle **SEND + MORE = MONEY**, each letter stands for a "
                    "different digit and leading letters cannot be 0. What digit must **M** be?",
        "answer": ["1", "one"],
        "explanation": "SEND and MORE are both 4-digit numbers, so their sum is at most "
                       "9999 + 9999 = 19,998. MONEY is a 5-digit number, so its first digit M can "
                       "only be the carry from adding two 4-digit numbers, which is 1. (The full "
                       "solution is 9567 + 1085 = 10652.)",
        "hint": "What is the largest possible sum of two 4-digit numbers?",
        "tags": ["search"],
    },
    {
        "id": "Q60", "unit": "II", "topic": "Constraint Satisfaction Problems (CSP)",
        "type": "MCQ", "difficulty": "Medium",
        "question": "In backtracking search for a CSP, the **Minimum Remaining Values (MRV)** "
                    "heuristic chooses which variable next?",
        "options": [
            "The variable with the most legal values left in its domain",
            "The variable that comes first in alphabetical order",
            "A variable chosen at random",
            "The variable with the fewest legal values left in its domain",
        ],
        "answer": "The variable with the fewest legal values left in its domain",
        "explanation": "MRV picks the 'most constrained' variable. If a variable has only one or two "
                       "values left, trying it first quickly shows whether the current partial "
                       "assignment will fail, which cuts down backtracking. It is also called the "
                       "'fail-first' heuristic.",
        "hint": "It is also called the 'fail-first' heuristic.",
        "tags": [],
    },
    {
        "id": "Q61", "unit": "II", "topic": "Constraint Satisfaction Problems (CSP)",
        "type": "Scenario", "difficulty": "Easy",
        "question": "A university wants to build its exam timetable as a CSP. Each exam is a variable "
                    "and the possible time slots are its domain. Which of these is a **constraint**?",
        "options": [
            "The list of all exams to be scheduled",
            "The set of time slots in the exam week",
            "Two exams that share a student cannot be in the same time slot",
            "The name of the software used to print the timetable",
        ],
        "answer": "Two exams that share a student cannot be in the same time slot",
        "explanation": "A CSP has variables (the exams), domains (the time slots) and constraints "
                       "(rules on which combinations are allowed). 'No student sits two exams at "
                       "once' limits which slots exams can take together, so it is a constraint. "
                       "The list of exams is the variables and the time slots are the domain.",
        "hint": "A constraint is a rule that limits which values can go together.",
        "tags": ["real-world"],
    },

    # ---------- Topic 20: Means-End Analysis ----------
    {
        "id": "Q62", "unit": "II", "topic": "Means-End Analysis",
        "type": "MCQ", "difficulty": "Easy",
        "question": "What is the main idea of Means-End Analysis?",
        "options": [
            "Find the difference between the current state and the goal, then choose an operator that reduces that difference",
            "Always expand the shallowest node first",
            "Pick a random neighbour and move to it if it is better",
            "Assign values to variables while respecting all constraints",
        ],
        "answer": "Find the difference between the current state and the goal, then choose an operator "
                  "that reduces that difference",
        "explanation": "Means-End Analysis compares where you are with where you want to be, finds "
                       "the most important difference, and picks an operator (the 'means') that "
                       "reduces it. If that operator cannot be applied yet, reaching its "
                       "preconditions becomes a new sub-goal. The other options describe BFS, "
                       "hill climbing and CSP.",
        "hint": "'Ends' are the goals and 'means' are the operators.",
        "tags": [],
    },
    {
        "id": "Q63", "unit": "II", "topic": "Means-End Analysis",
        "type": "Fill in the Blank", "difficulty": "Easy",
        "question": "In Means-End Analysis, the table that lists which operators can reduce each kind "
                    "of difference is called a ________ table.",
        "answer": ["difference", "difference table"],
        "explanation": "The difference table links each type of difference (for example 'object is "
                       "in the wrong room') to the operators that can reduce it (for example PUSH or "
                       "CARRY). Means-End Analysis looks up this table to decide what to do next.",
        "hint": "MEA is all about reducing these.",
        "tags": [],
    },
    {
        "id": "Q64", "unit": "II", "topic": "Means-End Analysis",
        "type": "Scenario", "difficulty": "Medium",
        "question": "You are at home in Coventry and need to be at a 9 am interview in central London. "
                    "Using Means-End Analysis, what should you deal with first?",
        "options": [
            "Walking to the front door first, because it is the first physical step",
            "The biggest difference, the distance between Coventry and London, by choosing an operator such as 'take the train'; getting to the station and from the London station to the office become smaller sub-problems",
            "Trying every possible route at random until one works",
            "Planning what to say in the interview, because it is the final goal",
        ],
        "answer": "The biggest difference, the distance between Coventry and London, by choosing an "
                  "operator such as 'take the train'; getting to the station and from the London station "
                  "to the office become smaller sub-problems",
        "explanation": "MEA tackles the most important difference first. The main gap is roughly "
                       "100 miles, so the operator 'take a train' is chosen. Its precondition (being "
                       "at Coventry station) and what is left after it (getting from Euston to the "
                       "office) become smaller sub-goals that are solved the same way.",
        "hint": "Start with the largest gap between where you are and where you need to be.",
        "tags": ["real-world"],
    },
    {
        "id": "Q65", "unit": "II", "topic": "Means-End Analysis",
        "type": "Assertion-Reason", "difficulty": "Hard",
        "question": "**Assertion (A):** Means-End Analysis was the main reasoning method in the "
                    "General Problem Solver (GPS) developed by Newell and Simon.\n\n"
                    "**Reason (R):** In Means-End Analysis, when an operator's preconditions are not "
                    "met, meeting them becomes a new sub-goal (operator subgoaling).",
        "options": AR_OPTIONS,
        "answer": AR_B,
        "explanation": "Both statements are true. GPS (Newell and Simon) was built around Means-End "
                       "Analysis, and MEA does use operator subgoaling. However, R only describes "
                       "how MEA works; it does not explain why MEA was used in GPS. So the answer "
                       "is B.",
        "hint": "Both facts are true. Does the second one explain the first?",
        "tags": [],
    },
]
