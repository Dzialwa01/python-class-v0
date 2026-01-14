# Write a function `ends_with_t` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# ends with the character "t".

def ends_with_t(string):
    return string[-1] == "t"

print(ends_with_t("smart"))      # True
print(ends_with_t("racket"))     # True
print(ends_with_t("taco"))       # False
print(ends_with_t("boomerang"))  # False

