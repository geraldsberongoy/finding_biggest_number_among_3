# Assignment 4

# Ask user to input 3 numbers. Find and print the 
# biggest number using only if-else statement

#import
import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image

customtkinter.set_appearance_mode("dark")

window = customtkinter.CTk()
window.title("Highest Number")
window.geometry("360x480")
window.resizable(width=False, height=False)

# Functions
def determine():
    first_number = float(entry_first_number.get())
    second_number = float(entry_second_number.get())
    third_number = float(entry_third_number.get())
    messagebox.showinfo("Submitted", "The highest number has been determined.")
    
    
    def highest_of_three(first_number, second_number, third_number):
        if any (entry == "" for entry in (entry_first_number.get(), entry_second_number.get(), entry_third_number.get())):
            messagebox.showerror("Error", "Please enter all the field.")

        if first_number >= second_number and first_number >= third_number:
            return first_number
        elif second_number >= first_number and second_number >= third_number:
            return second_number
        else:
            return third_number
        
    highest_number = highest_of_three(first_number, second_number, third_number)
    number_text_label.configure(text="The highest number is:")
    highest_number_label.configure(text=(highest_number), font=('Helvetica', 20, 'bold'), text_color="#D21404")
        
# GUI WIDGETS

banner_image = customtkinter.CTkImage(Image.open("banner.png"), size=(320, 100))
label_banner_image = customtkinter.CTkLabel(window, text="", image=banner_image, corner_radius=100)
label_banner_image.place(relx=0.5, rely=0.13, anchor=CENTER)

# Ask user to input number 1
entry_first_number = customtkinter.CTkEntry(window, placeholder_text="Enter the first number", placeholder_text_color="white"	, corner_radius=10, width=300, height=30)
entry_first_number.place(relx=0.5, rely=0.3, anchor=CENTER)

# Ask user to input number 2
entry_second_number = customtkinter.CTkEntry(window, placeholder_text="Enter the second number",placeholder_text_color="white", corner_radius=10, width=300, height=30)
entry_second_number.place(relx=0.5, rely=0.4, anchor=CENTER)

# Ask user to input number 3
entry_third_number = customtkinter.CTkEntry(window, placeholder_text="Enter the third number",placeholder_text_color="white", corner_radius=10, width=300, height=30)
entry_third_number.place(relx=0.5, rely=0.5, anchor=CENTER)

 # Function inside the command button that finds the highest among the inputted numbers using if-else statement
determine_button = customtkinter.CTkButton(window, text="Determine", text_color="black", font=('Open Sans', 20, 'bold'), command= determine, fg_color="#E1A3FF", width=300, height=30)
determine_button.place(relx=0.5, rely=0.6, anchor=CENTER)

frame_result = customtkinter.CTkFrame(window, border_width=2, border_color="black", width=320, height=140)
frame_result.place(relx=0.5, rely=0.81, anchor=CENTER)

# Diplay the highest number                  
result_label = customtkinter.CTkLabel(frame_result, text="Result", font=('Helvetica', 26, 'bold'))
result_label.place(relx=0.5, rely=0.12, anchor=CENTER)

number_text_label = customtkinter.CTkLabel(frame_result, text="")
number_text_label.place(relx=0.5, rely=0.4, anchor=CENTER)

highest_number_label = customtkinter.CTkLabel(frame_result, text="")
highest_number_label.place(relx=0.5, rely=0.65, anchor=CENTER)

# # pseudocode
# # Ask user to input number 1
# first_number = float(input("Enter first number: "))

# # Ask user to input number 2
# second_number = float(input("Enter second number: "))

# # Ask user to input number 3
# third_number = float(input("Enter third number: "))

# # Function that finds the highest among the inputted numbers using if-else statement
# highest_number = highest_of_three(first_number, second_number, third_number)

# # Diplay the highest number
# print("The highest number is ", highest_number)")

window.mainloop()