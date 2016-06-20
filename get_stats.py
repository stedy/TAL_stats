from splinter import Browser

with Browser() as browser:
    slug = "http://www.thisamericanlife.org"
    url = slug + "/user/login"
    browser.visit(url)
    browser.fill('name', 'z11k')
    browser.fill('pass', 'pwd_2012')
    button = browser.find_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/form/div/div/input[3]').click()
    print browser.url

    browser.visit("http://www.thisamericanlife.org/radio-archives#2015")
    print browser.html.encode('utf-8')
