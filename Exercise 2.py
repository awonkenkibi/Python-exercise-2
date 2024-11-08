# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 8
x += 3
print(x)
# TODO: Multiply y by 2 using the *= operator
y = 9
y *= 2
print(y)
# TODO: Divide x by y and store the result in a variable called 'result'

results =8/9
# TODO: Print the value of 'result'
print(results)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
print(20> 15)
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
modulus = 15%2
print(modulus)

# TODO: Create a condition that checks if c is less than or equal to a
print(12<=20)
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = (20>15 or 15%2 and 12<=20)
# TODO: Print the value of 'final_condition'
print(final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int(input("what is your score?"))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if  score >= 90 and 100: 
    print("A")
elif score >= 80 and 89:
    print("B")
elif score >= 70 and 79:    
    print("C")
elif score >= 60 and 69: 
    print("D")
else:
    print("F")
# TODO: Print the grade for the given score
print(score)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = int(input("please insert a number"))
num2 = int(input("please insert a second number"))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("insert an opertion of your choice")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "*":
    Results = num1*num2


elif operation =="-": 
    
    # TODO: Handle the case of division by zero
else:



# TODO: Print the result of the operation
print("Results", num1*num2)
