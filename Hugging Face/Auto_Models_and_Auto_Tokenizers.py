# Dzialwa Nemakonde
# 02 June 2026

# Here we learn how to gain full control over models and tokenization

## What are Auto Classes?

# When we need more control, pipelines become limiting. This is where Auto classes come in.
# Auto classes automatically load the correct model architecture, load the correct tokenizer and match them properly.


## Auto Models
# Auto models simplify model loading without hardcoding architectures.
# Loading a model:
from transformers import AutoModelForSequenceClassification

model=AutoModelForSequenceClassification.from_pretrained(
"distilbert-base-uncased-finetuned-sst-2-english"
)
# Internally what happens is the correct model class is selected, pretrained weights are downloaded then the model is ready for inference or fine-tuning.

# AutoTokenizers
# Models do not understand raw text. The understand numbers(tokens) hence tokenizers are needed.
# An important rule is that the tokenizer used must pair with the model. This is done automatically with pipelines but it is manual with auto classes.
# Loading the tokenizer
from transformers import AutoTokenizer

tokenizer=AutoTokenizer.from_pretrained(
"distilbert-base-uncased-finetuned-sst-2-english"
)
# Upholding the rule ensures same preprocessing, same vocabulary and same token rules used during training.


## Tokenizer Text with AutoTokenizer

# Tokenizers do the following:- cleans text (lowercase, accents, punctuation) 
# - Splits text into token
# - Maps tokens to IDs
# e.g:
tokens = tokenizer.tokenize("I love learning AI!")
print(tokens)
# Example output
['i', 'love', 'learning', 'ai', '!']

# Not all models tokenize the same way, which is why it is dangerous to mix tokenizers and models
# BERT -> word-piece tokens
# GPT -> byte-pair encoding
# SentencePiece -> subword units
# So the same sentence can produce different tokens depending on the model.


## Building a Custom Pipeline with Auto Classes

from transformers import(
    AutoTokenizer,
    AutoModelForSequenceClassification,
    pipeline
)

model_name = "distilbert-base-uncased-finetuned-sst-2-english"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

custom_pipeline=pipeline(
task="text-classification",
model=model,
tokenizer=tokenizer
)

custom_pipeline("This course is absolutely amazing!")

# This yields the same results as a normal pipeline with every step being able to customize every step.


## Use Cases for AutoModels and AutoTokenizers

# We prefer Auto classes when tasks require advanced customization such as:
# - Advanced Text Preprocessing (Custom cleaning rules and Domain-specific normalization)
# - Custom Thresholding (Adjust confidence cutoffs; Prefer certain labels "e.g., route more queries o Support") - Basically custom threshold is setting confidence limits and business rules to control how predictions are assigned.
# - Complex NLP Pipelines: Multi-step workflows, combine classification, summarization, and embeddings and integrate wirth databases or APIs.