"""Python file to recieve the bot token and prefix from the user in a nice looking GUI program. Includes a setup class and a main function. Within the setup class, you will find several functions:
    askUser will prompt the user for their token and prefix.
    validityCheck will ensure that the user's inputs are valid.
    confirmation will check with the user to confirm their inputs.
    configAssign will write the user's token and prefix to a config.txt file.
    configLogging will append the new change to confighistory.txt.
"""

# Imports dependencies
import tkinter as tk
# from tkinter import ttk <-- Not used, but might be in the future.
from tkinter import simpledialog
from tkinter import messagebox

import sys
import datetime

# setup class where most of the work will take place


class setup(object):

    # Initiating variables. Some should be obvious by looking.
    # confirmquestion is the question that will be asked b/c of awkward tk syntax, and userconfirmation will be the boolean for whether the user is content with their inputs.
    def __init__(self, bot_token, bot_prefix):
        self.window = tk.Tk()
        self.window.withdraw()  # Hides root menu to make it look cleaner.
        self.token = bot_token
        self.prefix = bot_prefix
        self.confirmquestion = ""
        self.userconfirmation = ""

        self.now = datetime.datetime.now()  # This will be used in

    # Put together a series of input GUIs to obtain input from the user, also counts for users pressing cancel to exit the setup process.
    def askUser(self):
        self.bot_token = simpledialog.askstring(
            "Input", "What is the bot token?", parent=self.window)

        if self.bot_token == None:
            messagebox.showerror("Error", "Setup has been cancelled.")
            sys.exit()

        self.bot_prefix = simpledialog.askstring(
            "Input", "What will the bot's prefix be?", parent=self.window)

        if self.bot_prefix == None:
            messagebox.showerror("Error", "Setup has been cancelled.")
            sys.exit()

    # Checks user inputs against various statements to ensure that it is valid, restarting the program if they fail to pass the checks.
    def validityCheck(self):
        # Looks for empty inputs and prefixes of purely spaces
        if self.bot_token != "" and self.bot_prefix != "" and not self.bot_prefix.isspace():
            print("Valid input.")  # Just printing to the console.

        elif self.bot_token == "" or self.bot_prefix == "" or self.bot_prefix.isspace():
            messagebox.showerror(
                "Warning", "One of your inputs is invalid. The program will run again.")
            main()

    # Confirms users inputs with them again.
    def confirmation(self):

        # Variable used for question since messagebox syntax seems to not work with string compostion.
        self.confirmquestion = "So your bot token is:", self.bot_token, "and your bot prefix is:", self.bot_prefix
        self.userconfirmation = messagebox.askyesno("Confirmation", self.confirmquestion)

        if self.userconfirmation == True:
            messagebox.showinfo("Information", "Okay, your bot token and prefix have been set.")

        elif self.userconfirmation == False:
            messagebox.showinfo("Information", "Okay, running the program again.")
            main()

    # Writes user inputs to config.txt
    def configAssign(self):

        with open("config.txt", "w") as my_file:

            my_file.write(self.bot_token + "\n")
            my_file.write(self.bot_prefix)

    # Appends new changes to confighistory.txt
    def configLogging(self):
        with open("confighistory.txt", "a") as my_file:

            my_file.write("Date of update:" + str(self.now) + "\n")
            my_file.write("Bot Token: " + self.bot_token + "\n")
            my_file.write("Bot Prefix: " + self.bot_prefix + "\n")
            my_file.write("\n")

# Main function.


def main():

    # Initializing variables with useless values
    bot_token = ""
    bot_prefix = ""

    setup_instance = setup(bot_token, bot_prefix)  # Class instance created

    setup_instance.askUser()

    setup_instance.validityCheck()

    setup_instance.confirmation()

    setup_instance.configAssign()

    setup_instance.configLogging()


main()
