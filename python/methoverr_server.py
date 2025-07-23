class server:
    def __init__(self,name):
        self.name = name

    def start(self):
         return f"{self.name} is starting..."
    def deploy(self):
         return "Deploying web app using parent method"



class Webserver(server):
    def deploy(self):
         return f"Deploying web app using child method"
         #child is ovveriding the parent method


ws = Webserver("Webserver01") 
print(ws.start())
print(ws.deploy())
