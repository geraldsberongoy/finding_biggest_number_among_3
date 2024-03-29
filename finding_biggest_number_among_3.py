# Assignment 4

# Ask user to input 3 numbers. Find and print the 
# biggest number using only if-else statement

#import
import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image

#themes
customtkinter.set_appearance_mode("dark")

#main window
window = customtkinter.CTk()
window.title("Highest Number")
window.geometry("360x480")
window.resizable(width=False, height=False)

# Functions
def determine():
    if any (entry == "" for entry in (entry_first_number.get(), entry_second_number.get(), entry_third_number.get())):
            messagebox.showerror("Error", "Please enter all the field.")
            return
    try:
        first_number = float(entry_first_number.get())
        second_number = float(entry_second_number.get())
        third_number = float(entry_third_number.get())
        messagebox.showinfo("Submitted", "The highest number has been determined.")
        
    except ValueError:
        messagebox.showerror("Error", "Oppps! Please enter valid numeric values.")
        return
    
    def highest_of_three(first_number, second_number, third_number):
        if first_number >= second_number and first_number >= third_number:
            return first_number
        elif second_number >= first_number and second_number >= third_number:
            return second_number
        else:
            return third_number
        
    highest_number = highest_of_three(first_number, second_number, third_number)
    number_text_label.configure(text="The highest number is:", font=('Helvetica', 15))
    highest_number_label.configure(text=(highest_number), font=('Helvetica', 30, 'bold'), text_color="#D21404")

def clear_entries():
    entry_first_number.delete(0, END)
    entry_second_number.delete(0, END)
    entry_third_number.delete(0, END)
    number_text_label.configure(text="")
    highest_number_label.configure(text="")
     
# GUI WIDGETS
#Image
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
determine_button = customtkinter.CTkButton(window, text="Determine", text_color="black", font=('Helvetica', 15, "bold"), command= determine, fg_color="#bb86fc", width=145, height=30)
determine_button.place(relx=0.27, rely=0.6, anchor=CENTER)

clear_button = customtkinter.CTkButton(window, text="Clear", text_color="white", font=('Helvetica', 15, "bold"), command=clear_entries, fg_color="#3a2d49", width=145, height=30)
clear_button.place(relx=0.72, rely=0.6, anchor=CENTER) 

# Frame for the result
frame_result = customtkinter.CTkFrame(window, border_width=2, border_color="black", width=320, height=140)
frame_result.place(relx=0.5, rely=0.81, anchor=CENTER)

# Diplay the highest number                  
result_label = customtkinter.CTkLabel(frame_result, text="Result", font=('Helvetica', 26, 'bold'))
result_label.place(relx=0.5, rely=0.15, anchor=CENTER)

number_text_label = customtkinter.CTkLabel(frame_result, text="")
number_text_label.place(relx=0.5, rely=0.4, anchor=CENTER)

highest_number_label = customtkinter.CTkLabel(frame_result, text="")
highest_number_label.place(relx=0.5, rely=0.65, anchor=CENTER)

window.mainloop()