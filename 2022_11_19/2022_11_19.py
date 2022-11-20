## Small Python Script for today

## Python Data Structures : Dictionaries

## Dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

## Create and print a dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

## Accessing Items

## You can access the items of a dictionary by referring to its key name, inside square brackets:

x = thisdict["model"]
print(x)

## There is also a method called get() that will give you the same result:

x = thisdict.get("model")
print(x)

## Change Values

## You can change the value of a specific item by referring to its key name:

thisdict["year"] = 2018

## Loop Through a Dictionary

## You can loop through a dictionary by using a for loop.

## When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

## Print all key names in the dictionary, one by one:

for x in thisdict:
    print(x)
