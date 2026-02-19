# Dzialwa Nemakonde
# 21 January 2026

# Write a function `remove_capitals(text)` that returns a new string with all
# capital letters removed.

def remove_capitals(text):

    word = ""
    for ch in text:
        if ch.lower() == ch: # Ensuring that only lowercase numbers are added 
             word += ch

    print(word)         

# Example:
remove_capitals("fOrEver")     #-> 'frver'
remove_capitals("raiNCoat")    #-> 'raioat'
remove_capitals("cElLAr Door") #-> 'clr oor'