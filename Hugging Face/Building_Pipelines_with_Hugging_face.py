# Dzialwa Nemakonde

## What is Text Classification

# This is the task of assigning predefined categories or labels to a piece of text

# The common use cases include: sentiment analysis, spam detection, topic classification, grammar checking, and question answering systems.


## Sentiment Analysis: Coding Example
# Hugging Face makes text claasification easy using pipelines from Face Transformers library

from transformers import pipeline

classifier=pipeline(
task="text-classification",
model="distilbert-base-uncased-finetuned-sst-2-english"
)

result = classifier("I hate waiting in long queues")
print(result)

# Output example
[{'label': 'NEGATIVE', 'score': 0.99}]
# The model predicts Negative sentiment, the confidence score shows how sure the model is.


## Text Classification: Grammatical Correctness

# This classification determines whether a sentence is grammatical correct or not
# Commonly used in grammar checkers, writing assistants and language learning tools.

# e.g., Coding example
from transformers import pipeline

grammar_checker=pipeline(
task="text-classification",
model="textattack/bert-base-uncased-CoLA"
)

result=grammar_checker("He eat pizza every day")
print(result)

# example output
[{'label': 'LABEL_0', 'score': 0.99}]
# LABEL_0 -> Grammatically incorrect


## Text Classification : QNLI

# QNLI, Question Natural Language Inference, checks whether a given sentence premise answers a question.
# This task is crucial for: Question-answering systems, fact checking and information verification.

# example code
from transformers import pipeline

qnli_classifier=pipeline(
task="text-classification",
model="textattack/bert-base-uncased-QNLI"
)

result=qnli_classifier(
"Where is Seattle located?, Seattle is in Washington state."
)

print(result)

# output example
[{'label': 'LABEL_0', 'score': 0.98}]
# LABEL_0 -> Entailment (True)
# The premise answers the question correctly


## Text Classification: Dynamic Category assignment

# Sometimes, categories are not fixed during training and this is where dynamic category assignment comes in.
# This approach is widely used in: customer support systems, Email routing, Content moderation and recommendation systems.

# Zero-Shot Classification
# Zero-shot means the model has not been trained on any specific labels but still understands and assigns them using language knowledge

# Coding example:
from transformers import pipeline

zero_shot=pipeline(
task="zero-shot-classification",
model="facebook/bart-large-mnli"
)

result=zero_shot(
"Hey, we would like to feature your courses in our newsletter!",
candidate_labels=["Marketing","Sales","Support"]
)

print(result["labels"][0],result["scores"][0])

# Output example
# Support 0.63


## Challenges of Text Classification

# Ambiguity - Same text can have multiple
# Sarcasm and Irony - "Great, another bug in production" -> Sounds positive but is actually negative
# Multilingual complexity - different grammar rules, cultural context or language-specific expressions
