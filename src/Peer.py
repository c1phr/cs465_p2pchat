import socket, select, json

from src.Connection_Info import Connection_Info


class peer(object):
    def __init__(self, name):
        self.connection = \
                Connection_Info(socket.gethostbyname(socket.gethostname()))
                #This should work so long as /etc/hosts isn't overriding
        self.name = name
        self.peer_list = {self.connection.Get_IP(): self.name}
        self.Join_Network()

    def Get_List(self):
        return self.peer_list

    def Set_List(self, new_list):
        self.peer_list = new_list

    def Add_User(self, name, ip):
        self.peer_list[ip] = name

    def Remove_User(self, ip):
        del self.peer_list[ip]

    def Get_Name(self):
        return self.name

    def Set_Name(self, new_name):
        self.name = new_name
        self.peer_list[self.connection.Get_IP()] = new_name \
                #Make sure we update the name in the peer's own dictionary
        #Send_Message() --> Send a message out to the network to inform them of the new name

    def Send_Message(self, message):
        to_send = message.To_Json() #Serialize the data into JSON so it can be sent over the socket
        pass
      
    def Start_Server(self): #Tory, this one's all you if you want
        """
        Handle non-blocking socket netcode
        """
        pass

    def Listen_Handler(self, data):
        """
        Unpacks data that was recieved from the network and takes appropriate action
        """
        data_dict = json.loads(data) #Deserialize the data back into a Python dictionary
        flag = data_dict["flag"]
        if flag == "J":
            #Join flag
        
        elif flag == "M":
            print(data_dict["text_rep"]
        
        elif flag == "N":
            #Name change
            
        elif flag == "D":
            #Disconnect
            

    def Join_Network(self):
        """
        Assumes that a server has already been started, and should probably error out if not.
        Sends a message out to the network to make other peers aware of presence.
        """
        pass

    def Leave_Network(self):
        """
        Send out a message to the network to inform that this peer is departing.
        """
        pass

    def Send_Chat(self):
        pass