import tkinter
import random

#Create root window
root = tkinter.Tk()

root.title("Guessing Game")

#Set the root window size
root.geometry("250x75")

#Remove the maximize button
root.resizable(0,0)

#Change the root window color
root.configure(bg="white")

#Get a random number for guessing
computer_guess = random.randint(1, 10)

def check():
    #Get the value from txt_guess
    user_guess = int(txt_guess.get())

    #Determine Higher, lower or right
    if user_guess < computer_guess:
        msg = "Higher!"
    elif user_guess > computer_guess:
        msg = "Lower!"
    elif user_guess == computer_guess:
        msg = "Correct!"
    else:
        msg = "Something went wrong..."

    #Show the result
    label_result["text"] = msg

    #Clear txt_guess
    txt_guess.delete(0, 5)

def reset():
    #Declare the global varible
    global computer_guess
    computer_guess = random.randint(1, 10)

    #Change the label_result text
    label_result["text"] = "Game reset! Guess again!"


#Create widgets
label_title = tkinter.Label(root, text = "Welcome to the Guessing Game!", bg="white")
label_title.pack()

label_result = tkinter.Label(root, text = "Good Luck!", bg="white")
label_result.pack()

btn_check = tkinter.Button(root, text = "Check", fg = "green", command = check)
btn_check.pack(side="left")

btn_reset = tkinter.Button(root, text = "Reset", fg = "red", command = reset)
btn_reset.pack(side="right")

txt_guess = tkinter.Entry(root, width = 3)
txt_guess.pack()

#Start the main event loop
root.mainloop()
root.destroy()