# predict -> type -> run workflow

# Snippet 2.1

nonsense = "blog trust fund tattooed williamsburg poke roof party"
has_ok = "ok" in nonsense

if has_ok: #True
    print("yeet") # yeet
elif len(nonsense) > 10: # this is still satified how ever as the first statement has been executed, the rest the elif and else are ignored
    print("yo")
else:
    print("no")

has_zoo = "zoo" in nonsense
has_fun = "fun" in nonsense

if has_zoo and has_ok: # False 
    print("cool")
elif has_ok:
    print("rad") # rad
elif has_fun:
    print("dope") # not executed for same reason as above
else:
    print("nope")


#Snippet 2.2

q = 25
if q % 3 == 0 and q % 5 == 0: # False
    print("both")
elif q % 3 == 0 or q % 5 == 0: # True
    print("either") # either
else:
    print("neither")

r = 9
if r % 3 == 0 and r % 5 == 0: # False
    print("both")
elif r % 3 == 0 or r % 5 == 0: # True
    print("either") # either
else:
    print("neither")

s = 15
if s % 3 == 0 and s % 5 == 0: # True
    print("both") # both
elif s % 3 == 0 or s % 5 == 0:
    print("either")
else:
    print("neither")

