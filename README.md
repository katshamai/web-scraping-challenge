# Web Scraping Challenge - Mission to Mars

## Background

In this assignment, we built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines the steps undertaken.

### Step 1 - Scraping
My initial scraping was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

The Jupyter Notebook file called is called "mission_to_mars.ipynb" 

### Step 2 - MongoDB and Flask Application
Using MongoDB with Flask templating, we created a HTML page that displays all of the information that was scraped from the URLs above.

We started by converting the Jupyter notebook into a Python script called "scrape_mars.py" with a function called scrape that executes all of the scraping code and return one Python dictionary containing all of the scraped data.


Next, we created a route called "/scrape" that imports the scrape_mars.py script and calls the scrape function.

The return value is stored in Mongo as a Python dictionary.

We created a root route "/" that queries the Mongo database and passes the Mars data into an HTML template to display the data.


We created a template HTML file called "index.html" (stored in the "templates" folder) that takes the Mars data dictionary and displays all of the data in the appropriate HTML elements. 

### Step 3 - Screen shots of final application
Once completed, we took screen shots of our final application in both desktop format and formatted sized for smaller screens. These are stored in the "Images" folder.
