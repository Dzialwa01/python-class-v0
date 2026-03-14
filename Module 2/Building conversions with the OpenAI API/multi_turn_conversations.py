# Dzialwa Nemakonde
# 04 March 2026

# Multi-turn conversations with GPT

# 1. What are Multi-Turn Conversations?
# To unlock the real power of chat models, we create multi-turn conversations.
# Multi-turn conversation means: The user and AI talk back and forth and Each mew message remembers previous messages


# 2. Assistant Messages in Conversations
# The model always generates a response to the latest user message, using:
# the system message and all previous user and assistant messages.

# important idea => if we store the assistant's reply and send it again with the next user message, we can continue the conversation


# 3. How a conversation is built (Concept)

# To build a conversation, we follow these steps:
## User sends a message
## Assistant generates a response
## The response is saved
## Both are sent again with the next user message


# 4. Why Conversation History Matters
# The conversation history helps the model to understand context better:
# e.g.
#  User: Hi, my name is Rahul.
# Assistant: Nice to meet you, Rahul!
# User: What is my name?
# Assistant: Your name is Rahul.


# 5. Coding a Multi-Turn Conversation in Python

# Step 1: Define the System message - to set the behavior of the assistant
# messages = [ {"role":"system","content":"You are a helpful Python tutor."}]

# Step 2: Create User Questions
# We will ask multiple related questions.
# user_qs = ["Why is Python popular?","Summarize the above answer in one sentence."]

# Step 3: Loop Through Questions
# We want a response for each question, so we use a loop.
# for question in user_qs

# Step 4: Add User Message to conversation
# Convert the question into a message and store it.
#     user_message = {"role":"user","content": question}
#     messages.append(user_message)

# Step 5: Send Messages to the Model
# The model now sees the full conversation.
#     response = client.chat.completions.create(
#       model="gpt-4.1-mini",
#       messages = messages)

# Step 6: Extract Assistant Response

# Get the assistant's reply and store it.
# assistant_message = {"role":"assistant","content": response.choices[0].message.content}
# messages.append(assistant_message)

# step 7: Print the conversation
# So we can clearly see what's happening.
# print("User:", question) print("Assistant:", assistant_message["content"]) print()


# 6. Result: A real conversation
# The second question: " Summarize the above answer in one sentence" , works without repeating the explanation, because:
# The assistant's previous is stored and the model has full context.
# This proves that mlti-turn conversations are working correctly.


# 7. Key Takeaways (Very Important)
# Multi-turn chat requires:
## storing user messages
## storing assistant replies
## sending the full message list every time

# THe model does not remember anything by itself, We must send conversation history manually


# Summary Table
# | Concept | Meaning |
# | --- | --- |
# | Single-turn | One question, one answer |
# | Multi-turn | Back-and-forth conversation |
# | Messages list | Stores full conversation |
# | Context | Previous messages sent again |

# Final thought => Multi-turn conversations are the foundation of all AI chatbots.
# Once this is mastered, you can build real chat applications

# Practice and exercises done in AI-Application repository