import socks
import requests,socket
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

def return_ip():
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
    socket.socket = socks.socksocket
    ip_address = requests.get('https://api.ipify.org').text
    print(f"{RED}Your IP Address:{RESET} {ip_address}\n")