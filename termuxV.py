### !/usr/bin/python3

#CREATED 2023 BY MR,OWLBIRD05
#CODED BY MR,OWLBIRD05
#CREDITS TO INTELLEGENCE CYBER COMMUNITY LEADER
from time import sleep
import os
import sys
import getpass
## 4 Modules

## Pass And User
def masuk():
 os.system("clear")
 print()
 sleep(1)
 print("\033[1;91m             _                ___")
 sleep(0.2)
 print("\033[1;91m            | |    ___   __ _|_ _|_ __")
 sleep(0.2)
 print("\033[1;91m            | |   / _ \ / _` || || '_ \ ")
 sleep(0.2)
 print("\033[1;91m            | |__| (_) | (_| || || | | |")
 sleep(0.2)
 print("\033[1;91m            |_____\___/ \__, |___|_| |_|")
 sleep(0.2)
 print("\033[1;91m                        |___/")
 sleep(0.1)
 print("\033[1;97m ╻ ╻┏━┓┏━╸┏━┓┏┓╻┏━┓┏┳┓┏━╸   ┏━┓┏━┓┏━┓┏━┓╻ ╻┏━┓┏━┓╺┳┓")
 sleep(0.1)
 print("\033[1;97m ┃ ┃┗━┓┣╸ ┣┳┛┃┗┫┣━┫┃┃┃┣╸    ┣━┛┣━┫┗━┓┗━┓┃╻┃┃ ┃┣┳┛ ┃┃")
 sleep(0.1)
 print("\033[1;97m ┗━┛┗━┛┗━╸╹┗╸╹ ╹╹ ╹╹ ╹┗━╸   ╹  ╹ ╹┗━┛┗━┛┗┻┛┗━┛╹┗╸╺┻┛")
 sleep(0.2)
 print("                \033[0m[\033[101mCreated By OwlBird05\033[0m]")
 print()
 print("\033[1;91m[\033[92m!\033[91m]\033[1;97m ----------------------------------------------- \033[1;91m[\033[92m!\033[91m]")
 print()
