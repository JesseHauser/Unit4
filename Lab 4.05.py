'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])
​
    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)
In your notebook
Write down any bugs that you see in the program
it is not counting the 1 and the for loop is meessed up
2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)
Continue in your notebook
Write down any bugs that you see in the program
not lined up properly and not calling the function
3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.
'''
def print_numbers(list):
        for i in range(0, len(list)+1):
            print(list)
num_list = [1, 2, 3, 4, 5, 6]
print_numbers(num_list)

def swapping_stars():
    line_str = ""
    for line in range(0, 6):
        for char in range(0,6):
            if line % 2 == char % 2:
                    line_str += "*"
            else:
                    line_str += "-"
    print(line_str)
swapping_stars()

user_input = input("what function would you like to run: 'swapping_stars' or 'print_numbers'")
if user_input == 'swapping_stars':
    swapping_stars()
elif user_input == 'print_numbers':
    print_numbers(num_list)
