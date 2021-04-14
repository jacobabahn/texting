import TNAPI, random

from stuff import *

client = TNAPI.Client(email, pw, "Jacob")

def compliments(name):
    compliment_list = []
    file = open("compliments.txt")

    for line in file:
        line = line[:-1]
        compliment_list.append(line)

    number = random.randint(1, len(compliment_list))
    message = compliment_list[number]
    client.send_sms(name, message)

compliments(contacts["Quincey"])