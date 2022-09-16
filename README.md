![main banner](https://github.com/Oslo-Metropolitan-University-OsloMet/individual-portfolio-assignment-1-s344055/blob/main/Banner.png "Main banner")

# TCP Python Chatbot | IPA-1
_Individual Portfolio Assignment 1 by s344055_


This chatbot is created with inspiration from any customer support teams of a takeaway/delivery company. In my use-case I used foodora customer support. The bots are coded to respond to either postive og negative questions/comments from the customer. This is an individual portfolio assignment in the course "DATA2410 - Networking and cloud computing" at Oslo Metropolitan University. We were tasked with creating a chat room with bots and a host that could talk to each other through a TCP socket. **The chatbot is written in python.** 

**The 6 words the bot is looking for is** `["takeaway", "reservation", "order", "cooling", "heating", "rawfood"]` so make sure to write a sentence with one of these words.

<br>

<h2>How to run</h2>
<ol>
    <li>Start by running server.py in a terminal window with the port as the agrument</li>
    <li>The server is now in listening-mode and are waiting for connections. While waiting the customer is asked for a name</li>
    <li>Open up three new terminal windows for the customer support team/bot to connect to the server.</li>
    <li>In each of the terminal windows write in python3 nclient.py localhost 4242 “CUSTOMER_SUPPORT_NAME” to start nclient.py where the arguments are IP-address, port and Customer Support Name.</li>
    <li>When all three bots are conntected the chat is started. The customer is now asked for the question/comment. The customer can either write a word or a whole sentence. The system detects the important word of the sentence.</li>
    <li>The customer support team will now answer the customer based on negative or positive questions/comments.</li>
    <li>To disconnect from the chat, the customer can write ‘bye’ on first question, or ‘No’ on the question if the customer is happy with the answers.</li>
</ol>

<br>

<h2>nServer.py: Customer</h2>

```python
**Requires port number as argument:**

python3 nserver.py 4242

Type nserver.py --h for more info
```

<br>

<h2>nClient.py: Customer support Team/Bots</h2>

```python
**Requires hostname, port number and customer support name as arguments. The customer support name can be whatever you want.**

python3 nclient.py localhost 4242 

Type nclient.py --h for more info
```

<br>
<h2>Sources</h2>
<ul>
    <li>https://realpython.com/python-sockets/</li>
    <li>https://www.geeksforgeeks.org/simple-chat-room-using-python/</li>
    <li>https://github.com/sondrekulseng/Python-chatbot/blob/main/README.md</li>
    <li>https://github.com/Axmar00/Python-chatbots/blob/master/README.md</li>
    <li>https://github.com/mainadennis/An-AI-Chatbot-in-Python-and-Flask</li>
</ul>
