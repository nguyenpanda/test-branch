import string
import time
text = 'Tuong Nguyen, A.K.A NGUOI DEP TRAI NHAT Vietnam!'

def printALot(text, delay=0.005):
    temp = ''
    for char in text:
        for i in string.printable:
            if i == char or char == ' ':
                time.sleep(delay)
                print(temp + '\033[91;1m' + i + '\033[0m')
                temp += ('\033[92;1m' + char + '\033[0m')
                break
            else:
                time.sleep(delay)
                print(temp + '\033[91;1m' + i + '\033[0m')