from socket import*
import os

host = "192.168.0.104"
port = 9999

s = socket(AF_INET, SOCK_STREAM)

s.bind((host, port))

s.listen(5)
while True:
    c,addr = s.accept()

    type = c.recv(1024).decode('utf-8')
    if(type == "s"):
        os.system("shutdown")
    elif(type == "r"):
        os.system("restart")
    elif(type == "m"):
        os.system("gle.mp3")