## Menu
def back():
 sleep(1)
 os.system("clear")
 print()
 os.system("neofetch --ascii_distro NuTyX")
 print("\033[0m            \033[0m[\033[101mCreated 2024 By OwlBird05\033[0m]")
 sleep(0.1)
 print()
 sleep(0.1)
 print("                       \033[0m Menu")
 sleep(0.1)
 print("       \033[91m[\033[92m1\033[91m]\033[0m Install Termux Mod 0.120.0 \033[91m[Not Original]")
 sleep(0.1)
 print("       \033[91m[\033[92m2\033[91m]\033[0m Install Termux 0.119.1     \033[91m[\033[1;96mRecomended\033[91m]")
 sleep(0.1)
 print("       \033[91m[\033[92m3\033[91m]\033[0m Install Termux 0.118.0     \033[91m[No Recomended]")
 sleep(0.1)
 print("       \033[91m[\033[92m4\033[91m]\033[0m Install Termux 0.117       \033[91m[No Recomended]")
 sleep(0.1)
 print("       \033[91m[\033[92m5\033[91m]\033[0m Install Termux 0.116       \033[91m[No Recomended]")
 sleep(0.1)
 print("       \033[91m[\033[92m6\033[91m]\033[0m Install Termux 0.114       \033[91m[No Recomended]")
 sleep(0.1)
 print("\033[1;97m       ----------------------------------------------")
 sleep(0.1)
 print("       \033[91m[\033[92m7\033[91m]\033[0m Install Tools OwlTrack     \033[91m[\033[1;96mVVIP Tools\033[91m]")
 sleep(0.1)
 print("       \033[91m[\033[92m8\033[91m]\033[0m Contact Developer          \033[91m[\033[1;96mDeveloper\033[91m]")
 sleep(0.1)
 print("       \033[91m[\033[92m9\033[91m]\033[0m Exit                       \033[91m[Exit]")
 sleep(0.1)
 print()
 sleep(0.1)
 termux = input("\033[91m[\033[92m>\033[91m]\033[1;96m Chose: ").lower()
 ## Chose 1
 if termux == "1":
  sleep(1)
  os.system("clear")
  os.system("neofetch --ascii_distro chrome")
  print("\033[0m       \033[0m[\033[101mBy OwlBird05\033[0m]")
  sleep(0.1)
  print()
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Installing Termux Version 0.119.1")
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Opened Link To Download")
  sleep(1)
  os.system("xdg-open https://www.mediafire.com/file/gvlanung2ywkloi/TermuxMod%25280.120.0%2529.zip/file?dkey=eixg36at7ib&r=1987")
  sleep(3)
  print()
  out();
 ## Chose 2
 if termux == "2":
  sleep(1)
  os.system("clear")
  os.system("neofetch --ascii_distro chrome")
  print("\033[0m       \033[0m[\033[101mBy OwlBird05\033[0m]")
  sleep(0.1)
  print()
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Installing Termux Version 0.119.1")
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Opened Link To Download")
  sleep(1)
  os.system("xdg-open https://download.apkcombo.com/com.termux/Termux_0.119.1_apkcombo.com.apk?ecp=Y29tLnRlcm11eC8wLjExOS4xLzExOS5lMzNiNGRhMmJiM2M3MTdjOWI1NGM2ZWMwZjI5YmMwZDExN2VmODBhLmFwaw==&iat=1697545509&sig=788b2e196a646484a26e2289ce9c91b9&size=112434858&from=cf&version=latest&lang=id&fp=a321b1dcb5957b0fbc4dd5c986f6dc4c&ip=110.136.216.40")
  sleep(3)
  print()
  out();
 ## Chose 3
 if termux == "3":
  sleep(1)
  os.system("clear")
  os.system("neofetch --ascii_distro chrome")
  print("\033[0m       \033[0m[\033[101mBy OwlBird05\033[0m]")
  sleep(0.1)
  print()
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Installing Termux Version 0.118.0")
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Opened Link To Download")
  sleep(1)
  os.system("xdg-open https://download.apkcombo.com/com.termux/Termux_0.118.0_apkcombo.com.apk?ecp=Y29tLnRlcm11eC8wLjExOC4wLzExOC41MThkOGEwNDliMzFlZTI4ZTBkZjczZTVmYTIxZjM4NmZjNDY4ODg4LmFwaw==&iat=1697548433&sig=2b34f51d3505813de01c28a79f459feb&size=101739523&from=cf&version=old&lang=id&fp=a321b1dcb5957b0fbc4dd5c986f6dc4c&ip=110.136.216.40")
  sleep(3)
  print()
  out();
 ## Chose 4
 if termux == "4":
  sleep(1)
  os.system("clear")
  os.system("neofetch --ascii_distro chrome")
  print("\033[0m       \033[0m[\033[101mBy OwlBird05\033[0m]")
  sleep(0.1)
  print()
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Installing Termux Version 0.117")
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Opened Link To Download")
  sleep(1)
  os.system("xdg-open https://download.apkcombo.com/com.termux/Termux_0.117_apkcombo.com.apk?ecp=Y29tLnRlcm11eC8wLjExNy8xMTcuNDkxZjIwN2UyODlhYzA1YmNiMzljYTQzNmI1MjE4ZjZhZTgwMWRiZC5hcGs=&iat=1697548724&sig=0b3a106fb10c4cc0e4686090d07fe287&size=85749239&from=cf&version=old&lang=id&fp=a321b1dcb5957b0fbc4dd5c986f6dc4c&ip=110.136.216.40")
  sleep(3)
  print()
  out();
 ## Chose 5
 if termux == "5":
  sleep(1)
  os.system("clear")
  os.system("neofetch --ascii_distro chrome")
  print("\033[0m       \033[0m[\033[101mBy OwlBird05\033[0m]")
  sleep(0.1)
  print()
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Installing Termux Version 0.116")
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Opened Link To Download")
  sleep(1)
  os.system("xdg-open https://download.apkcombo.com/com.termux/Termux_0.116_apkcombo.com.apk?ecp=Y29tLnRlcm11eC8wLjExNi8xMTYuNjA5MWI1OTc0NGQwNzA5OWJiY2YzNzc4ODUwZjMwZGZkOGYzZDE2Yi5hcGs=&iat=1697548953&sig=997271f968595334887020e1fc74e02b&size=85732799&from=cf&version=old&lang=id&fp=a321b1dcb5957b0fbc4dd5c986f6dc4c&ip=110.136.216.40")
  sleep(3)
  print()
  out();
 ## Chose 6
 if termux == "6":
  sleep(1)
  os.system("clear")
  os.system("neofetch --ascii_distro chrome")
  print("\033[0m       \033[0m[\033[101mBy OwlBird05\033[0m]")
  sleep(0.1)
  print()
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Installing Termux Version 0.114")
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Opened Link To Download")
  sleep(1)
  os.system("xdg-open https://download.apkcombo.com/com.termux/Termux_0.114_apkcombo.com.apk?ecp=Y29tLnRlcm11eC8wLjExNC8xMTQuYjYxNjFiOWY3ZTdiNDk2ZTE5NDJhNWRmNzk2M2U4MWZjMTk5MDI0Mi5hcGs=&iat=1697549248&sig=ac93d355bbb17d3a322d15e20fd2efad&size=84814921&from=cf&version=old&lang=id&fp=a321b1dcb5957b0fbc4dd5c986f6dc4c&ip=110.136.216.40")
  sleep(3)
  print()
  out();
 ## Chose 7
 if termux == "7":
  sleep(1)
  os.system("clear")
  os.system("neofetch --ascii_distro BSD")
  print("\033[0m       \033[0m[\033[101mBy OwlBird05\033[0m]")
  sleep(0.1)
  print()
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Cloning Github")
  sleep(0.2)
  os.system("cd $HOME && rm -rf OwlTrack && git clone https://github.com/IccTeam/OwlTrack")
  sleep(1)
  print("\033[91m[\033[92m>\033[91m]\033[0m File saved in /data/data/com.termux/files/home/OwlTrack")
  print()
  out();
 ## Chose 8
 if termux == "8":
  sleep(1)
  os.system("clear")
  os.system("neofetch --ascii_distro BSD")
  print("\033[0m       \033[0m[\033[101mBy OwlBird05\033[0m]")
  sleep(0.1)
  print()
  sleep(0.2)
  print("\033[91m[\033[92m>\033[91m]\033[0m Opened WhatsApp")
  sleep(0.2)
  os.system("xdg-open http://wa.me/+6283848301116")
  sleep(1)
  print("\033[91m[\033[92m>\033[91m]\033[0m If you not have WhatsApp you can dm my ig: @iccfficial")
  print()
  out();
