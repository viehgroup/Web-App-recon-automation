#!/usr/bin/env python

# modules in standard library

import sys
import os

# Check if we are running this on windows platform
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white

def no_color():
    global G, Y, B, R, W
    G = Y = B = R = W = ''


def banner():
    print("""%s
 __      _______ ______ _    _ _______ _____ _     __ 
 \ \    / /_   _|  ____| |  | |__   __/ ____| |   /_ |
  \ \  / /  | | | |__  | |__| |  | | | |    | |    | |
   \ \/ /   | | |  __| |  __  |  | | | |    | |    | |
    \  /   _| |_| |____| |  | |  | | | |____| |____| |
     \/   |_____|______|_|  |_|  |_|  \_____|______|_|
                                                      
                                                      %s%s
                # Coded By VIEHTCI-BATCH-01
    """ % (R, W, Y))
    
    
banner()

#print("Please Enter the wordlist location, you can find in this code, where i have added comments")

print("Enter the location where you want to store it !!")
path = input("Enter the absolute path to store your informtation, so you can access it -> ")
domain = input("Enter the domain you want you gather the information : ")

absolute_path = f'{path}/{domain}'

creating_folder = f'mkdir {absolute_path}'


os.system(f'{creating_folder}')

print("\n")

print("*********************************")
print("\t Subdomain Enumeration \t")
print("*********************************")
print("\n")


# Subdomain Enumeration and checking for Live domains

command1 = f'subfinder -d {domain} -silent | tee {absolute_path}/sub1.txt'

os.system(f'{command1}')

command2 = f"assetfinder {domain} | tee -a {absolute_path}/sub1.txt"
os.system(f"{command2}")


command4 = f"cat {absolute_path}/sub1.txt | httpx -mc 200,302,403 -silent | tee {absolute_path}/live_subs.txt"
os.system(f"{command4}")

command5 = f"rm -rf {absolute_path}/sub1.txt"
os.system(f"{command5}")


print("*********************************")
print("\t Fuzzing for the Virtual Host \t")
print("*********************************")
print("\n")

# Enter  your wordlist location, edit this before run this tool.

command11 = f'cat {absolute_path}/live_subs.txt | while read -r url; do ffuf -w wordlist.txt -u $url -H "Host: FUZZ" -fr "error" -t 100 | tee {absolute_path}/vhost.txt ; done;'
os.system(f"{command11}")

print("*********************************")
print("\t URL Enumeration \t")
print("*********************************")
print("\n")

command6= f"cat {absolute_path}/live_subs.txt | waybackurls | tee {absolute_path}/urls1.txt"

os.system(f"{command6}")

command7 = f"cat {absolute_path}/live_subs.txt | gau | tee -a {absolute_path}/urls1.txt"

os.system(f"{command7}")


print("*********************************")
print("\t Directory-Brute Forcing \t")
print("*********************************")
print("\n")

# Enter  your wordlist location, edit this before run this tool.

command10 = f'cat {absolute_path}/live_subs.txt | while read -r url; do ffuf -w dicc.txt -u $url/FUZZ -mc 200,302,403 -t 100 | tee {absolute_path}/directory_fuzzed.txt; done;'

os.system(f"{command10}")

print("*********************************") 
print("\t Parameter Fuzzing \t")
print("*********************************")
print("\n")

# Enter  your wordlist location, edit this before run this tool.

command12 = f'cat {absolute_path}/live_subs.txt | while read -r url; do ffuf -w parameters.txt -u $url/?FUZZ=test_value -mc 200,302 -t 100 | tee {absolute_path}/parameters_fuzzed.txt; done;'

os.system(f"{command12}")



print("*********************************")
print("\t Thanks for Using \t")
print("*********************************")
print("\n")











