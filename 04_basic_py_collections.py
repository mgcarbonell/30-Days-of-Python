# In python we have lists
names = ["Jerry", "Elaine", "Kramer", "George"]

# and we can spread them over multiple lines, or mix datatypes
friend_details = ["Andy", 33, "big boss"]

# we can access them like standard javascript notation
print(friend_details[0])  # => Andy
print(friend_details[1])  # => 33
print(friend_details[2])  # => big boss

# we can also access them with negatives, that's like a len - 1
print(names[-1])  # => George

# want to add something to the end of the list? .append()
names.append('Newman')
# or we can use the + operator
names = names + ['Helen']
print(names[-1])  # Helen
print(names[-2])  # Newman

# we can also use insert() so if we have...
numbers = [1, 2, 4, 5]
# and we want to insert a 3 at index 2 we would
numbers.insert(2, 3)

# to remove items from a list we can remove
names.remove('Newman')  # removes Newman

# we can also use del
del numbers[0]  # deletes index 0 in numbers (deletes 1)
print(numbers)

# we can also pop() to remove the last item and save it
jerry_mom = names.pop()
print(jerry_mom)

# we can also clear the array with clear
names.clear()
print(names)  # => []

# TUPLES the Devil's Datastructure (just kidding)

# All we need to define a tuple is a series of comma separated values

names = "Jerry", "Elaine", "George"
# most often you'll see names = ("Jerry", "Elaine", "George") with the parens

# We can also store tuples in a list!
movies_example = [
    ("Eternal Sunshine of the Spotless Mind", 2004),
    ("Memento", 2000),
    ("Requiem for a Dream", 2000)
]
# ESSM & 2004 = a tuple
# Like lists, we can access a value in a tuple with list notation.
print(names[0])  # => Jerry
print(movies_example[0])  # => ('Eternal Sunshine of the Spotless Mind', 2004)
# we can even use double notation to return something specific
print(movies_example[0][0])  # => Eternal Sunshine of the Spotless Mind

# However, TUPLES ARE IMMUTABLE. We cannot change once defined!

# Exercises
# 1. Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
movies = [("Hackers", "Iain Softley", 1995, 20000000)]
# 2. Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
user_movie_title = input("What's your favorite movie? ")
user_movie_director = input(f"Who directed {user_movie_title}? ")
user_movie_year = int(input(f"In what year was {user_movie_title} released? "))
user_movie_budget = int(input(f"What was the budget of {user_movie_title}? "))
# 3. Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
user_movie_tuple = (user_movie_title, user_movie_director,
                    user_movie_year, user_movie_budget)
print(user_movie_tuple)

# 4. Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f"{user_movie_tuple[0]} directed by {user_movie_tuple[1]} was released in {user_movie_tuple[2]} with a budget of {user_movie_tuple[3]}.")
# 5. Add the new movie tuple to the movies collection using append.
movies.append(user_movie_tuple)
# 6. Print both movies in the movies collection.
print(movies)
# 7. Remove the first movie from movies. Use any method you like.
movies.pop(0)
print(movies)
