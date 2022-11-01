## Detect a int value in a list to associate with a string value using a hashmap

# Create a list of int values

hashmap = {1: "Banana", 2: "Apple", 3: "Orange", 4: "Pear", 5: "Grape"}

# Create a input to detect a int value in the list

while True:
    try:
       input = int(input('Enter a number: '))
    except ValueError:
        print("You must enter a number")
    else:
        break # to exit the while loop

# Create a if statement to detect the int value in the list

if input in hashmap:
    print(hashmap[input])

else:
    print("No Fruits Found")


