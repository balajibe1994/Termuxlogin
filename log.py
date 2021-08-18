from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
          # print('\033[1;36;40m')
           print('')
           os.system('date | lolcat')
           print("\033[1;93m")
           print(" \033[1;92m  <----- I AM THE BEST ----->")
           print("\033[1;93m")
           print("")
           print("")
           try:
               x = "Balaji"
               print('\033[1;92mUsername  \033[1;93m: {0} '.format(x))
               e = getpass('\033[1;92mPassword \033[1;93m: ')
               print ("")
               if e=="bala":
                   print('wait...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   #os.system('toilet -f standard'+x+' -F gay')
                   #print('\033[1;92m ────────────────────────────────────── ')
                   print("")
                   break
               else:
                   print("")
                   print("")
                   print("")
                   print("")
                   print("\033[1;91m     Wrong Password")
                   time.sleep(2)
                   print("")
           except Exception:

               print("")
               print("")
               print("")
               print("")
               print("")
               print("\033[1;91m     Wrong Password")
               time.sleep(2)
           except KeyboardInterrupt:
               print("")
               os.system('killall -9 com.termux')
               print("")
               print("")
               print("")
               print("")
               print("\033[1;91m     Wrong Password")
               time.sleep(2)

menu()
