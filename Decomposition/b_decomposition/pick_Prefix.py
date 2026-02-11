# Dzialwa Nemakonde
# 11 February 2026

# Write a function `pick_prefix(strings, prefix)` that accepts:
# - a list of strings
# - a prefix string
# The function should return a list of words that begin with the prefix.

def pick_prefix(strings, prefix):

    ans_list = []

    for word in strings:
        if word[0:len(prefix)] == prefix: # to compare if the start of the work matches the prefix
            ans_list.append(word)

    return ans_list        

print(pick_prefix(['connect','company','concert','cram'],'con'))
# ['connect', 'concert']

print(pick_prefix(['miner','mistake','misspeak','moose','mission'],'mis'))
# ['mistake', 'misspeak', 'mission']