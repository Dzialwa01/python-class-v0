# Dzialwa Nemakonde
# 28 May 2026


## What are Hugging Face Datasets

# The hugging face Hub provides a large collection of community-curated datasets covering:
# - Natural Language Processing (NLP)
# - Computer Vision
# - Audio and Speech 
# - Multimodal tasks

# These datasets are hosted under the Datasets sections of the Hub:
# Just like models, datasets come with: Metadata, Documentation, Licenses and Preview tools

# The dataset search experience is very similar to models and we can filter datasets by:
# Modality (Text,Image,Audio,etc.)
# Task (Text Generation. Translation, Classification,etc.)
# Language 
# Size
# License
# And this helps us quickly find the most suitable dataset for our task.

# Example: Italian Text Generation Dataset
# - We want to fine-tune a text generation model to improve italian language output. 
# We perform a step-by-step filtering wherein we go to Datasets -> select text modality -> choose the Text Generation task -> then add keyword search: italian


## Installing the Datasets Library

# Hugging Face provides a dedicated Python package called datasets installed in the following way:
# pip install datasets
# this library allows us to: download datasets, load large datasets efficiently, process data with minimal code and share datasets easily.

# Downloading a Dataset in Python
# e.g from datasets import load_dataset
# dataset = load_dataset("dataset_name")
# you can also add a split by adding a second parameter in the load_dataset function. (split = 'train')
# the common splits are: train - for training a model; test - for evaluating the training; validation - for tuning and monitoring the performance of the model


## Data manipulation: Filtering Rows

# To filter rows, we use the .filter() method
# e.g., Finding rows containing "bella"
# filtered_dataset = dataset.filter(lambda rown: "bella" in row["text"])


## Data manipulation: Selecting Rows

# To select rows by index, we use .select() method.
# e.g selecting first two rows
# small_dataset = dataset.select(range(2))