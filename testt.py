from selenium import webdriver
wd = webdriver.Firefox()
usr='admin'
pasw='password'
wd.get('https://cloudkentest.herokuapp.com/')
username=wd.find_element_by_id('cloud')#userid
username.send_keys(usr)
password=wd.find_element_by_id('ken')#password
password.send_keys(pasw)
button2=wd.find_element_by_id('check')
button2.click()