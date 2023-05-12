import argparse
import requests
from bs4 import BeautifulSoup
parser = argparse.ArgumentParser()
parser.add_argument("-url", help="URL of the website to fetch input names from")
args = parser.parse_args()
if not args.url:
    print("Please provide a URL using the -url argument.")
    exit()
response = requests.get(args.url)
soup = BeautifulSoup(response.content, 'html.parser')
input_elements = soup.find_all('input')
input_names = [elem.get('name') for elem in input_elements]
print("Input Names:")
for name in input_names:
    print(name)
