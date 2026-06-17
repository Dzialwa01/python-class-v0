# Dzialwa Nemakonde
# 21 May 2026 

## What is Prompt Engineering for Chatbots?
# Prompt engineering is the process of designing instructions (prompts) that guide a chatbot to behave and respond in the way we want .
# In chatbot development, prompts decide: who the chatbot is, what it knows and how it responds to users.


## Why do Chatbots Need Prompt Engineering?
# As chatbots interact with many unpredictable users, we cannot predict every question a user will ask.
# So we use prompt engineering to guide the chatbot behaviour so that its focused on its domain, gives consistent responses and it improves accuracy and reliability.


## Chatbot Prompt Engineering Using the OpenAI API
# For chatbot development, system messages are the most important.
# THis is because system messages control how the chatbot behaves; define its role, tone, and limitations and they apply to every user interaction.
# As a result our get_response() function will have to contain a entry for the system prompt

# The first important task of the system message is to define the chatbot's purpose, as having a clear purpose makes the chatbot to provide accurate answers.
# System messages should also define how the chatbot should respond by specifying things like the target audience, tone(formal, friendly, neutral), answer length and output structure

# The system message can also limit what the chatbot can answer. e.g. "Answer finance-related questions only. For other topics, reply: 'Sorry, I only know about finance.'"