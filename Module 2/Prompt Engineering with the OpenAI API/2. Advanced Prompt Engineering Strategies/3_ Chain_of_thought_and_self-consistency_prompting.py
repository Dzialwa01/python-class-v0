# Dzialwa Nemakonde
# 13 May 2026

# Chain-of-Thought and Self-Consistency Prompting - Learning prompting techniques that help us understand how an AI model arrives at it answer and not just the final answer.


## What is Chain-of-Thought Prompting?
# This means asking the AI to explain its thinking step by step before giving the final answer.
# This is very useful for: math problems, logical reasoning and multi-step decision making.
# It makes the model think out loud instead of jumping straight to the answer.


## Standard prompt vs Chain-of-Thought Prompt

# Example Problem:
# Rahul has 10 books, he gives 3 books to his friend. Then he buys 5 more books. How many books does Rahul have now?

# Standard prompt - "How many books does Rahul have now?" -> Model output - 12
# - We obtain the answer but we don't know how the model calculated it and we cannot easily check if it's correct

# Chain-of-Thought Prompting - "Solve the problem step by step and explain your reasoning." -> Model output:
# 1. Rahul starts with 10 books
# 2. He gives away 3 books → 10 − 3 = 7
# 3. He buys 5 more books → 7 + 5 = 12
# 4. Final answer: 12 books

# Now we can clearly see and verify each step.


## Chain-of-Thought prompting
# In contrast to multi-step prompting, in chain-of-though prompting we do not give the steps the model must follow, we ask the model to generate its own steps.
# e.g. "Solve the problem and explain your thinking"
# This helps us to understand the logic of the model, debug mistakes and trust the answer more.

# One big limitation of chain-of-thought is that if the model makes a mistake in one step, the final will also be wrong. This is where self-consistency prompting helps.


## What is Self-Consistency Prompting
# This means the model solves the same problem multiple times and each time, it uses a different reasoning path and then we choose the most common final answer.

# Example problem: There are cars in a parking lot. 5 cars leave, and 7 new cars enter. Finally, how many cars are there?
# Prompt: "Imagine three independent experts solving this problem. Each expert explains their reasoning. Choose the final answer by majority rule."

# This method reduces errors, improves reliability and works well for complex reasoning tasks.