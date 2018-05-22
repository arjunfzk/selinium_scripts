

from selenium import webdriver
wd = webdriver.Firefox()
wd.get('http://uims.cuchd.in/uims/')
uid=wd.find_element_by_xpath('//*[@id="txtUserId"]')
uid.send_keys('16BCS2090')
logbtn=wd.find_element_by_xpath('//*[@id="btnNext"]')
logbtn.click()

