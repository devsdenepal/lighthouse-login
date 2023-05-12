import socks
import requests
import socket
import os
from bs4 import BeautifulSoup
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
def fetch_input(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    input_elements = soup.find_all('input')
    input_names = [(elem.get('name'), elem.get('type')) for elem in input_elements if elem.get('type') in ['text', 'password']]
    return input_names
