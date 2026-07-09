# Dzialwa Nemakonde
# 03 June 2026

# Exploring question answering models and learn how to have conversations with documents. 

## What is document Question Answering

# This is an NLP task where a model answers questions based on the content of a document
# The model reads the document, understands context, and finds the most relevant answer.

# Use Cases for Document Q & A
# Document Q & A is widely used across industries to automate information retrieval. Such as:
# Legal - To identify clauses in contracts; TO extract termination conditions or deadlines.
# Finance - to retrieve revenue, expenses, and KPIs from reports; Analyse financial statements quickly
# Customer Support - Answer FAQs from user manuals; reduce support ticket volume.


## Extracting Text from PDF using pypdf

# As models cannot read PDDFs directly, we first extract text using the lightweight Python library pypdf.

# Steps: load the pdf -> Access all pages -> Extract text from each page -> Combine everything into a single string

# Code example:
from pypdf import PdfReader

reader=PdfReader("US-Employee_Policy.pdf")

document_text=""
for page in reader.pages:
document_text += page.extract_text()


## Creating a Question-Answering Pipeline

# We choose: Task - question-answering; Model: distilbert-base-uncased-distilled-squad

# Code Example:
from transformers import pipeline

# Create Question Answering pipeline
qa_pipeline = pipeline(
    task="question-answering",
    model="distilbert-base-uncased-distilled-squad"
)

# Sample document
document_text = """
Employees are encouraged to participate in community service activities.
Each employee is allowed 1 volunteer day per year to support charitable
organizations and local community programs.
"""

# Question
question = "How many volunteer days are allowed per year?"

# Get answer
result = qa_pipeline(
    question=question,
    context=document_text
)

print("Answer:", result["answer"])
print("Confidence Score:", round(result["score"], 2))
print("Start Position:", result["start"])
print("End Position:", result["end"])
print("\nFull Output:")
print(result)

# Output example:
Answer: 1
Confidence Score: 0.92
Start Position: 95
End Position: 96

{
    'answer': '1',
    'score': 0.92,
    'start': 95,
    'end': 96
}