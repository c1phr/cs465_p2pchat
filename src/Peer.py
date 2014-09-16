import socket, select, json

from src.Connection_Info import Connection_Info
from src.Message import Message


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
                # Make sure we update the name in the peer's own dictionary
                # Send_Message() --> Send a message out to the network to 
                # inform them of the new name

    def Send_Message(self, message):
        """
        -target_peer is the peer to whom the message should be sent.
        """
        #So i did this connection but i might have to meet up with you guys, particularly
        #Andrew to see how we want to handle the peer ips through this message. I saw that
        #Andrew already made a for loop swithin send chat so hopefully these inputs work!

        to_send = message.To_Json() # Serialize the data into JSON so it can
                                        # be sent over the socket


        for target_peer in self.Get_List():
            self.socket_con.connect(target_peer, self.connection.Get_Send_Port()) #connect to particular ip
            self.socket_con.send(to_send)    #send the JSON encoded message
            self.socket_con.close()          #close the socket
      
    def Start_Server(self): #Tory's
        """
        Handle non-blocking socket netcode
        """
        self.connection = Connection_Info(socket.gethostbyname(socket.gethostname()))
        self.socket_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #open socket
        self.socket_con.listen(15) # up to fifteen users can message at once. Can change later
        self.socket_con.setblocking(False) #opens the non blocking channel

    def Listen_Handler(self, data, ip):
        """
        Unpacks data that was recieved from the network and takes appropriate action
        Takes in serialized data and the ip of the sender
        """
        data_dict = json.loads(data) #Deserialize the data back into a Python 
                                     # dictionary
        flag = data_dict["flag"]
        if flag == "J": #Join
            if ip:
                #Body should contain the name of the new user
                self.peer_list[ip] = data_dict["body"]
                update_message = Message("U", self.peer_list) #Create new 
                                # message object to wrap the update message
                self.Send_Message(update_message) #Send an update message out, 
                                    #this will give the new peer the full list

        elif flag == "U": #Update List
            self.peer_list = data_dict["body"] #We want to assume that the new
                                        #list coming down the wire is canonical
        
        elif flag == "M": #Message
            print(data_dict["text_rep"])
        
        elif flag == "N": #Name Change
            self.peer_list[ip] = data_dict["body"]
            
        elif flag == "D": #Disconnect
            del data_dict[ip]
            

    def Join_Network(self, target):
        """
        -Since we're assuming that the IP of an active peer is already known,
        we'll need the IP of that peer to join the network.
        -Assumes that a server has already been started, and should probably 
        error out if not.
        -Sends a message out to the network to make other peers aware of
        presence.
        """
        self.Add_User( target )
        join_request = Message( 'J', format("{target}", target) )
        self.Send_Message( join_request )
        pass

    def Leave_Network(self):
        """
        Send out a message to the network to inform that this peer is
        departing.
        """
        # TODO: We need to decide how this ought to be handled. Had a
        # discussion with Salvatore about whether we should (A) send the
        # leave request to just one peer--whose responsibility it then
        # becomes to inform the rest of the network--or (B) send the leave
        # request to all peers, which puts a lot of pressure on a node that
        # may just want to get out of the network ASAP. However, considering
        # that we're only planning for graceful departure, it's not totally
        # unreasonable to put that burden on the departing party. -AS
        pass

    def Send_Chat(self, message_body):
        """
        -message should be a string when it's passed in.
        -Send a message to each peer, in turn.
        """
        to_send = Message('M', message_body)
        self.Send_Message(to_send)
