# Dzialwa Nemakonde
# 26 February 2026

# 1. Shot Prompting (Introduction)
# AI can generate text when we give it a prompt. But the big question is: how do we get better and more accurate answers from the AI?
# The answer is by simply writing better prompts.


# 2. Proving Examples
# One powerful way to improve AI answers is by giving examples inside the prompt
# WHen we show AI what we want, it understands our expectation more clearly -> This is called shot prompting


# 3. What is Shot Prompting?
# Shot prompting means adding examples to your prompt to guide the AI
# There are three main typres:

## Zero-shot prompting -. No examples, only instructions.
## One-shot prompting -> One example is given.
## Few-shot prompting -> Multiple examples are given
# The more examples we give, the better the AI understands the task.


# 4. Why is Short Prompt Important?
# Giving examples helps AI perform better in many tasks, such as:

## Classification -> putting text into categories
## Sentiment analysis -> finding emotions like positive or negative
## Data extraction -> pulling specific information from text
# In short better prompts = better results.


# 5. Zero-Shot Prompting (No Examples)
# Let's say we want Ai to rate restaurant reviews with 1 = very bad and 5 = amazing

# In zero-shot prompting, we only give instructions, like: "Give a number from 1 to 5 for each review"
# Because we did not show any example, the AI gave the number and added extra text like "Neutral" which we did not ask for.


# 6. One-Shot Prompting ( One Example)
# Now we add one example before the real reviews
# Example - The food was terrible -> 1
# This assists the Ai understand thatonly the number is needed amd also the format that we want which makes the output cleaner and more accurate.


# 7. Few-Shot Prompting ( Multiple Examples)
# We now add two or three examples which is called few-shot prompting
# With more examples formatting becomes more consistent and scores become more reasonable
# Usually, more examples = better understanding


# 8. General Categorisation ( Without Examples)
# Shot prompting is not just for sentiment analysis. 

# Example task: " Categorise animals as land, sea, or both"
# Without examples, the AI explains its reasoning (even when we didn't ask). It is also more prone to making mistakes, like labeling salmon as "Both"


# 9. Few-Shot prompting for Categories
# Now we add examples like: Zebra = Land; Crocodile = Both.
# We also show the exact formatting using =
# AFter implementing this, prompting becomes perfect an wrong answers are fixed because examples remove confusion.


# Exercise done in the AI_Application repository
# **Zero-shot prompting with reviews**

# As well as answering questions, transforming text, and generating new text, OpenAI's models can also be used for classification tasks, such as categorization and sentiment analysis.

# In this exercise, you'll explore using OpenAI's chat models for sentiment classification using reviews from an online shoe store called *Toe-Tally Comfortable*.

# **Instruction**

# - Define a `prompt` to classify the sentiment of the statements provided using the numbers `1` to `5` (positive to negative).
# - Create a request to the Chat Completions endpoint to send this prompt to `gpt-4o-mini`.