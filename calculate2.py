# tell user about operations they can do
print ('welcome to Jack basic math app for addition, subtration, division, multiplican ')

user_choice = input("""
enter "add" for addition
enter "subtract" for subtraction
enter "div" for division
enter "mult" for multiplication
""").lower()

if user_choice == 'add':
    num1 = int(input('Enter first number :'))
    num2 = int(input('Enter another number :'))
    result = num1 + num2
    print("{} + {} = {}".format(num1, num2, result))

elif user_choice == 'subtract':
    num1 = int(input('Enter first number :'))
    num2 = int(input('Enter another number :'))
    result = num1 - num2
    print("{} - {} = {}".format(num1, num2, result))

elif user_choice == 'div':
    num1 = int(input('Enter first number :'))
    num2 = int(input('Enter another number :'))
    result = num1 / num2
    print("{} / {} = {}".format(num1, num2, result))

elif user_choice == 'mult':
    num1 = int(input('Enter first number :'))
    num2 = int(input('Enter another number :'))
    result = num1 * num2
    print("{} * {} = {}".format(num1, num2, result))
 
else:  
        print("bye")







