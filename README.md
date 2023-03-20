# Thesis submission button

This is a simple script that creates a big red button that sends an email when pressed. The button was created for the submission of my thesis. It is a simple script that can be used for any purpose. Currently, this script only works on Windows when using outlook as the email client.

## Installation

There are no dependencies. Just open a terminal and clone the repository.

```bash
$ git clone
$ cd thesis_submission_button
```

Alternatively, you can download the repository as a zip file and extract it.

## Usage

The way the button works is such that when you press it, it sends an email to a specified receiver and cc's a list of people. Then the `Play/Pause media` functionality of the machine is triggered. This way you can pause a song at a specific time and when the button is pressed, the song will resume from that point. Finally, the script opens a webpage with a link.

Before running the script, you need to edit the `constants.py` file so that it contains the receiver's email address, the email addresses of the people who need to be cc'd in, the subject of the email, the body of the email, and the path of three possible attachments. The attachments are optional. If you don't want to attach anything, just leave the paths empty. There are two additional constants that control the size of the button and the webpage that is opened when the button is pressed. For more information, see the documentation in the `constants.py` file.

Then, you can run the script.

```bash
$ python main.py
```


# Limitations
This script only works on Windows when using outlook as the email client. It is possible to make it work on other operating systems and email clients, but I didn't have the time to implement that. If anyone wants to do it, feel free to make a pull request.