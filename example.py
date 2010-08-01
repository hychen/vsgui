#!/usr/bin/env python
"""
Example of VSGUI to describe what it does....

@author Hsin-Yi Chen (hychen) <ossug.hychen@gmail.com>
"""
import sys
import time
import random

from vsgui import *

anwsers = ["loves you", "don't love you"]

notice("Hey! Example of VSGUI is running!")

if not input_yesno("Do you want to start this example to see how it work?",
                    y="Sure", n="No! I don't want"):
    warning("OK! but please read the codes if you have time.")

username = input_text("Your name:")
if not check_passwd(username, text="(passwd is %s)" % username):
    error("Die!")
    sys.exit()

usersex = input_ab("What is your sex?", 'male', 'famel')
liked_sex = input_radiolist(['sex'], ['','male', '','famel', '', 'unknow'], text="What is your lover's sex?")

def get_anwser():
    update = progress('Starting to ask Mazo-Po', auto_close=True)
    update('20', "sending your questions to sky")
    time.sleep(1)
    update('40', "Mazo-Po hear questions")
    time.sleep(1)
    update('60', "Mazo-Po is asking A-pi-PO")
    time.sleep(1)
    update('80', "A-pi-Po is thinking")
    anwser = random.choice(anwsers)
    time.sleep(1)
    update('100', "A-pi-Po get a anwser")
    return anwser

accept = False
while not accept:
    anwser = get_anwser()
    msg = ['Your are %s, a %s' % (username, usersex),
           'your lover is a %s' % liked_sex,
           'and he/her %s' % anwser]
    msg.append("Do you accept this?")

    accept = input_yesno(','.join(msg), y='Yes', n='Fuck!')

# save result
# @TODO write example for saving file
