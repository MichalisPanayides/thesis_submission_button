from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import win32com.client as win32

from constants import (
    RECEIVER_EMAIL,
    CC_EMAILS,
    SUBJECT,
    MESSAGE,
    ATTACHMENT_1,
    ATTACHMENT_2,
    ATTACHMENT_3,
)


def send_email():
    """
    This function sends an email with the thesis attached. The function:
    1. Creates an instance of outlook application
    2. Creates an instance of mail item
    3. Sets the receiver, cc, subject and body of the email
    4. Attaches the thesis to the email
    5. Attaches the thesis declaration and notice of submission forms
    6. Sends the email
    """ 
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = RECEIVER_EMAIL
    mail.CC = CC_EMAILS
    mail.Subject = SUBJECT
    mail.Body = MESSAGE

    mail.Attachments.Add(ATTACHMENT_1)
    mail.Attachments.Add(ATTACHMENT_2)
    mail.Attachments.Add(ATTACHMENT_3)

    mail.Send()


def display_button():
    """
    This function creates a clickable button to submit the thesis. The function:
    1. Creates an instance of tkinter frame in fullscreen mode
    2. Set the size of the tkinter window to be the size of my screen
    3. Load the image of the button using PhotoImage function
    4. Add a Label widget to display a message at the top
    5. Create a button widget that when clicked runs the press_button() function
    """
    def press_button():
        """
        This function is called when the button is clicked. The function:
        1. Sends an email with the thesis attached
        2. Displays a message box
        3. Opens a youtube video in a new tab
        """
        send_email()
        webbrowser.open('https://youtu.be/3GwjfUFyY6M?t=32')
        messagebox.showinfo("WOOHOO","Congratulations! You did it!")
        messagebox.showinfo("WOOHOO", "PhDone")


    win = Tk()
    win.attributes('-fullscreen', True)    
    win.geometry("1600x1050")

    click_btn = PhotoImage(file='button.png').subsample(2, 2)
    Label(win, text="Submission time!", font= ('Aerial 17 bold italic')).pack(pady=30)
    button = ttk.Button(win, image=click_btn, command=press_button).pack(pady=20)

    win.mainloop()

if __name__ == '__main__':
    display_button()
