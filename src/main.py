import socket, select, json

from Connection_Info import Connection_Info
from Message import Message
from Peer import Peer

def main():
    connected = False

    print("Welcome to Python P2P Chat\n\n"

        #USER HELP INFO
          "Flags:\n"
          "/name               change your username\n"
          "/info               displays your user information\n"
          "/leave              disconnect and leave the chat\n"
          "/join               enter IP of known user\n"
          )

    #Setting initial username for chat
    print("What would you like your name to be?")
    print("Name: ")
    name_in = input()
    start_info = Peer(name_in)
    print("Welcome " + str(name_in) + "!")


    #handling all user message inputs + flags
    user_msg = input()
    while user_msg:

        #ERROR HERE - EXITS AFTER NAME CHANGE
        #Name change
        if user_msg == "/name":
            print("Enter new name:")
            new_name = input()
            old_name = name_in
            name_in =  new_name
            n_msg = Message("N", old_name + " changed names to " + name_in)

        #Joining another IP
        elif user_msg == "/join":
            print("Enter a known IP:")
            known_ip = input()
            join_mes = Message("J", "Joined chat successfully")
            connected = True

        #leaving the chat
        elif user_msg == "/leave":
            disconnect_msg = Message("D", name_in + "has left the chat")
            print("Leaving chat and exiting program...")
            connected = False
            return

        #ERROR HERE - EXITS AFTER PRINT
        #Sending a message when not yet connected to a chat
        elif user_msg and (user_msg != "/join") and (connected is False):
            print("You aren't connected yet")

        #Sending a normal message.
        else:
            reg_msg = Message("M", user_msg)

        return



main()