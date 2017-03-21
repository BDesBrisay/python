#  CIS 117 Python Programming - Lab 8
#  By Bryce DesBrisay

class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.body = ""

    def append(self, line):
        self.body += line + "\n"

    def toString(self):
        return "From: " + self.sender + "\n" + "To: " \
        + self.recipient + "\n" + self.body


# From: Bob
# To: Santa
# For Christmas, I would like:
# Video games
# World peace
