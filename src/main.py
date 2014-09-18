import socket, select, json

from Connection_Info import Connection_Info
from Message import Message
from Peer import Peer

def main():
    connected = False
    running = True

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
    print("IP: " + start_info.connection.Get_IP())



    while running:
        #handling all user message inputs + flags
        user_msg = input()

        #Name change
        if user_msg == "/name":
            print("Enter new name:")
            new_name = input()
            start_info.Set_Name(new_name)
            name_msg = Message("N", new_name)
            start_info.Send_Message(name_msg)
            start_info.Send_Chat(name_in + " changed their name to " + new_name)
            print("You've changed your name to: " + new_name)

        #Info about current user
        elif user_msg == "/info":
            print("Name: " + start_info.Get_Name())
            print("IP: " + start_info.connection.Get_IP())
            print("Connected to: ")
            for ip in start_info.Get_List():
                print(start_info.Get_UserName(ip) + " : " + ip)

        #Joining another IP
        elif user_msg == "/join":
            print("Enter a known IP:")
            known_ip = input()
            start_info.Join_Network(known_ip)
            start_info.Set_Connected(True)

        #Leaving the chat
        elif user_msg == "/leave":
            start_info.Leave_Network()
            # disconnect_msg = Message("D", name_in + "has left the chat")
            print("Leaving chat and exiting program...")
            running = False
            return

        #Sending a message when not yet connected to a chat
        elif user_msg and (user_msg != "/join") and (start_info.Get_Connected() is False):
            print("You aren't connected yet")
            user_msg = ""

        #Sending a normal message.
        else:
            start_info.Send_Chat(user_msg)


main()