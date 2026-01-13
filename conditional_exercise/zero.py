# Predicting what each snippet will output

# Snippet 01

if True:
    print("foo")

if False:
    print("bar")

# ans : foo


# Snippet 02

if False or False:
    print("boop")

if True or False:
    print("beep")

# ans : beep


# Snippet 03
num = 40

if num > 0:
    print("zip")

if num % 2 == 0:
    print("zoop")

# ans: zip , zoop


# Snippet 04

word = "jeep"

if word[0] == "d":
    print("yer")
else:
    print("nah")

# ans: nah


# Snippet 05

sentence = "roger that"

if sentence[-1] == "t":
    print("ends in t")
else:
    print("does not end in t")

if len(sentence) <= 4:
    print("short")
else:
    print("long")

#ans: ends in t
#   : long