from os import system, name
import sys
import time
import base64
import random
from colorama import Fore, Style, init
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

init()

passwords = {
  "gold": "",
  "titanium": "",
  "pearl": ""
}

class Lock:
  def __init__(self, token, open):
    self.token = token
    self.open = open

gold_lock = Lock(b'gAAAAABiG-Jdfd8KUH4i48ES3HVfekGZ8u4dqsMjetpT93AdyNwD6gUGrss-qV5rPKlAVrEhuzQa7CUGtFHrpb7kaJrqscQjzQ==', False)

titanium_lock = Lock(b'gAAAAABiG-Kmz3ezej1P-89qWroNKEBMfJGg8mfCK7tdqw8x0MuDPTynUOp1entY5_M-jPYCNXIaKSN0EJLVKVoija_HF5P2Xg==', False)

pearl_lock = Lock(b'gAAAAABiG-GG0EeYaty7iZXhNpTnOxun87PGzbxw0UI64c5TsOu4pgb97QQqkBzMoxhJPGxkNXPUvmYKrbTKlD1KdjFwF5x7TA==', False)

ttm_token = b'gAAAAABiHCaclTUIuCGWDp-cy7euvbpvZgqlaqftnniiQGtc8rQib-GBnEjL5jm7mK2-s6xYS-OFgQCFESpK8mRvpo17POh1Eg=='
ttm_found = False

def clear():
  time.sleep(1)
  cont = input("Press enter to continue. ")
  _ = system('clear')

def opened():
  if (passwords['gold'] == "" or passwords['titanium'] == "" or passwords['pearl'] == ""):
    death()
    return
  lines = ["The ground rumbles underneath you...\n", "And the treasure chest pops open.\n", "Congratulations, you've won...\n", "Absolutely nothing!\n\n", "There's nothing in the treasure chest...", "except for another slip of paper.", f"On it, is written: {decrypt(b'gAAAAABiHDGxb76n3_VyXmMMt7uq5KC5Jhy7zoj2-9GUoCXdTJkGAkyettQ7pSGQRitbJubdraKMLsB_M7wS7M7GzQ9GVTqx6T-YlTBZ8AtPh3-po9c3leQ=', 'POGPOGPOGPOGPOG').decode('utf-8')}"]
  for line in lines:
    letters = list(line)
    for letter in letters:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(0.05)
    print()
    time.sleep(3)
    
  sys.exit(f"{Fore.RED}{Style.BRIGHT}Good luck.\n\n")
  return

def death():
# try me
  print("LMAO you tried to brute force.\nI applaud your efforts, but I'm going to kill you.\nAs punishment, you have to start over.")
  sys.exit(f"{Fore.RED}Get rolled kid")
  
