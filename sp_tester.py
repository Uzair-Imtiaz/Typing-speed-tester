import time
import random

def mistake(test, input):
    error = 0
    for i in range(len(test)):
        try:
            if test[i] != input[i]:
                error += 1
        except:
            error += 1
    return error

def speed(stime, etime, input):
    time_dif = round(etime - stime)
    spd = len(input) / time_dif
    return round(spd)

input = [ ]
test1 = random.choice(imput)
print("Typing test")
print(test1)
print('''

''')
time_s = time.time()
usertest = input("start typing: ")
time_e = time.time()
print()
print('speed: ', speed(time_s,time_e,usertest), 'w/sec' )
print('Mistakes: ', mistake(test1, usertest))
