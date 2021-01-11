from bs4 import BeautifulSoup as soup  # The following is the HTML data structure
from urllib.request import urlopen as uReq  # The following is the Web client


# In the following example we will scrape season, fg3%, 3pt attempts, 3pt makes
page_url = "https://www.basketball-reference.com/leagues/NBA_stats_per_game.html"
uClient = uReq(page_url)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the store page
seasons = page_soup.findAll("td", {"data-stat": "season"})
makes = page_soup.findAll("td", {"data-stat": "fg3_per_g"})
attempts = page_soup.findAll("td", {"data-stat": "fg3a_per_g"})
percentages = page_soup.findAll("td", {"data-stat": "fg3_pct"})




# output file to write to local disk
headers = "Season, 3P Makes, 3P Attempts, 3P% \n"
out_filename = "3pt_data.csv"

f = open(out_filename, "w")
f.write(headers)

for i in range(0,1000): 
    try:
        a = str(seasons[i].text)   
    except IndexError:
        break     
    print("Season: " + a) 

    b = str(makes[i].text) 
    print("3P Makes: " + b)

    c = str(attempts[i].text)
    print("3P Attempts: " + c)

    d = str(percentages[i].text)
    print("3P%: " + d + "\n")
        
    f.write(a + ", " + b + ", " + c + ", " + d + "\n")

f.close() 
