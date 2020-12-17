from selenium import webdriver

url = 'http://127.0.0.1:5000/'
browser = webdriver.Firefox()
browser.get(url)

browser.find_element_by_xpath(
    '/html/body/div/div/a').click()

browser.find_element_by_xpath(
    '/html/body/div/div[1]/div[1]/a[2]').click()
