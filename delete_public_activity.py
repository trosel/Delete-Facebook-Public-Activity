#! /usr/local/bin/python3
import time
from selenium import webdriver

fb_username = 'username-from-url'
email = 'email'
pw = 'pass'
year = 0
month = 0

year_month = [
    [
        '?timeend=1546329599&timestart=1543651200&sectionLoadingID=m_timeline_loading_div_1546329599_1543651200_25_&sectionID=month_2018_12',
        '?timeend=1543651199&timestart=1541055600&sectionLoadingID=m_timeline_loading_div_1543651199_1541055600_25_&sectionID=month_2018_11',
        '?timeend=1541055599&timestart=1538377200&sectionLoadingID=m_timeline_loading_div_1541055599_1538377200_25_&sectionID=month_2018_10',
        '?timeend=1538377199&timestart=1535785200&sectionLoadingID=m_timeline_loading_div_1538377199_1535785200_25_&sectionID=month_2018_9',
        '?timeend=1535785199&timestart=1533106800&sectionLoadingID=m_timeline_loading_div_1535785199_1533106800_25_&sectionID=month_2018_8',
        '?timeend=1533106799&timestart=1530428400&sectionLoadingID=m_timeline_loading_div_1533106799_1530428400_25_&sectionID=month_2018_7',
        '?timeend=1530428399&timestart=1527836400&sectionLoadingID=m_timeline_loading_div_1530428399_1527836400_25_&sectionID=month_2018_6',
        '?timeend=1527836399&timestart=1525158000&sectionLoadingID=m_timeline_loading_div_1527836399_1525158000_25_&sectionID=month_2018_5',
        '?timeend=1525157999&timestart=1522566000&sectionLoadingID=m_timeline_loading_div_1525157999_1522566000_25_&sectionID=month_2018_4',
        '?timeend=1522565999&timestart=1519891200&sectionLoadingID=m_timeline_loading_div_1522565999_1519891200_25_&sectionID=month_2018_3',
        '?timeend=1519891199&timestart=1517472000&sectionLoadingID=m_timeline_loading_div_1519891199_1517472000_25_&sectionID=month_2018_2',
        '?timeend=1517471999&timestart=1514793600&sectionLoadingID=m_timeline_loading_div_1517471999_1514793600_25_&sectionID=month_2018_1',
    ],
    [
        '?timeend=1514793599&timestart=1512115200&sectionLoadingID=m_timeline_loading_div_1514793599_1512115200_25_&sectionID=month_2017_12',
        '?timeend=1512115199&timestart=1509519600&sectionLoadingID=m_timeline_loading_div_1512115199_1509519600_25_&sectionID=month_2017_11',
        '?timeend=1509519599&timestart=1506841200&sectionLoadingID=m_timeline_loading_div_1509519599_1506841200_25_&sectionID=month_2017_10',
        '?timeend=1506841199&timestart=1504249200&sectionLoadingID=m_timeline_loading_div_1506841199_1504249200_25_&sectionID=month_2017_9',
        '?timeend=1504249199&timestart=1501570800&sectionLoadingID=m_timeline_loading_div_1504249199_1501570800_25_&sectionID=month_2017_8',
        '?timeend=1501570799&timestart=1498892400&sectionLoadingID=m_timeline_loading_div_1501570799_1498892400_25_&sectionID=month_2017_7',
        '?timeend=1498892399&timestart=1496300400&sectionLoadingID=m_timeline_loading_div_1498892399_1496300400_25_&sectionID=month_2017_6',
        '?timeend=1496300399&timestart=1493622000&sectionLoadingID=m_timeline_loading_div_1496300399_1493622000_25_&sectionID=month_2017_5',
        '?timeend=1493621999&timestart=1491030000&sectionLoadingID=m_timeline_loading_div_1493621999_1491030000_25_&sectionID=month_2017_4',
        '?timeend=1491029999&timestart=1488355200&sectionLoadingID=m_timeline_loading_div_1491029999_1488355200_25_&sectionID=month_2017_3',
        '?timeend=1488355199&timestart=1485936000&sectionLoadingID=m_timeline_loading_div_1488355199_1485936000_25_&sectionID=month_2017_2',
        '?timeend=1485935999&timestart=1483257600&sectionLoadingID=m_timeline_loading_div_1485935999_1483257600_25_&sectionID=month_2017_1',
    ]
]

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
driver.get(activity_page + year_month[year][month])
time.sleep(2)

while True:
    # Try to find a public activity
    try:
        public_activity_delete_unlike_removereaction_button = driver.find_element_by_xpath("//img[@src='https://static.xx.fbcdn.net/rsrc.php/v3/yp/r/--soLpMIbaJ.png']/../../../following-sibling::div/span/a[contains(text(),'Delete') or contains(text(), 'Unlike') or contains(text(), 'Remove Reaction')]")
    except:
        print("did not find any public activity on page -> loading more")
        # Try to find a "Load more from" button to get more public activities
        try:
            load_more_button = driver.find_element_by_xpath("//h3[contains(text(), 'Load more from')]")
        except:
            # If there's no "Load more" button, go to previous month
            print("the load more button is not here -> going to previous month")
            month += 1
            try:
                driver.get(activity_page + year_month[year][month])
            except IndexError:
                # Go to previous year if no more months
                year += 1
                month = 0
                driver.get(activity_page + year_month[year][month])
        else:
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});", load_more_button)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", load_more_button)
    else:
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});", public_activity_delete_unlike_removereaction_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", public_activity_delete_unlike_removereaction_button)
    finally:
        time.sleep(6)

driver.quit()
