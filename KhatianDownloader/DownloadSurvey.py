from bs4 import BeautifulSoup
import os
import requests
import sys

if len(sys.argv) != 3:
    print("Please set correct args!")
    sys.exit()

print("Downloading volume page...")

req = requests.get(sys.argv[1])
main_soup = BeautifulSoup(req.content, 'html.parser')
anchors = main_soup.find_all("a", class_="kno")
links = ["http://drr.land.gov.bd"+a['href'] for a in anchors]
tables = []
page_count = len(links)
i = 1

print(f"There are {page_count} pages.\nStarting main process...")

for link in links:
    req = requests.get(link)
    page_soup = BeautifulSoup(req.content, 'html.parser')
    tables = tables + [str(tbl) for tbl in page_soup.find_all("table")]
    print(f"{i} out of {page_count} pages complete!")
    i = i + 1

print("Parsing complete!\nSaving to file...")

endl = "\n"
str_tbl = endl.join(tables)
b_tables = BeautifulSoup(str_tbl).prettify()

with open("./Final/"+sys.argv[2]+".html", "w") as f:
    f.write(b_tables)


# files = os.listdir("./pages")
# tables = []

# for file in files:
#     with open("./pages/"+file) as f:
#         soup = BeautifulSoup(f)
#     tables = tables + [str(tbl) for tbl in soup.find_all("table")]

# endl = "\n"
# str_tbl = endl.join(tables)
# b_tables = BeautifulSoup(str_tbl).prettify()

# with open("./out.html", "w") as f:
#     f.write(b_tables)
