# server.py - TCP chatbot server
import argparse  # importing module
import socket  # importing module
import time  # importing module

client = []  # client list
resp = []  # response list
CommentList = ["takeaway", "reservation", "order", "cooling", "heating", "rawfood"]  # comment list
verboseMode = False  # additional details TRUE/FALSE


# function sendMsg()
def sendMsg(msg, clientSkip):  # send msg to client
    if clientSkip:  # skip client
        for c in client:  # loop
            try:
                if c != clientSkip:
                    c.send(msg.encode())
                else:
                    c.send(msg.encode() + " (this is me!)".encode())
            except Exception as err:  # client error
                clientError(c)
    else:  # send to all
        for c in client:  # for loop
            try:
                c.send(msg.encode())
            except Exception as err:
                clientError(c)


# function getResp()
def getResp():  # fetching respones from customer support members
    for c in client:  # for loop
        try:
            resp.append(c.recv(1024).decode())  # store response from clients
        except Exception as err:
            clientError(c)


# function clientError()
def clientError(c):
    # remove client from list and send error msg
    global client
    client.remove(c)
    sendMsg("\nError: Oh no! A bot was disconnected:(", None)
    print("Error: A bot was disconnected.")


def chat():  # starting chat from beginning
    global s
    if verboseMode:  # Checking if verboseMode is TRUE
        print("\n--- Chat ---")  # Printing text
        print("Status: {} customer support connected.".format(len(client)))  # Printing text

    if len(client) < 2:  # min 2 from customer support team (client.py) must be connected to the server.
        print("Error: 2 or more from support team must be connected.")  # Printing text
        exit()  # exiting process

    while True:  # runs whithout condition until break
        print("What can we help you with or write 'bye' to leave.")  # Printing text
        stringcomment = str(input())  # user writes in a comment
        if stringcomment.lower() == "bye":  # If there is 'bye' in the sentence
            print("Disconnecting support team...")  # Printing text
            for c in client:  # for loop
                c.close()  # closing

            print("Chat stopped! Have a nice day!")  # Printing text
            exit()  # exiting process
        else:
            # checking for comment in sentence
            comment = next((x for x in CommentList if x in stringcomment), stringcomment) # If there is a comment in the sentence
            time.sleep(1)  # delaying next code
            # variable to send to all customer support members the sentence from customer
            msg = "\nCustomer: {}".format(comment)
            sendMsg(msg, None)  # sending msg text to all customer support members

            index = 0  # making variable

            for i in range(5):  # for loop where range starting in 0 and increase by 1 and stops on 5
                # checking if the index variable is higher than items in clients minus 1
                if index > len(client) - 1:
                    index = 0  # setting index as 0
                time.sleep(1)  # delaying next code
                getResp()  # fetching respones from customer support members
                print("{}".format(resp[index]))  # Printing text
                sendMsg(resp[index], client[index])  # send respone to clients, not sender
                resp.clear()  # removing all elements from list
                index += 1  # adding one to index

            sendMsg("-- Question round done. Waiting on customer... ",
                None)  # sending text to cusomter support members

            print("\n\nAre you happy with the answers? (yes/no)")  # Printing text
            restart = str(input())  # getting input from customer on next task

            if restart.lower() == "yes":  # if the response from customer is 'yes'
                print("\n\nNICE! now..")  # Printing text
                getResp()  # fetching respones from customer support members
                resp.clear()  # removing all elements from list
                chat()  # start again from beginning
            if restart.lower() == "no":  # if the response from customer is 'no'
                print("To bad. See you later, alligator!")  # Printing text
                time.sleep(1)  # delaying next code
                print("Disconnecting support team...")  # Printing text
                for c in client:  # for loop
                    c.close()  # closing

                print("**Support team left**")  # Printing text
                exit()  # exiting process
            else:  # if not the response from customer is yes or no
                time.sleep(1)  # delaying next code
                print("Strange...? The chat is closing...")  # Printing text print("Well bye!")  # Printing text
                for c in client:  # for loop
                    c.close()  # closing

                time.sleep(1)  # delaying next code
                print("Disconnecting support team...")  # Printing text
                print("Chat stopped!")  # Printing text
                exit()  # exiting process


# parse terminal arguments
parser = argparse.ArgumentParser(
    description='Start chatserver. Example: server.py 4242')  # object holding information to parse command line
parser.add_argument('port', type=int,
                    help='Port to connect customer support. Must be integer')  # adding argument to parser object
parser.add_argument('-v', '--verbose', help='Show debug info.', action='store_true')  # adding argument to parser object
args = parser.parse_args()  # setting variable args as parser attempts to give errors whenever the user made a mistake
port = args.port

if args.verbose:  # if option is specified
    verboseMode = True  # setting verbose Mode to TRUE
    print(
        "Customer: localhost\nPort: {}\nSocket: SOCK_STREAM (TCP)\nStatus: listening...".format(port))  # Printing text

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCPsocket over IPv4
s.bind(("localhost", port))  # Binding to port
s.listen()  # Listening for connections

print("Welcome to Foodora customer support!")  # Printing text
print("--- What's your name? ---")  # Printing text
customerName = str(input())  # Making the customer write their name
print("\nHi, " + customerName + "!")  # Printing text
print("Hold on while we wait for excatly 3 people from our support team...")  # Printing text
time.sleep(3)  # delaying next code
print("Thank you for your patience, the support team are almost ready.\n")  # Printing text

while True:  # runs whithout condition until break
    # accept connection and add customer support member
    conn, addr = s.accept()  # Adding variable new socket object and address bound to socket
    client.append(conn)  # client getting socket object
    num_clients = len(client)  # setting num_clients as number of items in client variable

    botName = conn.recv(1024).decode()  # getting customer support member name
    print("--- {} have joined the chat | {}".format(botName, addr) + " ---")  # Printing text
    if num_clients == 1:  # Checking if only one customer support member is connected to server
        print("*Waiting for two more from customer support...\n")  # Printing text
    if num_clients == 2:  # Checking if two customer support members is connected to server
        print("*Waiting for the last guy now...\n")  # Printing text

    # Message to customer support member on how many members have joined the server
    welcome = "Welcome {}!\n{} / 3 customer support connected.".format(botName, num_clients)
    conn.send(welcome.encode())  # Sending message to client side

    if num_clients == 3:  # Checking if three customer support members is connected to server
        print("\nThank you for your patience, all three from the support team are here!\n")  # Printing text
        chat()  # starting chat
        break  # terminate loop and skipping to next code
