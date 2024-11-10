import requests
import string, json, requests, random
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep
import socket
from discord import SyncWebhook
import time


print(Colorate.Horizontal(Colors.cyan_to_green,"""                                           
   _ _ _     _   _____         _      _____                             
  | | | |___| |_|  |  |___ ___| |_   |   __|___ ___ _____ _____ ___ ___ 
  | | | | -_| . |     | . | . | '_|  |__   | . | .'|     |     | -_|  _|
  |_____|___|___|__|__|___|___|_,_|  |_____|_,_|__,|_|_|_|_|_|_|___|_|  
                                                   |_|      
                          Made by Flacis       
                          Github: flacisReel                             
"""))

print('                                                                      ')
#message, webhook, and delay message
webhook = input(Colorate.Horizontal(Colors.cyan_to_green,'Enter the webhook url ➤ '))
message = input(Colorate.Horizontal(Colors.cyan_to_green,'Enter a message you wanna spam ➤ '))
message_times = int(input(Colorate.Horizontal(Colors.cyan_to_green,'How many times do you wanna spam this message ➤ ')))
delay = int(input(Colorate.Horizontal(Colors.cyan_to_green,'Enter an amount of delay for each message spammed ➤ ')))


system('cls')

if webhook.startswith('https://discord.com/api/webhooks/'): 
        system('cls')
        #prints the message in the console (NOT DISCORD)
        for i in range (message_times):
             time.sleep(0.01) 
             print(Colorate.Horizontal(Colors.cyan_to_green,'[+] Message Sending...\n'))
        
        #sends the message
        for i in range(message_times):
          time.sleep(delay) 
          requests.post(webhook, json={'content': message})  

else:
    print('Sorry but that webhook is invalid.')

input()