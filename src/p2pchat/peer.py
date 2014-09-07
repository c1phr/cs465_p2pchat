import socket
from src.p2pchat.Connection_Info import Connection_Info


class peer(object):
    def __init__(self, name):
        self.connection = Connection_Info(socket.gethostbyname(socket.gethostname())) #This should work so long as /etc/hosts isn't overriding
        self.name = name
        self.peer_list = {self.connection.Get_IP(): self.name}

    def Get_List(self):
        return self.peer_list

    def Set_List(self, new_list):
        self.peer_list = new_list

    def Get_Name(self):
        return self.name

    def Set_Name(self, new_name):
        self.name = new_name
        self.peer_list[self.connection.Get_IP()] = new_name #Make sure we update the name in the peer's own dictionary