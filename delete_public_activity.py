#! /usr/local/bin/python3
import time
from selenium import webdriver

fb_username = 'username-from-url'
email = 'email'
pw = 'pass'

fb_domain = 'https://m.facebook.com/'
activity_page = fb_domain + fb_username + '/allactivity'

driver = webdriver.Firefox()

driver.get(fb_domain)
time.sleep(2) 
driver.find_element_by_name('email').send_keys(email)
driver.find_element_by_name('pass').send_keys(pw)
time.sleep(1)
driver.find_element_by_name('login').click()
time.sleep(2)
driver.get(activity_page)
time.sleep(2)

while True:

    try:
        public_activity_delete_unlike_removereaction_button = driver.find_element_by_xpath("//img[@src='https://static.xx.fbcdn.net/rsrc.php/v3/yp/r/--soLpMIbaJ.png']/../../../following-sibling::div/span/a[contains(text(),'Delete') or contains(text(), 'Unlike') or contains(text(), 'Remove Reaction')]")
    except:
        print("did not find any public activity on page")
        load_more_button = driver.find_element_by_xpath("//h3[contains(text(), 'Load more from')]")
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});", load_more_button)
        time.sleep(2)
        driver.execute_script("arguments[0].click();", load_more_button)
        time.sleep(6)
    else:
        time.sleep(2)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});", public_activity_delete_unlike_removereaction_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", public_activity_delete_unlike_removereaction_button)
        time.sleep(4)

driver.quit() 
