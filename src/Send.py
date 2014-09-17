import Peer, socket

myself = Peer.Peer("Tory")

tru = True

def send(s):
    myself.socket_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #open socket
    myself.socket_con.connect(("10.0.1.4", myself.connection.Get_Listen_Port())) #connect to particular ip
    myself.socket_con.send(s.encode())    #send the JSON encoded message

while tru:
    s = input("Message: ")
    if s == "e":
        myself.socket_con.close()          #close the socket
        tru = False
    else:
        send(s)