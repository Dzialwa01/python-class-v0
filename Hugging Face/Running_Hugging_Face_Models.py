# Dzialwa Nemakonde
# 28 May 2026

# Runnning Hugging Face Models

## What is inference

# Inference ,means using a trained AI model to make predictions on new data.
# When running Hugging Face models, we have two options which are Local Inference or Inference using providers (API)


## Local Inference
# This is running a model on your laptop or inside a cloud dev environment
# Advantages is that it is free, there's no API required and you have Full control over the model.
# Limitations are that on large models it is slow, uses High RAM and CPU and large models need GPU which laptop do not have

## Inference Providers (API-Based Inference)
# These are partner companies the host powerful machines (GPUs/TPUs) and run models for us remotely.
# We easily send the input and model name, and receive the output, All done through the Hugging Face APIs
# We use them because they are much faster, No hardware stress, can run large LLMs, image and video models and there's also Free credits to get started.


## Introduction to the Transformers Library

# To run models locally, we use transformers
# Transformers provide easy access o thousands of pre-trained models, uses the same API for NLP, vision and auduio, and they also work for inference and training.

# The pipeline() - Fastest Way to Run a Model.
# A pipeline is a high-level wrapper that: loads the model, handles tokemisation, runs inference and returns readable output

# Basic Example: Text Generation

from transformers import pipeline

generator = pipeline(
    task = "text-generation", # This tells what we want
    model = "openai-community/gpt2" # The model name from the hub
)

result = generator("What if AI") #Input text
print (result[0]["generated_text"]) # Dictionary with generated_text


## Adjusting Pipeline parameters

# We can control the output using parameters.
# Example: Limit Tokens and Generate multiple Outputs

results = generator(
    "What if AI",
    man_new_tokens = 10, # Limits the length of the output
    num_return_sequences = 2 # To enable multiple responses
)

for res in results:
    print(res["generated_text"])

# Theres temperature for creativity as well as randomness control with top_k and top_p
# The output of this becomes a list of dictionaries


## Using Hugging Face Inference providers

# Running models without using our own hardware
# Steps:
# - Create an inference client
# - Choose an inference provider
# - Add Hugging Face API key
# - Send input as messages

# An example of a provider is Together.ai