## Chose 9
 if termux == "9":
  logout();
 ## KeyboardInterput
 if termux == "":
  print("\033[91m[\033[92m>\033[91m]\033[1;96m KeyboardInterput")
  sleep(0.2)
  logout();
  back();
### Exit
def logout():
 print("\033[0;37\033[91mExiting.....")
 sleep(2)
 print('\033[0;37\033[94m  _    _          _____  _______     __  _____      __     __  ')
 sleep(0.10)
 print('\033[0;37\033[94m | |  | |   /\   |  __ \|  __ \ \   / / |  __ \   /\\ \   / /  ')
 sleep(0.10)
 print('\033[0;37\033[94m | |__| |  /  \  | |__) | |__) \ \_/ /  | |  | | /  \\ \_/ /   ')
 sleep(0.10)
 print('\033[0;37\033[94m |  __  | / /\ \ |  ___/|  ___/ \   /   | |  | |/ /\ \\   /    ')
 sleep(0.10)
 print('\033[0;37\033[94m | |  | |/ ____ \| |    | |      | |    | |__| / ____ \| |     ')
 sleep(0.10)
 print('\033[0;37\033[94m |_|  |_/_/    \_\_|    |_|      |_|    |_____/_/    \_\_|     ')
 sleep(0.30)
 print("")
 sys.exit();
### Exit Menu
def out():
 print("\033[0m       \033[0m[\033[101mBy OwlBird05\033[0m]")
 print("\033[91m      [\033[92m00\033[91m]\033[0;37m Back To Menu")
 print("\033[91m      [\033[92m99\033[91m]\033[0;37m exit tools")
 nember = input("\033[91m[\033[94mUser@localhost\033[91m]\033[0;37m Enter your nember ===>")

 if nember == "99" :
   logout();
 if nember == "00" :
   back();
 out()
### Login Tools
def login():
### Readline File User And Password
    if os.path.exists("./pass_usr.txt") and os.path.getsize("./pass_usr.txt") > 0:
     with open('pass_usr.txt', 'r') as file:
      pass_usr=file.readline().rstrip('\n')
      back();

    else:
     sleep(1)
     print()
     os.system("clear")
     sleep(1)
     print("\033[91m[\033[92m>\033[91m]\033[0m Subscribe My Youtube Channel")
     sleep(1)
     os.system("xdg-open http://www.youtube.com/@iccfficial")
     subs = input("\033[91m[\033[92m>\033[91m]\033[0m Press Enter To Next ")
     sleep(1)
     file = open("pass_usr.txt", "w")
     masuk();
     user = "MrOwlBird05"
     passwd = "Owl05"
     print("\033[91m[\033[92m>\033[91m]\033[0;37m Contact Developer To Get License Key")
     print("\033[91m[\033[92m>\033[91m]\033[0;37m Or You Can DM My Instagram @iccfficial")
     os.system("xdg-open http://wa.me/+6283848301116?text=Give+Me+*License*+Key+==➤+termuxV")
     print()
     sleep(0.8)
     username = input("     🦉 \033[1;37mUsername ===>\033[1;96m ")
     sleep(0.2)
     pass_usr = getpass.getpass(prompt='     🦉 \033[1;37mPassword ===> ')
     if username != user or pass_usr != passwd:
         print("")
         print("     🦉 \033[1;91mPassword or Username Wrong")
         sleep(2)
         login();
     elif username == user and pass_usr == passwd:
         print("")
         print("     🦉 \033[0mWelcome To \033[94m termuxV")
         sleep(1)
         file.write(pass_usr)
         print()
         sleep(0.2)
         print("\033[91m[\033[92m>\033[91m]\033[0m Pass saved in: ./pass_usr.txt")
         sleep(2)
         file.close()
         sleep(1)
         back();
login()
### END
