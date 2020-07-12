from bs4 import BeautifulSoup
import os
import requests
import sys


def parser(url, title):
    print("Downloading volume page...")
    req = requests.get("http://drr.land.gov.bd"+url)
    main_soup = BeautifulSoup(req.content, 'html.parser')
    anchors = main_soup.find_all("a", class_="kno")
    links = ["http://drr.land.gov.bd"+a['href'] for a in anchors]
    tables = []
    page_count = len(links)
    i = 1

    print(f"There are {page_count} pages.\nDownloading {title} files...")

    for link in links:
        req = requests.get(link)
        page_soup = BeautifulSoup(req.content, 'html.parser')
        tables = tables + [str(tbl) for tbl in page_soup.find_all("table")]
        print(f"{i}/{page_count} pages of {title} complete!")
        i = i + 1

    print("\nParsing complete!\nSaving to file...")

    endl = "\n"
    str_tbl = endl.join(tables)
    b_tables = BeautifulSoup(str_tbl, 'html.parser').prettify()

    with open("./Final2/"+title+".html", "w") as f:
        f.write(b_tables)


print("Downloading main page...")
url = "http://drr.land.gov.bd/vrr/upozila/292?page=5"
req = requests.get(url)
main_soup = BeautifulSoup(req.content, 'html.parser')
index = [2]
rows = [main_soup.find_all("tr")[row] for row in index]
row_count = len(rows)
print(f"There are {row_count} rows")

for row in rows:
    data = row.find_all("td")
    title = str(data[1].string).strip()
    print(f"Starting process for {title}...")
    cs = data[2].a['href']
    sa = data[3].a['href']
    rs = data[4].a['href']
    parser(cs, title+" CS")
    parser(sa, title+" SA")
    parser(rs, title+" RS")
    print(f"{title} done!")

print("All done!")
