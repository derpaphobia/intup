from bs4 import BeautifulSoup
from termcolor import colored
import requests

def formating(item,color):
	print('\n\t' + '#' * 31)
	print('\t' + colored(item, color))
	print('\t' + '#' * 31 + '\n')

URL = 'https://integrity.st'
content = requests.get(URL)

soup = BeautifulSoup(content.text, 'html.parser')

noConnect = soup.find('span', {"class" : "integrityno"})
connect = soup.find('i', {"class" : "integrityyes"})
text = ''

if noConnect:
	text = 'INTE ANSLUTEN VIA INTEGRITY-VPN'.center(31)
	formating(text, 'red')
elif connect:
	text = 'ANSLUTEN VIA INTEGRITY-VPN'.center(31)
	formating(text, 'green')
