# Dzialwa Nemakonde
# 19 May 2026

# Text Analysis - The process of examining written text to find meaningful information. This is done through many techniques of which two are: Text classification as well as Entity extraction.


## Text Classification
# This means assigning a category to a given text.
# E.g., In a sentiment analysis we can get the following categories: Positive, Negative and Neutral. The model can easily analyse which sentiment category a customer review belongs to.

# Classification with Specified categories
# For better results, we can clearly mention the categories in the prompt.
# E.g Analysing the sentiment of a smartwatch review: categories - positive, negative, neutral; output format - one word only
# The model then follows these instructions exactly

# If the categories are not specified, the model uses its own knowledge.
# It is always advised to define categories to get predictable results but the model does well for simple tasks like sentiment analyses.

# Multiple class classification
# it is possible for a text to belong to more than one category.
# The best practice in these situations can be to tell the maximum numbers of classes it can return


## Entity Extraction
# This is another form of text analysis where the goal is to extract specific information such as: names, places, organisations, dates and product details.

# To obtain accurate results in entity extration, we should: clearly mention which entities to extract; specify the output format.
# Eg., From a mobile phone description, ask the model to extract: product name, display size, camera resolution. And format the result as an unordered list.

# Sometimes, entity structures are too complex to explain in words so we can utilise few-shot prompting.
# Example:
# Support tickes from a travel booking app: Each ticket has customer details and reservation details; Some tickets may hsve phone numbers may others may not
# Now suppose we receive a new ticket from a customer named David, we include previous tickets, their extracted entities and the new ticket.
# The model follows the same structure and: extract relevant entities and identifies new sub-entities.