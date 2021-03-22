import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


def get_usernames(organization_id):

    users = {}

    my_url = 'https://codeforces.com/ratings/organization/865'
    # headers={'User-Agent': 'Mozilla/5.0'} for avpiding http error
    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    page_html = urlopen(req).read()
    page_soup = soup(page_html, "lxml")
    table = page_soup.findAll('table', {'class': ''})[3]
    rows = table.findAll('tr')

    # parsing
    for row in rows:
        line = []
        for cell in row.findAll(['td']):
            line.append(cell.get_text().strip())
            # print(cell)
        if line:
            #print(line[1], line[3])
            users[line[1]] = line[3]

    #print(users)
    return users


get_usernames(846)
