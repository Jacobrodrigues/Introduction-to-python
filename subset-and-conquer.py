#test for subset and conquer
""" Subsetting python list is a piece of cakes. Take the code sample below.
    which create list X and the selects"b" from it. Remember that this is the second element,
    so it has index, you can  also use negative indexing 
"""
"""instructions
 #  I - Print out the second element from the areas list (it has the value 11.25)
 #  II - Subset and print out the last element of areas. being 9.50. Using a negative index makes sense here!
 #  III - Select the number representing the area of the living room (20.0) and print it out
"""
# Start the code

# Create the areas list
areas = ["hallway",11.25,"kitchen",18.0,"living room",20.0,"bedroom",10.75,"bathroom", 9.50]

# I - Print out the second element from the areas list (it has the value 11.25)
print(areas[1])

# II - Subset and print out the last element of areas. being 9.50. Using a negative index makes sense here!
print(areas[-1])

# III - Select the number representing the area of the living room (20.0) and print it out
print(areas[5])