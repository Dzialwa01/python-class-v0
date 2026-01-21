# Dzialwa Nemakonde
# 21 January 2026

# Write a function `censor_e(text)` that returns a new string where all 'e' characters
# are replaced with '*'.

def censor_e(text):

    word = ""

    for i in text:
        if i.lower() == 'e': # Ensuring that all Es (lowecase or uppercase are replaced)
            word += "*"
        else:
            word += i

    print(word)                

# Example:
censor_e("speedy")  #-> 'sp**dy'
censor_e("pending") #-> 'p*nding'
censor_e("scene")   #-> 'sc*n*'
censor_e("heat")    #-> 'h*at'