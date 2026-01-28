# Dzialwa Nemakonde
# 28 January 2026

# Learning about nesting

# Snippet 1

# Predict what this will print:
for i in range(1, 5):
    for j in range(1, 4):
        print(i, j)

# 1,1 ; 1,2; 1,3; ... ; 4,1 ; 4,2, 4,3 

# Snippet 2

for n in range(2):
    print("n=" + str(n))
    for m in range(5):
        print("   m=" + str(m))
    print("n=" + str(n))

# n=0 
# m=1
# m=2
# m=3
# m=4
# n=0
# n=1
#...
#n=1

#snippet 3

friends = ["philip", "abby", "phelipe", "simcha"]

for i in range(len(friends)):
    for j in range(len(friends)):
        print(friends[i], friends[j])

#phillip phillip
#phillip abby
#abby phillip
#....
#simcha simcha

# snippet 4

locations = ["flatbush", "williamsburg", "bushwick", "greenpoint"]

for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        print(locations[i], locations[j])

#flatbush williamsburg ... 
#flatbush greenpoint
#williamsburg, bushwick 
#williamsburg greenpoint
#bushwick greenpoint

# snippet 5

colors = ["red", "purple", "orange"]

for color_str in colors:
    print(color_str)
    for char in color_str:
        print(char)

#red
#r
#e
#d
#...