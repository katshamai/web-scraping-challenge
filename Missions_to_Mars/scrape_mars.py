# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
from IPython.display import HTML

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

mars_collection={}
def scrape():
    # URL of page to be scraped
    nasa_url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response = requests.get(nasa_url)

    # Create BeautifulSoup object; parse with 'lxml'
    nasa_soup = bs(response.text, 'lxml')

    # Extract title text
    news_title = nasa_soup.find('div',class_='content_title').find('a').text
    mars_collection['news_title']=news_title

    # Extract Paragraph text
    news_paragraph = nasa_soup.find('div', class_="rollover_description_inner").text
    mars_collection['news_paragraph'] = news_paragraph
  
    # # JPL Mars Space Images - Featured Image

    browser = init_browser()
     #Visit Nasa's JPL Mars Space url  using splinter module
    jplNasa_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jplNasa_url)
    #create HTML object
    html = browser.html
    jpl_soup = bs(html, 'html.parser')

    #get base Nasa link
    main_url ='https://www.jpl.nasa.gov'
     #get image url from the soup object.
    featured_image_url = jpl_soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    mars_collection['featured_image_url'] = f"{main_url}{featured_image_url}"

    # # Mars Facts

    # URL for Mars Facts
    facts_url = 'https://space-facts.com/mars/'

    # Use Pandas to parse html
    results = pd.read_html(facts_url)

    # Add parsed data into DataFrame
    mars_df = results[0]
    mars_df.head()

    # Add column names
    mars_df.columns = ['Information', 'Dimensions']
    mars_df.head()

    # Create HTML table from dataframe
    mars_collection['mars_html_table'] = mars_df.to_html(header=True, index=False)

    # # Mars Hemispheres

    # Set up connection to url
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    core_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/'
    browser.visit(hemi_url)
    html = browser.html
    hemi_soup = bs(html,'html.parser')

    # Identify all hemispheres list on page
    hemispheres = hemi_soup.find('div',class_='collapsible results')
    results = hemispheres.find_all('a')

    # Create a list to hold image url string and hemisphere title

    hemispheres_image_urls = []

    # Populate list with the images data

    for result in results:
        if result.h3:
            title = result.h3.text
            link = 'https://astrogeology.usgs.gov' + result['href']
            print(title,link)    
            browser.visit(link)
            image_html = browser.html
            soup = bs(image_html,'html.parser')
            soup_image = soup.find('div', class_='downloads').find('li').a['href']
            print(soup_image)
            mars_images = {'title':title, 'img_url':soup_image}
            hemispheres_image_urls.append(mars_images)

    # Check hemispheres_image_urls dictionary
    mars_collection['hemispheres_image_urls'] = hemispheres_image_urls

    return mars_collection