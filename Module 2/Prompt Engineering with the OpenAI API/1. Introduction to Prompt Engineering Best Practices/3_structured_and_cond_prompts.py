# Dzialwa Nemakonde
# 07 May 2026

# Structured outputs and conditional prompts

## Intro 
# Objective is to learn how to get structured outputs from a language model and also use conditional prompts to control responses logically
# These techniques help to get clean, predictable, and useful outputs instead of a random text.


## Structured Outputs
# These include tables, lists, formatted paragraphs and custom layouts.
# In order to obtain these stuctured outputs, we must explicitely tell the model to create them i.e. 'Create a table'


## Structured paragraphs
# Sometimes we want paragraphs with headings, subheadings and organised sections. To achieve this, we must mention the structure in the prompt. e.g.,
# "Write a structured paragraph about the benefits of exercise. Use the following headings:- Introduction- Physical Health Benefits- Mental Health Benefits"
# With this, the model produces clear headings, relevant content under each heading and also organized and readable output.

## Custom Output Formats
# Sometimes, we need custom formats that don't fit tables or lists
# The best approach is to break the prompt into: instructions; output format; input text
# e.g.: Custom Format (Story Title) 
# input text "Once upon a time, there was a boy named David who loved exploring forests..."
# Prompt: You are given a story opening.Tasks:1. Generate a suitable title for the story.2. Keep the original text unchanged.
#         Output format:Title: <generated title> Story: <originaltext>


## Conditional prompts
# These allow us to add logic inside a prompt similar to if-else in programming.
# e.g., : Language check
# prompt - If the following text is written in English, suggest a suitable title. Otherwise, respond with: "I only understand English."
# We can even add more conditions in the prompt so that the model knows whoch action to take when a particular condition is satisfied.