"""Python file to recieve the bot token and prefix from the user in a nice looking GUI program. Includes a setup class and a main function. Within the setup class, you will find several functions:

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
    """
    Class for the setup.

    Will walk the user through the setup, asking them for various inputs to get the bot ready to start running.
    """


    def __init__(self, bot_token, bot_prefix):
        """
        Initializes variables.

        :param bot_token: The bot token
        :param bot_prefix: The bot prefix
        """
        self.window = tk.Tk()
        self.window.withdraw()  # Hides root menu to make it look cleaner.
        self.token = bot_token
        self.prefix = bot_prefix
        self.confirmquestion = ""
        self.userconfirmation = ""

        self.now = datetime.datetime.now()

    def askUser(self):
        """
        Asks user for their token and prefix.

        :return: void function
        """
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


    def validityCheck(self):
        """
        Checks the user's inputs against various conditions that would be problematic for the bot.

        :return: void function
        """
        # Looks for empty inputs and prefixes of purely spaces
        if self.bot_token != "" and self.bot_prefix != "" and not self.bot_prefix.isspace():
            print("Valid input.")  # Just printing to the console.

        elif self.bot_token == "" or self.bot_prefix == "" or self.bot_prefix.isspace():
            messagebox.showerror(
                "Warning", "One of your inputs is invalid. The program will run again.")
            main()


    def confirmation(self):
        """
        Confirms the user's inputs with them.

        :return: void function
        """

        # Variable used for question since messagebox syntax seems to not work with string compostion.
        self.confirmquestion = "So your bot token is:", self.bot_token, "and your bot prefix is:", self.bot_prefix
        self.userconfirmation = messagebox.askyesno("Confirmation", self.confirmquestion)

        if self.userconfirmation == True:
            messagebox.showinfo("Information", "Okay, your bot token and prefix have been set.")

        elif self.userconfirmation == False:
            messagebox.showinfo("Information", "Okay, running the program again.")
            main()


    def configAssign(self):
        """
        Writes the user's inputs to a text file to store them for the bot.

        :return: void function
        """

        with open("config.txt", "w") as my_file:

            my_file.write(self.bot_token + "\n")
            my_file.write(self.bot_prefix)

    def configLogging(self):
        """
        Will append new changes to log them.

        :return:  void function
        """
        with open("confighistory.txt", "a") as my_file:

            my_file.write("Date of update:" + str(self.now) + "\n")
            my_file.write("Bot Token: " + self.bot_token + "\n")
            my_file.write("Bot Prefix: " + self.bot_prefix + "\n")
            my_file.write("\n")


if __name__ == "__main__":

    bot_token = ""
    bot_prefix = ""

    setup_instance = setup(bot_token, bot_prefix)

    setup_instance.askUser()

    setup_instance.validityCheck()

    setup_instance.confirmation()

    setup_instance.configAssign()

    setup_instance.configLogging()

