class Dog:
   def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        self.is_sleeping = False

   def bark(self):
        return "wooh!"

   def sleep(self):
        self.is_sleeping = True
        return f"{self.name} is sleeping"

   def wakeup(self):
        self.is_sleeping = False
        return f"{self.name} is now awake"


my_dog = Dog("Buddy","Pom")
your_dog = Dog("Lucy","German Sephard")

print(f"{my_dog.name} is a {my_dog.breed}")
print(your_dog.bark())
print(my_dog.sleep())
print(my_dog.wakeup())


