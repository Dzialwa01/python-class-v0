# Dzialwa Nemakonde
# 03 February 2026
# Learning about dictionaries

# Snippet_1 

movie = {
"title":"Fight Club",
"year":1999,
"genre": ["drama","thriller"],
"starring": ["Brad Pitt","Edward Norton"],
} # A dictionary contains keys on the left and values on the right of the colon 

print(movie["year"]) # Dictionaries do not have number indexes. Their indices are the keys 
print(movie["title"])
print(movie["genre"])
print(movie["genre"][0]) # If a value is a list we can just do double square brackets if we want a specific value and not the whole list
print(movie["genre"][1])

print(movie.get("duration")) # if we try to access a key not in the dictionary we get an error, but using the get method, we get the value None
print(movie["starring"][1])
print(len(movie["starring"]))


# Snippet_2

restaurant = {
"name":"Bob's Burgers",
"location":"123 Ocean Avenue",
"owners": ["Bob Belcher","Linda Belcher"],
"established":2011,
"menu": ["burgers","fries","shakes"],
}

print("owners" in restaurant) # we use in to check if a key is in the dictionary which returns a boolean 
print("employees" in restaurant)

some_key ="menu"
print(some_key in restaurant)

print(restaurant["menu"])
print(restaurant.get("menu"))
print(restaurant[some_key])
print(restaurant.get("some_key")) # This outputs none because we are passing some_key as a string and not a variable, and the key some_key is not in the dictionary

print("fries" in restaurant["menu"])


# Snippet_3
dog = {
"name":"Manny",
"age":5,
"breed":"pug",
"color":"fawn",
"favoriteFoods": ["bacon"],
}

print(dog["age"])
print(dog["breed"])
print(dog["favoriteFoods"])

# You can easily modify the values of the dictionary using the methods associated with the type as follows

dog["age"] +=1
dog["breed"] = dog["breed"].upper()
dog["favoriteFoods"].append("sausage")

print(dog["age"])
print(dog["breed"])
print(dog["favoriteFoods"])

for key in dog:
    print(key,"is", dog[key])

# Snippet 4

recipe = {
"name":"Old Fashioned Pancakes",
"difficulty":"easy",
"tasty":True,
"ingredients": ["eggs","milk","butter","flour","sugar"],
}

print(recipe["name"])
print(recipe["name"])
print(len(recipe["ingredients"]))
print(recipe.get("calories"))

some_variable ="difficulty"
print(recipe[some_variable])
print(recipe.get("some_variable"))

for ingredient in recipe["ingredients"]:
    print(ingredient)



