import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
NAME= 'Zarafsha Uzzaman'
EMAIL= 'zarafsha.u@gmail.com'
ORGANIZATION ='GW'




chrome_filepath = '/Users/zarafshauzzaman/PycharmProjects/automated-filling-forms/chromedriver/chromedriver 3'
s = Service(chrome_filepath)
driver = webdriver.Chrome(service=s)

googleform_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeIOfCuu-UD-WFRp669XnJu4SHF2G1y_kw-uwPFypBH7As7UQ/viewform?usp=sf_link'
driver.get(googleform_url)

info =[NAME, EMAIL, ORGANIZATION]
name_email_org_field = driver.find_elements(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf')

for i in range(len(name_email_org_field)):
    name_email_org_field[i].send_keys(info[i])

days = driver.find_elements(By.CSS_SELECTOR, 'div.uHMk6b.fsHoPb')

for day in days:
    if days.index(day) == 0 or days.index(day) == 1:
        day.click()


options = driver.find_elements(By.CSS_SELECTOR, 'span.aDTYNe.snByac.OvPDhc.OIC90c')


for option in options:
    if options.index(option) == 1:
        option.click()


yes = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div/label/div/div[1]/div[2]')
yes.click()



submit = driver.find_element(By.CSS_SELECTOR, 'span.NPEfkd.RveJvd.snByac')
submit.click()

time.sleep(20)

driver.quit()