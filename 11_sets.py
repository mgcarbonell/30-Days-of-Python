# Sets are a little different than collections. They are not reliably ordered.
# If we define a tuple and print it we know that the items will show up in
# the order we defined them. This isn't so for sets. Sets can only contain
# unique elements like keys.

# Why do we care about sets? They are useful operations for comparing members
# of collections. They're useful for filtering values, and also extremely
# efficient to perform these kinds of membership tests for sets.

# let's define a set:
vegetables = {"carrot", "lettuce", "broccoli", "onion", "carrot"}
# So it looks like like a dictionary, right? It sort of is, but different.
# but notice something here, if we print it we'll only receive carrot once.
# So the above set is identical to this set:
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
# What if we want to describe an empty set? We can't just use {} that will
# create a dictionary for us.
set()
# It's a hash map!

# Can we nest sets?
# nested_sets = {{1, 2, 3}, {'a', 'b', 'c'}}
# Uh oh, type error unhashable type: set Nope we can't.

# can we modify sets? Well we can ADD!
vegetables.add("potato")
print(vegetables)
# Can we add multiple items at once? UPDATE!
vegetables.update(["eggplant", "pumpkin"])
print(vegetables)
# And deleting items from sets? We use REMOVE
vegetables.remove("lettuce")
print(vegetables)
# If we try to .remove() something that doesn't exist we'll get a KeyError.
# So what if we're not sure an item exists in the set? We can use DISCARD.
# Discard works exactly like remove, but it will only try to remove an item IF
# it exists.
# We can also pop() from sets, once again it will give us the removed item
random_vegetable = vegetables.pop()
print(random_vegetable)

# What else can we do?

# UNIONS
# There is a union method with sets.
letters = {'a', 'b', 'c'}
numbers = {1, 2, 3}
letters_and_numbers = letters.union(numbers)
print(letters_and_numbers)
# While union is similar to update, update modifies an existing set, union
# creates a new one.

# INTERSECTION
# When we find the intersection of two sets, we get a new set containing the
# elements common to both sets.
mod_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
mod_3 = {3, 6, 9, 12, 15, 18}

mod_6 = mod_2.intersection(mod_3)

print(mod_6)  # {18, 12, 6}

# DIFFERENCE
# Be careful when using difference because the order of the sets matter!
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}
# If we call difference on bundle_1 and pass it bundle_2 we get a different
# order than if we call difference on bundle_2 and pass it bundle_1
print(bundle_1.difference(bundle_2))  # {'Final Fantasy VII', 'Cyberpunk 2077'}
print(bundle_2.difference(bundle_1))  # {'Halo Infinite', 'Doom Eternal'}
# What difference gives us, is every item in the set we called the method on,
# except those that also feature in this second set.
# When we write
bundle_1.difference(bundle_2)
# We get FFVII and C2077 but not RE3 because RE3 is in both sets. So what's
# different about bundle 1 compared to bundle 2 is it includes FFVII and C2077.

# SYMMETRIC DIFFERENCE
# symmetric_difference gives us all of the items which only features in one of the sets. Unlike difference the order of the sets doesn't matter.
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}

print(bundle_1.symmetric_difference(bundle_2))
# {'Halo Infinite', 'Cyberpunk 2077', 'Final Fantasy VII', 'Doom Eternal'}
# Notice that once more RE3 doesn't appear because it is in both sets.

# Can we do set operations with other collections? We can only call the set operator methods on sets, but we can actually pass in any collection we like into the method. For example:
# letters = {"a", "b", "c"}
# numbers = [1, 2, 3]

# letters_and_numbers = letters.union(numbers)

# print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}

# Checking if items are in collections:
# What if we want to check if a value is in collection? We can use the in keyword which will yield True if the item is found.
numbers = {1, 2, 3, 4, 5}
print(3 in numbers)  # True
print(7 in numbers)  # False
# we can also use it with strings and other collections
print("j" in "Python")  # False
print("n" in "Python")  # True
# We can use in for dictionaries too!
student = {
    "name": "Eric Cartman",
    "age": 10,
    "school": "South Park Elementary"
}

print("grades" in student)  # False
print("school" in student)  # True
# or among its values.
print(10 in student.values())  # True


# EXERCISES!
# 1) Create an empty set and assign it to a variable.
new_set = set()

# 2) Add three items to your empty set using either several add calls, or a single call to update.
new_set.add(2)
new_set.add(4)
new_set.add(6)
new_set.update({
    8,
    10,
    12
})
print(new_set)
# 3) Create a second set which includes at least one common element with the first set.
diff_set = {3, 6, 9, 12}

# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
union = new_set.union(diff_set)
print(union)
sym_diff = new_set.symmetric_difference(diff_set)
print(sym_diff)
intersect = new_set.intersection(diff_set)
print(intersect)

# 5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.
num = range(16, 24)
guess = int(input("Enter a number: "))
if guess in num:
    print("Your number is within the range!")
else:
    if guess < num[0]:
        print("Too low!")
    else:
        print("Too high!")

# If you want an extra challenge, also tell the user if their number was too high or too low.
