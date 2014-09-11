import time


class Message(object):
    """
    Messages contain the chat data passed between individual Peers. Through
    the use of flags, they can also indicate other information about
    individual peer state. 

    Possible flags for a message:
     (J) Join Request - request to join the network
     (M) Message - contains a chat message
     (N) Name Change - contains a new display name for the sending peer
     (D) Disconnect - the sending peer is disconnecting from the network
    """
    def __init__(self, flag, body):
        self.flag = flag
        self.body = body
        self.time = time.time()

    def __str__(self):
        timestamp = time.localtime(self.time)[3] + ":" \
                + time.localtime(self.time)[4]
        return timestamp + " --- " + self.body

    def Get_Flag(self):
        return self.flag

    def Get_Body(self):
        return self.body

    def Get_Timestamp(self):
        return self.time
