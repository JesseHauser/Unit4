'''
#############
Do Now 4.04
#############

In your console
---------------
Type and run the following code:
# my_building is a representation of the apartments on each floor of my 3 story building
my_building = [
    ['apt1a', 'apt1b', 'apt1c'],
    ['apt2a', 'apt2b', 'apt2c'],
    ['apt3a', 'apt3b', 'apt3c']
]
print("first floor: " + str(my_building[0]))
print("first floor, 3rd apartment: " + str(my_building[0][2]))

In your notebook
----------------
Respond to the following
Write down what was printed.

How you would access the 2nd apartment of the 3rd floor (apt3b)?

'''
my_building = [
    ['apt1a', 'apt1b', 'apt1c'],
    ['apt2a', 'apt2b', 'apt2c'],
    ['apt3a', 'apt3b', 'apt3c']
]
print("first floor: " + str(my_building[0]))
print("first floor, 3rd apartment: " + str(my_building[0][2]))
print("Third Floor, 2nd Apartment" + str(my_building[2][1]))