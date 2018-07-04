from bs4 import BeautifulSoup
import urllib2
import pandas as pd

def scrape(site, lang_name):
        filename = "data/terms_1_to_100/" + lang_name + ".csv"
        page = urllib2.urlopen(site)
        table = pd.io.html.read_html(page)[0]

        table.to_csv(filename, index=False, header=False, encoding="utf-8") 

if __name__ == "__main__":
	scrape("http://www.sf.airnet.ne.jp/ts/language/number/english.html", "english")
