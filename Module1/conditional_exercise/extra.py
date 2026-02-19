#Extra exercises dealing with conditionals

# Extra 1: Odd or Even

num = 17

if num % 2 == 0:
    print("even")
else:
    print("odd") # odd

# Extra 2: Password Strength

password = "Code123"

if len(password) < 4:
    print("too short") # False
elif password.isalpha():
    print("weak") # False as it contains numbers
elif password.isalnum(): # True
    print("medium") # medium
else:
    print("strong")


# Extra 3: Temperature Detector

temp = 32

if temp < 0: # False
    print("freezing")
elif temp < 20: # False
    print("cold")
elif temp < 30: # False
    print("warm")
else:
    print("hot") #hot


# Extra 4: Vowel or Consonant

ch = "e"

if ch.lower() in "aeiou":
    print("vowel") #vowel
else:
    print("consonant")


# Extra 5: Age Group Classifier

age = 14

if age < 13: # False
    print("child")
elif age < 20: # True
    print("teen") # teen
elif age < 60:
    print("adult")
else:
    print("senior")





