# Dzialwa Nemakonde
# 26 May 2026

# Incorporating External Context

## What is external context?
# This is extra information provided to a chatbot, which the model does not already know from its training. This information helps the chatbot to give accurate, relevant and useful answers to users.


## Why do chatbots need external context?
# Using the OpenAI API means we are using a pre-trained language model (LLM)
# LLMs only know information from their training data and also know information up to a specific cut-off date.
# In real applications, chatbots need: company-specific data, recent updates and private or internal information.


## How Do we provide Extra Information to a chatbot?
# We explicitly give context to the chatbot using two common ways:
# - Sample conversations
# - System prompt with embedded context.

# In this case, system prompts are better because of centralised information, it is easy to update, there's no need for many example conversations and it works well with purpose and behaviour rules.

# However, LLMs have limitations as they can only handle a limited amount of information.

# ## 🔑 Key Takeaways

# - LLMs do not know everything
# - Missing information is due to:
#     - Knowledge cut-off
#     - Private or non-public data
# - External context improves chatbot accuracy
# - System prompts are the best way to inject context
# - Context size is limited and must be managed carefully