class server:
    #object initilization
    #member variables serverId,name,ip,status,memory_usage
    def __init__(self,serverID,name,IP_address):
        self.serverID=serverID
        self.name=name
        self.IP_address=IP_address
        self.status="offline"
        self.memory_uasage=0

    #methods
    def ping(self):
        return f"pinging {self.IP_address}...."
    def getstatus(self):
        return f"{self.name} status is {self.status}"
    def updatestatus(self):
        if self.status=="offline":
           self.status= "online"
        else:
           self.status= "offline"
web_server1 = server("SI1226626267","Web_server1","192.168.1.10")
print(web_server1.ping())
web_server2 = server("SI1226678099","Web_server2","192.168.1.11")
print(web_server2.ping())
print(web_server1.getstatus())
web_server1.updatestatus()
print(web_server1.getstatus())

#server is a class
#create 4 object web1,web2,web3,web4 .They have there own memory
#ip,name,memory,status
#self means object itself
#