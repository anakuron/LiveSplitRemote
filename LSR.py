import socket
import sys
import click # pip install click
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.3.120', 16834))

#print("t=current time s=start/split r=reset p=pause q=quit")

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
