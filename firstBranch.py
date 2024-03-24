import string
import time
text = 'Tuong Nguyen, A.K.A NGUOI DEP TRAI NHAT Vietnam!'

def printSlow(text, delay=0.02):
    temp = ''
    for char in text:
        if char in string.printable:
            temp += ('\033[92;1m' + char + '\033[0m')
            print(temp, end='\r')
            time.sleep(delay)