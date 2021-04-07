# List of slicing and dicing(2)

""" 
    In the video, Hugo first discussed the syntax where you specify both where to begin and end the slice of your list
    my_list[start:end]

    However, it's also possible not to specify these indexes. If you don't specify the begin index. Python figures out that you want to start
    your slice at the beginning of yout list. If you don't specify the end index, the slice will go all the way to the last element of your list. to experiment
    with this,  try the following commands in the Ipython shell:

    x = ["a","b","c","d"]
    x[:2]
    x[2:]
    x[:]
    
"""

#instructions 
    # I - Create downstairs again, as first 6 elements of areas. This time, simplify by omitting the begin index.

    # II - Create upstairs again, as last 4 elements of areas. This time, simplify by omitting the end index. 

# Let's the code

# Create the areas list
areas= ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Create downstairs again, as first 6 elements of areas. This time, simplify by omitting the begin index.
downstairs= areas[:6]

# Create upstairs again, as last 4 elements of areas. This time, simplify by omitting the end index.
upstairs = areas[6:]

# print both downstairs and upstairs using print()
print(downstairs)
print(upstairs)