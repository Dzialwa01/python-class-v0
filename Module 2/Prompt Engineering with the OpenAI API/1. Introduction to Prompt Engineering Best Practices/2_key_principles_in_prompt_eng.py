# Dzialwa Nemakonde
# 09 March 2026

# Key principles of prompt engineering

## Clear and Precise prompts

# When talking to a Large Language Model, we should always aim for clarity and precision
# Think of giving someone directions:
# Bad directions -> 'Go somewhere near the market'
# Good directions -> 'Go straight for 200 meters, then turn left near the bank"


## Three Key Principles of Prompt Engineering

# 1. Using action verbs
# 2. Giving detailed and precise instructions
# 3. Writing well-structured points using delimiters


## Using Action Verbs

# Always tell the model exactly what to do using action verbs.
# Good Action Verbs: write, explain, describe, summarise, compare, evaluate, list, e.t.c.

# Avoid ambigious verbs as they are unclear and they do not tell the model what output you want.
# e.g., think, understand, feel, try, know, ...

# Example: Bad vs Good Verb Usage

# ineffective prompt: Think about deforestation.
# The problem here is that the model doesn't know whether to explain, list causes or give solutions.

# Improved prompt: Propose three strategies to reduce deforestation.
# Here the model knows the: task -> propose; output -> strategies; quantity -> three


## Formulating Detailed Instructions

# Good prompts include details such as: context, output format, length, style and target audience.

# Example: Tell me about dogs -> too broad
# : Describe the behaviour and characteristics of Golden Retrievers and explain why they are suitable for families. -> detailed prompt
# More detail = more accurate output


## Limiting output length

# Sometimes we want short answers, summaries or limited explanations are thered are two methods to do this.

# 1. Using max_tokens: This enforces a hard limit and may unfortunately cut responses mid-sentence.
# 2. Specify length in Prompt: This is recommended to ensure more natural and usually complete answers.
# e.g., Explain Python in no more than 3 sentences.


## Understanding Prompt Components

# A prompy often has two parts which are theinstruction and the input data.
# The instruction tell the AI what to do and the input data provides content to work on.


## Using Delimiters for Well-structured Prompts

# To avoid confusion, we separate input data using delimiters.
# We use delimiters such as: """""", [], (), ()
# This helps because it tell the model the start and end of the input.


## Using Python f-Strings for prompts

# instead of writing long text inside the prompt, we can store it in a variable.
# Example
text ="Artificial intelligence is transforming industries..."

prompt = f"""
Summarize the following text in one sentence:

```{text}```
"""

# This is perdect for long inputs. It also makes the code cleaner and easier to reuse.


## Final summary
# Use action verbs
# Avoid vague language
# Give clear and detailed instructions.
# Control output length clearly.
# Use delimiters for structured prompts
# Use f-strings for dynamic prompts.