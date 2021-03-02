import random #import random library

#create list: user possibil say to bots, menssion few words
hellow = ["hi","hello", "is anyone there", "good day", "hello there"]

#create loop for continue program works.
while True:
    a = input("User Said...") #get input from user
    if a.lower() in hellow: # condition and convert command into lower case
        botans = ["Hello !", "Hi", "Hi There", "Welcome"] #bots get answer in this list for user
        print('Bots Said - '+random.choice(botans)+'\n') #bots generate random answer on screen
