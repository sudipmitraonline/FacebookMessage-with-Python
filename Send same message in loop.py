import fbchat 
from getpass import getpass 
username = str(input("Username: ")) 
client = fbchat.Client(username, getpass()) 
no_of_friends = int(input("Number of friends: ")) 
for i in range(no_of_friends): 
    name = str(input("Name: ")) 
    friends = client.searchForUsers(name) # return a list of names 
    friend = friends[0] 
    msg = str(input("Message: ")) 
    for i in range(200):
        sent = client.sendMessage(msg, thread_id=friend.uid) 
    if sent: 
        print("Message sent successfully!") 
    runAgain = input("Want to Send another friend ? Y / N :")
    if runAgain == "N":
        break
    else :
        continue
            

