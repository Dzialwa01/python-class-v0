# Dzialwa Nemakonde
# 24 February 2026

# 1. Summarizing and editing text
# In this chapter, we learn how OpenAI chat models can work with exiisting text, not just answer questions.
# These models can: Edit text, Rewrite text, Summarize long content.


# 2. Quick recap
# We have used chat models to answer questions and follow simple instructions
# Now we are going to use them to transform text such as:
## Editing a paragraph
## Shortening long content
## Making text easier to understand.


# 3. Text Editing - Concept
# Text editing means changing parts of rxisting automatically.
# For example, suppose you have a short biography with a lot of things to edit i.e. name, pronouns etc. We can ask AI to edit this for us instead of editing everything manually.

# E.g
# Original text : Alex is a software developer. He works at a startup and loves teaching programming.

# Prompt we send to the model
# Update the following biography:
# - Change the name to Sarah
# - Change pronouns to she/her
# - Change job title to Senior Software Engineer

# """
# Alex is a software developer. He works at a startup and loves teaching programming.
# """

# NB
# We use triple quotes (`"""`)** to clearly separate:
# - Instructions
# - The text to be edited
# - This makes long or multi-line text easy to handle.


# 4. Text  Editing - Result
# AI Output : Sarah is a Senior Software Engineer. She works at a startup and loves teaching programming.

# Why is this powerful?
# There is no need to specify each word replacement as AI understands context. This is also much more flexible that a basic "find and replace" tool


# 5. TEXT SUMMARISATION - Concept
# Text summarisation means turning long text into a short, meaningful summary.

# Real-World Example - Imagine working in a big company that receives thousands of customer support chats every day. Managers do not have time to read full conversations, they need quick summaries.


# 6. TEXT SUMMARISATION - Example  
# Customer chat (stored as a string)
chat = """
Customer: My internet is very slow.
Agent: I’m sorry to hear that. Have you tried restarting the router?
Customer: Yes, but it didn’t help.
Agent: I will escalate this issue to our technical team.
"""
#  

# Prompt using an f-string
prompt = f"Summarize the following customer support chat in 2 sentences:\n{chat}"

# Recap -> An f-string allows us to insert variables directly into strings. It coverts python data into readable text automatically. 

# AI output : The customer reported slow internet issues that were not resolved by restarting the router. The agent escalated the issue to the technical team for further investigation.
# This helps to save hours of reading when dealng with large volumes of chats.


# 7. CONTROLLING RESPONSE LENGTH
# Sometimes the summary can be too short or too long.
# we control this by specifying max_completion_tokens.
# Smaller value -> Shorter response; Larger value -> Longer, more detailed response


# 8. UNDERSTANDING TOKENS
# A token is a piece of text used by the AI. It could be a word, part of a word or even punctuation
# e.g. ChatGPT is powerful might be broken into tokens like: ["chat", "GPT", "is", "powerful"]

# So when we set max_completion_tokens, we are telling the model to not generate more than this many tokens in the response. 


# 9. Calculating the Cost - Basics
# The OpenAI API is paid outside of learning environments.
# The cost depends on the model used, number of input tokens, number of output tokens.
## Pricing is per million tokens; input and output tokens may have different prices. More tokens = more cost

# Cost calculation
# calulating the cost of our summary request wherein our max_completion tokens = 500

# step 1: Find token usage:
# usage:{"prompt_tokens":300,"completion_tokens":200}

# step 2: covert pricing
# if a model costs: $2 per 1,000,000 tokens
# cost per token: 2 / 1,000,000 = $0.000002

# step 3 : Calculate total cost
# Input cost  = 300 × 0.000002
# Output cost = 200 × 0.000002
# Total cost  = $0.001

# Exercises -> Done on the AI application repository