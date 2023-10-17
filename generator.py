# password generator    
import random
import string
def gen_password(length):
    for i in range(length):
        t = random.choice(string.ascii_letters)
        print(t,end = '')
length = 6
a = gen_password(length)
