# Write a function `funny_sound` that accepts two strings.
# Return a new string made from:
# - the first three characters of the first string
# - the first three characters of the second string
#
# You may assume both strings are at least 3 characters long.

def funny_sound(string1, string2):
    return string1[:3] + string2[:3]

print(funny_sound("tiger", "spoon"))       # "tigspo"
print(funny_sound("computer", "phone"))    # "compho"
print(funny_sound("skate", "bottle"))      # "skabot"
print(funny_sound("frog", "ashtray"))      # "froash"

