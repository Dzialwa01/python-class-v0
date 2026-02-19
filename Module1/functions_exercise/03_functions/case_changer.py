# Write a function `case_change(text, make_upper)`:
#If `make_upper` is **True**, return the string in **uppercase**
# If False, return it in **lowercase**

def case_change(text, make_upper):
    
    if make_upper:
        return text.upper()
    else:
        return text.lower()

# Example cases

print(case_change("Super", True))      # SUPER
print(case_change("Super", False))     # super
print(case_change("tAmBourine", True)) # TAMBOURINE
print(case_change("tAmBourine", False))# tambourine

