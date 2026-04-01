import requests 
from bs4 import BeautifulSoup 
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_max" ,help ="Enter the no of pages", type=int)
parser.add_argument("--dbname" ,help ="Enter the no of DATABASE", type=str)
args = parser.parse_args()

dbname = args.dbname
page_max =args.page_max
connect.create(dbname)
url1 = "http://books.toscrape.com/catalogue/page-"
for n in range(1,page_max):
    req = requests.get(url1+ str(n) +".html")

    con = req.content
    sh = BeautifulSoup(con,"html.parser")

    data1 = sh.find_all("li"  ,{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    for k in data1 :
        dict = {}
        dict[name] = k.find("h3").text
        dict[price] = k.find("p",{"class" : "price_color"}).text
        dict[avail] = k.find("p",{"class" : "instock availability"}).text
    connect.insert_datato_db(dbname,tuple(dict.values()))    

connect.get_datafrom_db(dbname)
