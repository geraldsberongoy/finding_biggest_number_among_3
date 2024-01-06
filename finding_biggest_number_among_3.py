# Assignment 4

# Ask user to input 3 numbers. Find and print the 
# biggest number using only if-else statement

#import
import customtkinter
from tkinter import *


customtkinter.set_appearance_mode("dark")

window = customtkinter.CTk()
window.title("Highest Number")
window.geometry("360x480")
window.resizable(width=False, height=False)


# Functions
def highest_of_three(first_number, second_number, third_number):
    if first_number > second_number and first_number > third_number:
        return first_number
    elif second_number > first_number and second_number> third_number:
        return second_number
    else:
        return third_number
    
# pseudocode
# Ask user to input number 1
first_number = float(input("Enter first number: "))

# Ask user to input number 2
second_number = float(input("Enter second number: "))

# Ask user to input number 3
third_number = float(input("Enter third number: "))

# Function that finds the highest among the inputted numbers using if-else statement
highest_number = highest_of_three(first_number, second_number, third_number)

# Diplay the highest number
print(f"The highest number is {highest_number:.2f}")

window.mainloop()