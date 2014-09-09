import time


class Message(object):
    def __init__(self, flag, body):
        self.flag = flag
        self.body = body
        self.time = time.time()

    def __str__(self):
        timestamp = time.localtime(self.time)[3] + ":" + time.localtime(self.time)[4]
        return timestamp + " --- " + self.body

    def Get_Flag(self):
        return self.flag

    def Get_Body(self):
        return self.body

    def Get_Timestamp(self):
        return self.time