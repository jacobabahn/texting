import TNAPI, random, time

from stuff import *

client = TNAPI.Client(email, pw, "Jacob")


def specific_text(name, num, message):
    for i in range(num):
        time.sleep(0.5)
        client.send_sms(name, message)


def compliments(name):
    compliment_list = []
    file = open("compliments.txt")

    for line in file:
        line = line[:-1]
        compliment_list.append(line)

    number = random.randint(1, len(compliment_list))
    message = compliment_list[number]
    client.send_sms(name, message)


def text_chris():
    # insults = []
    client.send_sms(contacts["Chris"], "Hey you Fat Fuck")


def main():
    q = input("Compliment Quincey? ")
    if q == "y" or q == "Y":
        compliments(contacts["Quincey"])

    name = input("Who would you like to spam? ")
    if name == "":
        return
    message = input("What do you want the contents of the message to be? ")
    numTexts = int(input("How many messages would you like to send? "))
    
    specific_text(contacts[name], numTexts, message)

main()