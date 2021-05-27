# DICTIONARIES
# Officially a dictionary is python's version of an associated array, we also know this as an object. The other lists we've working with - lists, strings, and tuples are all sequence types.

# SEQUENCE is a technical term in Python: it refers to a collection which satisfies the sequence protocol. From something to be a sequence, it must have ordered indices which start from 0 and increment by steps of 1 and must also be possible to find the length of the collection with `len`.

# An ASSOCIATIVE ARRAY values are instead associated with some other term, not their index. If we change the order of the values it doesn't matter because we don't need to reindex everything. The 'associate term' we're talking about are KEYS. KEYS have VALUES and make up KEY: VALUE pairs.

# A key is sort of like a variable, however unlike variables keys are values themselves. "In a single dictionary, each key must be unique, but different dictionaries can have the same key as each other."

# A dictionary can have many keys, but each key must be unique, and each key must have a SINGLE value. However, this value CAN BE another collection INCLUDING ANOTHER dictionary.

# Let's make some dictionaries!

# student = {"name": "John Smith"}
student = {
    "name": "John Smith",
    "grades": [88, 76, 92, 85, 89]
}
print(student)
# We have keys of name and grades, and the values are a string and list.
# What can be used as ditionary key names? We can use strings, numbers, and even tuples. What can we not use? Lists. Why not? Because lists can CHANGE.
# Dictionary keys must be unique. Moreover, we cannot use a tuple that can contain a list because lists can be modified to become identical.

# How do we access them? Here's a few ways:
print(student["grades"])  # => [88, 76, 92, 85, 89]
# What about if we're not sure if the key exists?  We can us ethe get method.
print(student.get("grade"))  # => None
# We can even tell specify a default value by passing a second value to get.
print(student.get("grade", []))  # => []

# How do we add? Sort of the same way.
student["age"] = 17  # adds {"age": 17} to the dictionary.
print(student)
# => {'name': 'John Smith', 'grades': [88, 76, 92, 85, 89], 'age': 17}

# We can also use the update method.
movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019
}

meta_info = {
    "runtime": 181,
    "budget": "$356 million",
    "earnings": "$2.798 billion",
    "producer": "Kevin Feige"
}

# let's say we want to add the meta info to our movie dictionary
movie.update(meta_info)
# we've combined them!
print(movie)
# we could have also passed it in like this:
# movie.update({
# 	"runtime": 181,
# 	"budget": "$356 million",
# 	"earnings": "$2.798 billion",
# 	"producer": "Kevin Feige"
# })

# So how do we modify it? Let's take a look at our student again:
student["age"] = 18  # happy birthday John Smith, age is now 18

# And deleting?
# We can use del to delete a specific key, which will remove the key:value
del movie["runtime"]
# We can also pop and pass a key, which will return the removed value.
# We finally have the clear method, which will completely empty a dictionary.

# What about iterating?
# we can grab keys as so
for attribute in movie:
    print(attribute)
# => title, director, year
# and we can grab the values as so
for key in movie:
    print(movie[key])
# but this is a little unecessary because we can just...
for value in movie.values():
    print(value)
# nicer looking imo
# Okay but now I want both! I want the key and value!
for key in movie:
    print(f"{key}: {movie[key]}")
# or we can use the items method as well! Which is going to give us a series of tuples.
for key, value in movie.items():
    print(f"{key}: {value}")
# which is a little more clearer imo


# EXERCISES!!

# 1) Below is a tuple describing an album:

pink_floyd = (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
)
# Inside the tuple we have the album name, the artist (in this case, the band), the year of release, and then another tuple containing the track list.

# Convert this outer tuple to a dictionary with four keys.
album = {}
album["title"] = pink_floyd[0]
album["artist"] = pink_floyd[1]
album["release"] = pink_floyd[2]
album["tracks"] = pink_floyd[3]
print(album)

# 2) Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, you should print the name of the key, and then the value alongside it.
for key, value in album.items():
    print(f"{key}: {value}")

# 3) Delete the track list and year of release from the dictionary you created. Once you've done this, add a new key to the dictionary to store the date of release. The date of release for The Dark Side of the Moon was March 1st, 1973.
del album["tracks"]
del album["release"]
album.update({
    'release': 'March 1st, 1973'
})
print(album)
# If you use a different album for the exercises, update the date accordingly.

# 4) Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError. Once you've tried this, repeat the step using the get method to prevent the exception being raised.
# print(album["tracks"])
print(album.get("tracks"))
