'''
Do Now 4.02

1. In your console
Type the following code
    for i in range(0, 10):
        print(i)
In your notebook
Respond to the following
Write down what the range function does.
it goes through the list of numbers but not 10 cause 0 counts
2. In your console
Type the following
    a_list = ['apple', 'orange', 'pear', 'strawberry', 'grape']
    print(len(a_list))
    print(list(range(0, len(a_list)))
Continue in your notebook
Write down what range(0, len(a_list)) does.
it list all of the the stuff in a list as numbers
3. In your console
Use the range and len functions to make a for loop that prints the elements of a_list, one at a time.
'''
#for i in range(0, 10):
    #print(i)


a_list = ['apple', 'orange', 'pear', 'strawberry', 'grape']

for i in range(0,len(a_list)):
    print(a_list[i])
