# Dzialwa Nemakonde
# 01 June 2026

## What is Text Summarization
# Text summarisation is the process of reducing a long piece of tect into a shorter summary, while retaining the key ideas and essential information.


## Extractive vs Abstractive Summarisation
# These are the two main types of summarisation

# Extractive -> Selects important sentences from the original text without genrating new words. It is faster and more resource-efficient as well as very factual and safe. However, it may feel less natural and the summary can feel fragmented
# Mostly used in: - Legal document analysis (Higlighting key clauses and no risk of changing meaning)
# - Financial research (Extracting important findings and ensuring no new facts are introduced)

# Abstractive -> It generates new sentences to rephrase content for clarity and produces more human-like summaries. However, it requires more computation and it may introduce hallucinations.
# Mostly used in: - News Article Summaries
# - Content Recommendations (Generating descriptions users want to read)

# Extractive summarizatiom coding example
from transformers import pipeline

summarizer=pipeline(
task="summarization",
model="facebook/bart-large-cnn"
)

text="""
Data science is an interdisciplinary field that uses scientific methods,
processes, algorithms, and systems to extract knowledge and insights from data.
It combines statistics, computer science, and domain expertise.
"""

result=summarizer(text)
print(result)
# Output Example
[{'summary_text': 'Data science uses scientific methods and algorithms to extract insights by combining statistics, computer science, and domain expertise.'}]

# Abstractive summarizatiom coding example

from transformers import pipeline

summarizer=pipeline(
task="summarization",
model="sshleifer/distilbart-cnn-12-6"
)

result=summarizer(text)
print(result)
# Output Example
[{'summary_text': 'Data science combines statistics and computing to extract valuable insights from data.'}]
# The main difference is in the choice of the model


## Parameters for summarisation

# We can control the length and quality of summaries using parameters
# - min_new_tokens -> minimum summary length
# - max_new_tokens -> maximum summary length

# Key challenges in summarisation
# - Long documents may exceed model limits
# - Abstractive models may hallucinate
# - Domain-specific language needs fine-tuning

# Solution strategies
# - Chunk long texts
# - Choose extractive models for safety
# - Fine-tune on domain data