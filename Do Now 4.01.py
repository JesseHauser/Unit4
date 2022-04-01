'''
Do Now 4.01
1. In your console
Type the following Code
    single_fruit = ['apple', 'banana', 'watermelon', 'grape']
    multi_fruit = []
    multi_fruit.append(single_fruit[0] + 's')
    multi_fruit.append(single_fruit[1] + 's')
    multi_fruit.append(single_fruit[2] + 's')
    multi_fruit.append(single_fruit[3] + 's')
    print(multi_fruit)

In your notebook
Respond to the following
Briefly write down what happened. What would happen if you added 100 items to the list single_fruit? 
Write down how you would update multi_fruit.

2. In your console
Type the following
    list_of_numbers = [3, 5, 10, 23]
    for num in list_of_numbers:
        print(f"num is " + {num})
        
Continue in your notebook
Respond to the following
Briefly write down what happened. How would this change if you added 100 items to list_of_numbers?

3. In your console
Rewrite the code from part 1 using knowledge from part 2.
'''
'''
single_fruit = ['apple', 'banana', 'watermelon', 'grape']
multi_fruit = []
multi_fruit.append(single_fruit[0] + 's')
multi_fruit.append(single_fruit[1] + 's')
multi_fruit.append(single_fruit[2] + 's')
multi_fruit.append(single_fruit[3] + 's')
print(multi_fruit)
'''
#it added the single fruit list to multi fruit list while adding an s at the end, you would have to keep doing it 100 times.
'''
list_of_numbers = [3, 5, 10, 23]
for num in list_of_numbers:
    print(f"num is {num}")
'''
# it made it run through the print statement going through the list with loop 



from numpy import append


single_fruit = ['apple', 'banana', 'watermelon', 'grape']
multi_fruit = []
for item in single_fruit:
    multi_fruit.append(f"{item}s")
    print(multi_fruit)
