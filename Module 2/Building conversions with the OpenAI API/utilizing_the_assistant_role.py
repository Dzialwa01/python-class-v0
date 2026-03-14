# Dzialwa Nemakonde
# 3 March 2026

# 1. What is the assistant role
# The assistant role represents how the AI responds, the style, tone and format of answers as well as the example answers we want the AI to follow.
# THink of it as: "This is how I want the AI to reply"


# 2. Chat Completions for Single-Turn Tasks
# For single-turn tasks, we usually do NOT send assistant messages.
# THe model generates a response using: its existing knowledge, the system message and the user message.


# 3. WHy Use the Assistant Role? (Providing Examples)
# The main purpose of the assistant role is to give examples.
# This is very useful for: shot prompting, controlling tone (simple, formal, friendly), controlling format (steps, bullets, code + explanation) 
# This is actually a structured way of shot prompting


# 4. Assistant Role with Examples ( Python Tutor Example)
# Let's say we are building a python programming tutor app.
# We can teach the AI how to respond by giving it example conversations.

# Example structure
# System: You are a Python tutor who explains concepts simply.
# User: What is a variable in Python?
# Assistant: A variable is a container used to store data.
# Example:
# x = 10
# Here, x stores the value 10.

# User: What is a loop in Python?

# THe AI now understands: how detailed the answer should be; that examples are required; the teaching style.


# How the Response Works
# The output is accessed the same way as before (message -> content)
# Because we gave an assistant example the AI now replies in a similar tone, similar length and similar structure.

# Key point: You can add one or multiple examples, just experiment what works best. 
# But always remember, more examples => more control ; Too many examples => longer input and cost


# 6. System vs Assistant vs User (NB!!!)

# System Role -> Rules and Guardrails that the AI must follow
# Use this when the output  must follow a strict format and the behaviour must never change.
# e.g. "System : Always answer in simple English and include one example"

# Assistant Role -> Example answers (Best for multi-turn chatbots)
# Use this when you want to show how answers should look; you want consistant style in conversations
# e.g. 
# User: What is a function?
# Assistant: A function is a block of reusable code.
# Example:
# def greet():
#   print("Hello")

# User Role -> Context or Task Specific Examples
# Use this when context is needed to understand the task or when its a one-time task
# Example (Job advertisement)
# User: Here is an old job ad. Create a new one similar to this.
# Common in single-turn tasks


# 7 Summary Table
# | Role | Purpose | When to Use |
# | System | Rules & behavior | Fixed output format, restrictions |
# | Assistant | Example responses | Style, tone, teaching pattern |
# | User | Question or task | Context or instructions |

# Final takeaway => The assistant role is not just for replies, ot os a powerful tool to guide how the AI should respond. 

# Practice and exercises done in AI application repository