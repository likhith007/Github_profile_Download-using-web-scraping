from bs4 import BeautifulSoup
import requests

print("Please give github username to fetch profile image")

username = input()

html_page = requests.get('https://github.com/'+username)

soup = BeautifulSoup(html_page.content, 'html.parser')

# print(soup)

profileImage = soup.find('img', class_="avatar avatar-user width-full border color-bg-primary")

print(profileImage['src'])

response = requests.get(profileImage['src'])

file = open(username+".png", "wb")
file.write(response.content)
file.close()