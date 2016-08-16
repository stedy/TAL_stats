from splinter import Browser
from time import sleep
from datetime import date
from bs4 import BeautifulSoup
import os


with Browser() as browser:
    slug = "http://www.thisamericanlife.org"
    url = slug + "/user/login"
    browser.visit(url)
    browser.fill('name', 'z11k')
    browser.fill('pass', 'pwd_2012')
    button = browser.find_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/form/div/div/input[3]').click()

    yearly_pcts = []
    years = range(2015, date.today().year + 1)
    for year in years:
        episode_count, heard_count = 0, 0

        browser.visit(slug + "/radio-archives/" + str(year))
        sleep(20)
        year_results = browser.html
        soup = BeautifulSoup(year_results)
        heard_episodes = soup.find_all('a', {'class': 'flag unflag-action flag-link-toggle flag-processed'})
        for h in heard_episodes:
            heard_count += 1
        total_episodes = soup.find_all('a', {'class': 'image'})
        for te in total_episodes:
            episode_count += 1
        yearly_pcts.append((year, float(heard_count)/episode_count))
    print yearly_pcts

with open("results.txt", "wb") as outfile:
    for x in yearly_pcts:
        outfile.write("{},{}\n".format(x[0], x[1]))

    #then view file
    #browser.visit("file:///" + os.getcwd() + "/index.html")
