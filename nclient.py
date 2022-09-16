# client.py TCP chatbot client
import argparse  # importing modules
import random  # importing module
import socket  # importing module

comment = None  # setting comment variable as null
negativeComment = None  # setting negativeComment variable as null
nextAns = None  # setting next variable as null


# function bot()
def bot(datass, name):
    global comment, negativeComment, nextAns  # making variable modifiable for outside of scope

    # parse string
    words = datass.split()
    action = words[-1]
    action = action[:]
    sender = words[0]
    sender = sender[:-1]

    # comments
    negative = ["rawfood", "heating", "cooling"]  # negative comments
    positive = ["order", "takeaway", "reservation"]  # positive comments

    if sender == "Customer":  # respond to customer
        comment = action  # setting comment variable as action variable value
        nextAns = 1  # setting next variable as 1
        if comment in negative:  # checking if there is negative comment
            negativeComment = True  # setting negativeComment variable as TRUE
            return "{}: We have had some problem with {} this week.".format(name, comment)  # return text
        elif comment in positive:  # positive comment
            negativeComment = False  # setting negativeComment variable as FALSE
            return "{}: We can help with {}!".format(name, comment)  # return text
        else:  # if comment is undefined
            negativeComment = None  # setting negativeComment variable as None
            return "{}: Hmmm... I don't know if I understood correctly.".format(name)  # return text
    elif nextAns == 1:  # customer support member 2 response
        nextAns = 2  # setting next variable as 2
        if negativeComment:  # if negativeComment is TRUE -> Negative
            return "{}: Yes true, {}. Food {} have been the main priority in the office...".format(name,
                                                                                                   sender, comment)
        elif negativeComment is None:  # if negativeComment is undefined
            return "{}: I agree, what do you mean?".format(name)
        elif not negativeComment:  # if negativeComment is not TRUE -> Positive
            return "{}: Sure. We can help.".format(name)
    elif nextAns == 2:  # customer support member 3 response
        nextAns = 3  # setting next variable as 3
        if negativeComment:  # if negativeComment is TRUE -> Negative
            department = random.choice(["office", "CEO", "chef"])
            # return text
            return "{}: I will send the complaint to the {} hope that will fix it!".format(name, department)
        elif not negativeComment:  # if negativeComment is not TRUE -> Positive
            return "{}: Let me check the system for {}...".format(name, comment)  # return text
    elif nextAns == 3:  # bot 1 response
        nextAns = 4  # setting next variable as 4
        if negativeComment:  # if negativeComment is TRUE -> Negative
            # return text
            return "{}: Sounds great! I hope the problem with the food {} is soon fixed!".format(name, comment)
        elif negativeComment is None:  # if negativeComment is undefined
            return "{}: No comment.".format(name, sender)  # return text
        elif not negativeComment:  # if negativeComment is not TRUE -> Positive
            return "{}: Looks good in my end. We will set it up for you.".format(name)  # return text
    elif nextAns == 4:  # customer support member 2 response
        if negativeComment:  # if negativeComment is TRUE -> Negative
            couponvalue = random.choice(["5$", "15$", "45$"])
            return "{}: To make it up for you here is a {} coupon for your next purchase.".format(name, couponvalue)
        elif not negativeComment:  # if negativeComment is not TRUE -> Positive
            return "{}: Hope that was good enough answer.".format(name)  # return text


parser = argparse.ArgumentParser(
    description='Connect chatserver.Exa:client.py localhost 4242 NAME')  # holding information to parse command line
parser.add_argument('host', type=str,
                    help='Server for customer support to connect.')  # adding argument to parser object
parser.add_argument('port', type=int,
                    help='Port to connect customer support. Must be integer.')  # adding argument to parser object
parser.add_argument('bot', type=str, help='Customer Support Name.')  # adding argument to parser object
args = parser.parse_args()  # setting variable args as parser attempts to give errors whenever the user made a mistake
host = args.host
port = args.port
botName = args.bot

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # constants used to specify the address family and socket type
s.connect((host, port))  # connect to customer

s.send(botName.encode())  # send customer support member name to customer
welcome = s.recv(1024).decode()  # receiving welcome message
print(welcome)  # Printing text

while True:  # runs whithout condition until break
    try:  # testing code for errors
        data = s.recv(1024).decode()  # recv from customer
        print(data)  # Printing text
        resp = bot(data, botName)  # parse string and create response
        s.send(resp.encode())  # send response
    except Exception as err:  # statement that defines argument to except statement
        print("\nThe customer is happy! You are now being disconnected.")  # Printing text
        break  # terminate loop and skipping to next code
