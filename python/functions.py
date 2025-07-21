def add(x,y):
    num1=x+y
    num2=x*y
    return num1+num2

print(add(2,3))    

def login(username, password):
    if username == "admin" and password == "admin123":
        print('Login success')

    else:
        print('Invalid credentials')

uname = input('Enter username: ')
password = input('Enter password: ')
login(uname, password)