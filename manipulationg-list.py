# Replace list elements
''' Replace list elements is pretty easy. Simply subset the list and assing new values to the subset. You can select elements
    or you can change entire list slices at once.
    
    Use the Ipython Shell to experiment with the commands below. Can you tell what's happening and why?
    x = ["a","b","c","d"]
    x[1]= "r"
    x[2:]=["s","t"]

    Use this and the following exercises, you'll continue working on the areas list that contains the names and areas of different rooms in a 
    house
'''

#Instructions
    # I - Update the area of the bathroom area to bem 10.50 square meters instead of 9.50
    # II - Make the areas list more trendy! Change "living room" to "chill zone".

# Let's go the code

#Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

#Correct the bathroom area
# I - Update the area of the bathroom area to bem 10.50 square meters instead of 9.50
areas[9] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

print(areas)