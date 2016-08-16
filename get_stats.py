import argparse
from splinter import Browser
from time import sleep
from datetime import date
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description = """Summarize number of episodes
        of This American Life marked as Heard by year""")
parser.add_argument('user', help = "Username for http://wwww.thisamericanlife.org")
parser.add_argument('passwd', help = "User password for http://wwww.thisamericanlife.org")
args = parser.parse_args()

with Browser() as browser:
    slug = "http://www.thisamericanlife.org"
    url = slug + "/user/login"
    browser.visit(url)
    browser.fill('name', args.user)
    browser.fill('pass', args.passwd)
    button = browser.find_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/form/div/div/input[3]').click()

    yearly_pcts = []
    years = range(1995, date.today().year + 1)
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

with open("TAL.csv", "wb") as outfile:
    outfile.write("year,percentage\n")
    for x in yearly_pcts:
        outfile.write("{},{}\n".format(x[0], x[1]))
