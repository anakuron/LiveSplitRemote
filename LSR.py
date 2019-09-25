import socket
import sys
import click # install using "pip install click"
import time

ip = "192.168.1.151" # change this value to correct ip
portnumber = 16834 # change this value to the correct port number

print("Trying to connect to \033[1;32;40m")+ip+"\033[0;37;40m"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, portnumber))
print("\033[1;32;40mConnected\033[0;37;40m\r\n")

while True:
    print("t=current time | s=start/split | r=reset | p=pause (c=resume) | q=quit")
    sock.send("getfinaltime\r\n")
    print ("Final Time: ")+sock.recv(1024)
    key = click.getchar()
    if (key == 't'):
        print("\033[1;33;40mCurrent time")
        sock.send("getcurrenttime\r\n")
        print sock.recv(1024)+"\033[0;37;40m"

    elif (key == 's'):
        print("\033[1;32;40mStart/Split !!!\033[0;37;40m")
        sock.send("startorsplit\r\n")

    elif (key == 'p'):
        print("Pause")
        sock.send("pause\r\n")

    elif (key == 'c'):
        print("Resume")
        sock.send("resume\r\n")

    elif (key == 'r'):
        print("\033[1;31;40mReset")
        sock.send("reset\r\n")
        print("\033[0;37;40m")
        
    elif (key == 'q'):
        quit()
