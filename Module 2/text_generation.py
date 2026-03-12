# Dzialwa Nemakonde
# 25 February 2026

# Objective: To help you understand how to generate and refine text with AI, which is a valuable skill for creating content and automating communication tasks.
# You're building a foundation to make AI-generated text more relevant and useful for your goals

# 1. Text Generation
# In this lesson, the aim is to study text generation; how AI models generate text and this is used in real-world applications like chatbots, marketing, and product descriptions.


# 2. How Does a Model Generate Text?
# When we send a prompt to a chat model, the model tries to predict the most likely next words based on what it has learned from training data.
# For example, if we give the prompt: "Life is like a box of chocolates" , the model is very likely to complete it correctly because it has seen similar text many times during training.
# However, the output is not always guaranteed to be the same because AI models are non-deterministic, meaning they use probability to decide the next word. So even with the same prompt, the response can change slightly.

# 3. Controlling Randomness in Responses
# In many situations, randomness is not a good thing i.e., In a customer support bot, we do not want different answers for the same question. But at the same time, we want the model to understand different user inputs.
# This is where the temperature parameter comes in:
## Temperature = 0 -> very predictable answer which is almost the same answer every time.
## Temperature = 1 -> balanced (default)
## Temperature = 2 -> very creative and random

# If we increase the temperature, the response may become more unusual or creative, sometimes even strange. So there is always a tradeoff between consistency and creativity.


# 4. Text Generation for Marketing
# Text generation is not just for answering questions, it can also create new content. 
# For example, let's generate a tagline for an electric car. If our prompt is clear and detailed, the model can produce a strong marketing line.
# We can also experiment by changing: 
## temperature (for creativity)
## max_completion_tokens (for response length)


# 5 Text Generation for product description
# Another common use case is writing product descriptions
# i.e. Let's say we want a description for a smartwatch designed for fitness enthusiasts or business professionals
# We start the prommpt by listing key features and then clearly mention the tone (professional, energetic, friendly) and the target audience, which helps to produce better output

# 6. Improving and Refining Output.
# The result we get is often good enough to use directly on an e-commerce website.
# If we want to improve it further: we update the orginal prompt, add more details and generatr again. 

# Exercise: Done in AI Application

### **Content generation**

# AI is playing a much greater role in content generation, from creating marketing content such as blog post titles to creating outreach email templates for sales teams.

# In this exercise, you'll harness AI to generate a catchy slogan for a new restaurant. Feel free to test out different prompts, such as varying the type of cuisine (Italian, Chinese, etc.) or the type of restaurant (fine-dining, fast-food, etc.), to see how the response changes.
# Create a request to create a slogan for a new restaurant; set the maximum number of tokens to 100

## **Generating a product description**

# Imagine you're writing marketing copy for **SonicPro** headphones. Your goal is to generate a **persuasive product description** using the OpenAI API.

# Test how different **prompting techniques**, **response lengths**, and **temperature settings** influence the output!

# ### Intruction

# - Create a **detailed prompt** to generate a product description for SonicPro headphones, including:
#     - Active noise cancellation (ANC)
#     - 40-hour battery life
#     - Foldable design
# - Experiment with `max_completion_tokens` and `temperature` settings to see how they affect the output.

