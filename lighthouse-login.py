import argparse
import socks
import requests
import socket
import os
from bs4 import BeautifulSoup
from modules.check_ip import return_ip
from modules.fetch_input import fetch_input
from colorama import init, Fore, Style

# initialize colorama
init()

# ansi color vars
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN

socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket
parser = argparse.ArgumentParser()
parser.add_argument("-url", help="URL of the website to fetch input names from")
args = parser.parse_args()
return_ip()
print(f"{BLUE}Input Names:{RESET}")
print(fetch_input(args.url))