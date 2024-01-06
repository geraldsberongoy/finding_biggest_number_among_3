# Assignment 4

# Ask user to input 3 numbers. Find and print the 
# biggest number using only if-else statement

# pseudocode
# Ask user to input number 1
first_number = float(input("Enter first number: "))

# Ask user to input number 2
second_number = float(input("Enter second number: "))

# Ask user to input number 3
third_number = float(input("Enter third number: "))

# Find highest among the inputted numbers using if-else statement
if first_number > second_number and first_number > third_number:
    highest = first_number
elif second_number > first_number and second_number> third_number:
    highest = second_number
else:
    highest = third_number
# Diplay the highest number
print(f"The highest number is: {highest:.2f}")