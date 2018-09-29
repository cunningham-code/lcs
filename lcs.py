
from time import sleep
from selenium import webdriver
import getpass

user = input("Username: ")
pswd = getpass.getpass('Password: ')
# you can replace these prompts with hard coded variables

browser = webdriver.Firefox(executable_path="[REPLACE THIS WITH YOUR PATH]")
browser.get('https://coursesite.lehigh.edu/auth/saml/login.php?errorcode=4')

# sign in code
browser.find_elements_by_xpath("//*[contains(text(), 'Log in with Lehigh account')]")[0].click()
u = browser.find_element_by_id("username")
u.send_keys(user)
p = browser.find_element_by_id("password")
p.send_keys(pswd)
p.submit()

sleep(3)
elms = browser.find_elements_by_xpath('//*[@class=\'type_unknown depth_3 contains_branch\']')

felms = []
# This code makes sure to not open administrative courses
for el in elms:
    # print(el.get_attribute('innerHTML'))
    if("Administrative Courses" not in el.get_attribute('innerHTML')):
        felms.append(el)

links = []
for f in felms:
    children = f.find_elements_by_css_selector("*")
    for c in children:
       
        if(c.get_attribute('href') != None):
            links.append(c.get_attribute('href'))

for l in links:
    browser.execute_script('window.open(\'' + l + '\')')