import argparse
import socks
import requests
import socket
import os
from bs4 import BeautifulSoup
# ansi color vars
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

parser = argparse.ArgumentParser()
parser.add_argument("-url", help="URL of the website to fetch input names from")
args = parser.parse_args()

# Get the IP address of the user
ip_address = requests.get('https://api.ipify.org').text
print(f"{BOLD}Your IP Address:{RESET} {ip_address}\n")
if not args.url:
    print("Please provide a URL using the -url argument.")
    exit()

response = requests.get(args.url)
soup = BeautifulSoup(response.content, 'html.parser')
input_elements = soup.find_all('input')
input_names = [elem.get('name') for elem in input_elements]

print(f"{BOLD}Input Names:{RESET}")
for name in input_names:
    print(name)
