from bs4 import BeautifulSoup
# use pip install requests beautifulsoup4 pandas
import requests
import pandas as pd
import re

#best cafes in Kathmandu
url = 'https://www.holidify.com/pages/cafes-in-kathmandu-1311.html'
response = requests.get(url)
data = []
soup = BeautifulSoup(response.content, "html.parser")

light_gallery = soup.find('div', id='lightgalleryFlexpage')
if light_gallery:
    h2_tags = light_gallery.find_all('h2')
    
    # Print the text content of each <h2> tag
    for tag in h2_tags:
        text = tag.get_text(strip=True)
        cleaned_text = re.sub(r'^\d+\.\s*', '', text)
        print(cleaned_text)
else:
    print("No <div> with id 'lightgallery' found.")
