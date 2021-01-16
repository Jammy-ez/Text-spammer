import time
import pyautogui
import pyperclip
from os import system, name
from datetime import datetime

def clear():
    if name == 'nt':
        _ = system('cls')

print('Loading...')
time.sleep(1)
clear()
print('This tool was made by Jam')
time.sleep(1)
clear()
main= '''	
   __                        __                           ___       _
   \ \  __ _ _ __ ___  ___  / _\_ __   __ _ _ __ ___     / __\ ___ | |_
    \ \/ _` | '_ ` _ \/ __| \ \| '_ \ / _` | '_ ` _ \   /__\/// _ \| __|
 /\_/ / (_| | | | | | \__ \ _\ \ |_) | (_| | | | | | | / \/  \ (_) | |_
 \___/ \__,_|_| |_| |_|___/ \__/ .__/ \__,_|_| |_| |_| \_____/\___/ \__|
                               |_|
1)Spam from input
2)Spam from file
3)Credit
	'''
main1= '''
   __                        __                           ___       _
   \ \  __ _ _ __ ___  ___  / _\_ __   __ _ _ __ ___     / __\ ___ | |_
    \ \/ _` | '_ ` _ \/ __| \ \| '_ \ / _` | '_ ` _ \   /__\/// _ \| __|
 /\_/ / (_| | | | | | \__ \ _\ \ |_) | (_| | | | | | | / \/  \ (_) | |_
 \___/ \__,_|_| |_| |_|___/ \__/ .__/ \__,_|_| |_| |_| \_____/\___/ \__|
                               |_|
	'''
print(main)
op = input("CHOOSE OPTION:")
if op == '1':
	clear()
	print(main1)
	msg = input("Enter the message: ")
	n = input("How many times ?: ")
	cnt1 = input("Timer: ")
	cnt = float(cnt1)
	print('3')
	time.sleep(1)
	print('2')
	time.sleep(1)
	print('1')
	time.sleep(1)

	print("Printing "+ msg)
	print(n + " Times")

	for i in range(0,int(n)):
		time.sleep(cnt)
		pyautogui.typewrite(msg + '\n')

if op == '2':
	clear()
	print(main1)
	direct = input("Enter file name: ")
	cnt1 = input("Timer: ")
	cnt = float(cnt1)
	print('Finding File..')
	time.sleep(1)
	pile = open(direct,"r")
	print('3')
	time.sleep(1)
	print('2')
	time.sleep(1)
	print('1')
	time.sleep(1)
	print('Printing' + direct)

	for word in pile:
		time.sleep(cnt)
		pyautogui.typewrite(word)
		pyautogui.press("enter")
if op == '3':
	clear()
	print(main1)
	print('This tool was made by Jam')
	print('''
My youtube:https://www.youtube.com/channel/UCmtvqkSQZRHmtiEyXA0IQSg
My tiktok:https://www.tiktok.com/@jamovh?lang=en
		''')
	time.sleep(10)
	print('Closing in:3')
	time.sleep(1)
	print('Closing in:2')
	time.sleep(1)
	print('Closing in:1')
	time.sleep(1)
