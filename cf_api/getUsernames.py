  
import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from flask_restful import Resource
import json


def get_usernames(organization_id):

    users = {}

    # my_url = 'https://codeforces.com/ratings/organization/'
    # my_url += str(organization_id)
    # headers={'User-Agent': 'Mozilla/5.0'} #for avpiding http error
    # req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    # page_html = urlopen(req).read()
    # print(my_url)
    y = open("41.txt", "r")
    page_html = y.read()
    x = open("temp.txt", "w")
    # x.write(page_html)
    x.close()
    page_soup = soup(page_html, "lxml")
    rows = page_soup.find('div', {'class': 'ratingsDatatable'}).find('table').findAll('tr')
    
    # parsing
    for row in rows:
        line = []
        for cell in row.findAll(['td']):
            line.append(cell.get_text().strip())
            # print(cell)
        if line:
            # print(line)
            #print(line[1], line[3])
            users[line[1]] = line[3]

    #print(users)
    return users

