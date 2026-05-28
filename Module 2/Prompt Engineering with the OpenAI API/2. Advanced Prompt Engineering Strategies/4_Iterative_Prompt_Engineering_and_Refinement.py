# Dzialwa Nemakonde
# 14 May 2026

# Iterative prompt engineering - This is improving a prompt step by step until we get the output we really want.

# Prompt engineering does not always work perfectly on the first try. So we follow a simple cycle:
# 1. Write a prompt
# 2. Give it to the model
# 3. Look at the Output 
# 4. Analyse what is missing or wrong
# 5. Refine the prompt

# This is done because sometimes the model misunderstands what we want
# It also helps us customise the level of detail


## Example: Analysing a Python Function
# Take a python function that calculates the area of a rectangle using length and width.

# Intial prompt: " Analyse the following code in one sentence."
# Model output: "This code calculates the area of a rectangle using length and width."
# This is correct but the are missing details such as the programming language. So we refine the prompt

# Refined prompt: "Analyze the following code in one sentence and mention the programming language."
# Model output: "This Python function calculates the area of a rectangle using length and width."


# Example: Structured Prompt Refinement
# Suppose we now want more structured information.

# Refined prompt: "Analyse the following funtion and provide: Short description, Python language, Inputs and Outputs"
# Model Output: # Model Output:
# - Description: Calculates the area of a rectangle
# - Language: Python
# - Inputs: length, width
# - Output: area of the rectangle

# Prompt refinement applies to all prompt types
# - Few-shot prompts → refine examples
# - Multi-step prompts → refine steps
# - Chain-of-thought prompts → refine problem description
# - Self-consistency prompts → refine reasoning instructions