def treasure_chest():
  global ttm_token
  global ttm_found

  while True:
    if (gold_lock.open and titanium_lock.open and pearl_lock.open):
      opened()
      break
      return
    
    decision = input((f"What would you like to do? \n-=-=-=-=-=-=-\n{Fore.GREEN}1) Open a lock! (o){Fore.YELLOW}\n2) Search the area. (s)\n{Fore.RED}3) Shake the treasure chest in frustration! (f){Style.RESET_ALL}\n")).strip().lower()

    if (decision == "o"):
      while True:
        lock = input(f"Which lock would you like to unlock? \n{Fore.YELLOW}1) Gold Lock (g)\n{Fore.BLUE}2) Titanium Lock (t)\n{Fore.WHITE}3) Pearl Lock (p)\n\n{Fore.RED}4) Back (b)\n{Style.RESET_ALL}").strip().lower()
        if (lock == "g"):
          if (gold_lock.open):
            if (passwords['gold'] == ""):
              death()
            else:
              print(f"You have already opened the {Fore.YELLOW}Gold Lock.{Style.RESET_ALL}\nThe password is {Fore.GREEN}{passwords['gold']}{Style.RESET_ALL}")
            break
          response = decrypt(gold_lock.token, str(input('Enter a password. ')))
          if response is not None:
            response = response.decode('utf-8')
            gold_lock.open = True
            passwords['gold'] = response
            print(f"With a click, the lock opens,\nvanishing in a spectactular cloud of dust before it hits the ground.\nYou hear the following letters in your head: {Fore.GREEN}{response}{Style.RESET_ALL}")
            clear()
          break
        elif (lock == "t"):
          if (titanium_lock.open):
            if (passwords['titanium'] == ""):
              death()
            else:
              print(f"You have already opened the {Fore.BLUE}Titanium Lock.{Style.RESET_ALL}\nThe password is {Fore.GREEN}{passwords['titanium']}{Style.RESET_ALL}")
            break
          response = decrypt(titanium_lock.token, str(input('Enter a password. ')))
          if response is not None:
            response = response.decode('utf-8')
            titanium_lock.open = True
            passwords['titanium'] = response
            print(f"With a crack, the lock breaks,\ntumbling to the ground.\nYou hear the following letters in your head: {Fore.GREEN}{response}{Style.RESET_ALL}")
            clear()
          break
        elif (lock == "p"):
          if (pearl_lock.open):
            if (passwords['pearl'] == ""):
              death()
            else:
              print(f"You have already opened the {Fore.WHITE}Pearl Lock.{Style.RESET_ALL}\nThe password is {Fore.GREEN}{passwords['pearl']}{Style.RESET_ALL}")
            break
          response = decrypt(pearl_lock.token, str(input('Enter a password. ')))
          if response is not None:
            response = response.decode('utf-8')
            pearl_lock.open = True
            passwords['pearl'] = response
            print(f"The lock explodes, sending shards of metal\nflying at you. However, they pass right through you.\nThankfully, you're unharmed.\nYou hear the following letters in your head: {Fore.GREEN}{response}{Style.RESET_ALL}")
            clear()
          break
        elif (lock == "b"):
          break
        else:
          print(f"{Fore.RED}{Style.BRIGHT}That's not an option. Please enter \"g\", \"t\", or \"p\"{Style.RESET_ALL}")
      treasure_chest()
    elif (decision == "s"):
      x = 10
      num = random.randint(1, x)
      if (num == ((9 * 2) / 3) % 5 and not ttm_found):
        if (x == 1):
          print("That was smart.\n")
          time.sleep(2)
        ttm_found = True
        print(f"While searching on the ground, you find a piece of blue paper.\nThere's faint letters written on it: {decrypt(ttm_token, 'WOWTHATSCOOL').decode('utf-8')}")
        time.sleep(5)
      elif (ttm_found):
        print(f"There's nothing else. The piece of paper you found reads: {decrypt(ttm_token, 'WOWTHATSCOOL').decode('utf-8')}")
        clear()
      else:
        responses = ["You find nothing...", "There's nothing on the ground.", "Well, that tree looked cool, but there's nothing here.", "You glance around, but find nothing."]
        print(random.choice(responses))
        clear()
    elif (decision == "f"):
      print(f"{Fore.RED}{Style.DIM}Your efforts are futile. {Style.RESET_ALL}")
      clear()
    else:
      print(f"{Fore.RED}{Style.BRIGHT}Invalid Input. Try again.{Style.RESET_ALL}")
  clear()
      
  
def decrypt(token, pwd):
  kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=b"m\xea\x8c\x10T\xd1\xa8\xb7%8\xf3\xe4\x89\xccP;",
      iterations=1000,
  )
  
  key = base64.urlsafe_b64encode(kdf.derive(pwd.encode('utf-8')))
  print(key)
  f = Fernet(key)
  try:
    return (f.decrypt(token))
  except Exception:
    print("Your password was wrong. Please try again.")
    clear()
    treasure_chest()

print(f"Wow, you found a treasure chest!\nUnfortunately, it's {Fore.RED}locked{Style.RESET_ALL} with three durable locks.")

treasure_chest()