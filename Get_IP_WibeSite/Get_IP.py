# create by the ghost

import os
import sys
import socket
import platform

g = '\033[1;32m' 
r = '\033[1;31m' 
y = '\033[1;33m' 
b = '\033[1;36m' 
c = '\033[1;30m' 
w = '\033[1;37m' 

def logo():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print(g,'''

    ░██████╗░███████╗████████╗  ██╗██████╗░  ░██╗░░░░░░░██╗░██████╗
    ██╔════╝░██╔════╝╚══██╔══╝  ██║██╔══██╗  ░██║░░██╗░░██║██╔════╝
    ██║░░██╗░█████╗░░░░░██║░░░  ██║██████╔╝  ░╚██╗████╗██╔╝╚█████╗░
    ██║░░╚██╗██╔══╝░░░░░██║░░░  ██║██╔═══╝░  ░░████╔═████║░░╚═══██╗
    ╚██████╔╝███████╗░░░██║░░░  ██║██║░░░░░  ░░╚██╔╝░╚██╔╝░██████╔╝
    ░╚═════╝░╚══════╝░░░╚═╝░░░  ╚═╝╚═╝░░░░░  ░░░╚═╝░░░╚═╝░░╚═════╝░

              ======================================
              |            *THE GHOST*             |
              ======================================
    ''')
    print(y,"\n >> Get IP For Any WebSite.")
    print(y,"\n >> Enter Your Website Like This: www.example.com")
    print(y,"\n >> Press 'q' To exit.\n")

def get_ip():
    logo()
    dns = input(f"{w} >> Enter your website: ")
    if dns == " " or dns == "":
        get_ip()
    elif dns == "q" or dns == "e":
        sys.exit()
    else:
        IP = socket.gethostbyname(dns)
        print (f"\n Host Name Is: {dns} \n  \n IP: {IP} \n")
get_ip()
