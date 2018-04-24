from bs4 import BeautifulSoup
import requests
URL = 'https://genius.com/Kanye-west-mercy-lyrics'
page = requests.get(URL)    
html = BeautifulSoup(page.text, "html.parser") # Extract the page's HTML as a string

# Scrape the song lyrics from the HTML
lyrics = html.find("div", class_="lyrics").get_text().encode('ascii','ignore')
reader = open("data/kanye/extra.txt", "w")
reader.writelines(str(lyrics))
reader.close()
