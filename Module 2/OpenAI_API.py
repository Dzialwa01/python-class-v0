# Dzialwa Nemakonde
# 23 February 2026
# All exercises are being completed in the AI Application repository 

# 1.1 Working with OpenAI API (Application Programming interface)

# OpenAI is a company that researches and develops artificial intelligence system. They build powerful AI models which are used by developers i.e ChatGPT

# 1.2 What is ChatGPT?
# THis is a ready-made application which is designed for humans to chat with AI. THis is not the technology itself, it is a product.

# What is OpenAI API?
# The OpenAI API allows developers to interact with powerful language models like (Generative Pre-trained Transformer [GPT]) programmatically instead of using the ChatGPT UI(user interface)
# You can use it to generate text, build chatbots, summarise content, answer questions, automate tasks.

# Step 1: Create an API Key
# Go to platform.openai.com
# login 
# Navigate to API Keys
# Generate a new secret key
# Copy it immediately as you won't see it again
# NB: Never expose your API key in frontend code

# Python Example: Making an OpenAI API Request

# uv add openai 

from openai import OpenAI # Create a client (make sure your OPENAI_API_KEY is set in your environment)
client = OpenAI()# Replace the prompt below with your own question or instruction

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,
  
    # Enter your prompt
    messages=[{"role": "user", "content": "Can you tell me about MERN stack job market"}]
)

print(response.choices[0].message.content)

# What Happening in this code? 
#  OPENAI() creates a connection to the OpenAI API
# model specifies which AI model you want to use
# input is your prompt (question or instruction)
# response.output_text contains the AI's reply. ## This is the same technology behind ChatGPT, but now you control it through code.


# 2 System vs User Messages
 
# Chat models do not take one prompt, they take a conversation, made of different message roles*
# Message Roles:
## system: Sets behaviour, rules, personality (e.g. "Be formal", " Act as a tutor")
## User - What the user says (your messages)
## assistant - Model's response or previous replies
# Chat models uses all of this to generate the next reply

# Analogy: 
# System message -> Teacher's instruction
# User message -> Student's question
# Assistant -> AI's answer

# Simple Text Generation (User Message Only)

response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[
        {"role":"user","content":"What is Python?"}
    ]
)
print(response.choices[0].message.content)

# What's happening 
# messgaes is a conversation
# role = "user" -> student question
# message.content -> AI's final answer


# 4. System vs User Messages (Core Concept)
# system message defines role and teaching style
# User message is the question

response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[
        {
"role":"system",
"content":"You are a programming teacher. Explain concepts simply with examples."
        },
        {
"role":"user",
"content":"Explain JavaScript closures"
        }
    ]
)

print(response.choices[0].message.content)

# 5. Using System Prompts to Guide AI behaviour
# Example: Bullet-Point Answers Only
response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[
        {
"role":"system",
"content":"Answer only in bullet points. Keep it short."
        },
        {
"role":"user",
"content":"Explain OOP concepts"
        }
    ]
)

print(response.choices[0].message.content)

# Example: Code reviewer Bot
response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[
        {
"role":"system",
"content":"You are a code reviewer. Point out mistakes and suggest improvements politely."
        },
        {
"role":"user",
"content":"def add(a,b): return a+b"
        }
    ]
)

print(response.choices[0].message.content)

#Exercise 2
# Write a system prompt that:
# - Acts as a **Python mentor**
# - Explains step-by-step
# - Avoids advanced terms


# 6 Understanding Tokens (With Code) =

# - **Definition**: Tokens are the basic units of text that language models like LLMs (Large Language Models) process. They can be words, parts of words, or even punctuation.

# - **Tokenization**: The process of breaking down text into tokens. For example, the sentence "I love programming!" may be tokenized into ["I", "love", "program", "ming", "!"].

# - **Vocabulary**: LLMs have a predefined vocabulary, which is a collection of all possible tokens they can recognize. This can range from thousands to millions of tokens.

# - **Input Representation**: Each token is translated into numerical values (embeddings) for the model to understand and process.

# - **Importance**: The way text is tokenized can significantly affect the model's performance and its ability to understand context or capture nuances in language.

# - **Subword Tokens**: Many LLMs use subword tokenization (like Byte Pair Encoding) to handle unknown words by dividing them into smaller, known parts, which helps in reducing vocabulary size.

# - **Efficiency**: Using tokens allows models to process text more efficiently, as they can handle large amounts of data without needing to understand every single character or word.

# - **Examples**: Common LLMs like GPT, BERT, and T5 use different tokenization methods, impacting how they interpret and generate language.

# 7. Mini project ( Perfect for Assignment)

# Building a Teaching Bot
while True:
    user_input=input("\nAsk a question (or type 'exit'): ")

    if user_input.lower()=="exit":
        break

    response=client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
                {
    "role":"system",
    "content":"You are a helpful programming teacher. Explain simply with examples."
                },
                {
    "role":"user",
    "content":user_input
                }
            ]
        )

print("\nAnswer:")
print(response.choices[0].message.content)


# Key takeaways
# Chat models use structured messages
# System messages conrol behaviour
# User messages ask questions
# Tokens affect cost and limits
# APIs enablle real applications, not just chat.
