import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = 'C:/Usuários/thiag_sds47gm/Downloads/chromedriver.exe'

driver = webdriver.Chrome()

driver.get('https://www.omelete.com.br/')

element = driver.find_element('xpath', '/html/body/header/div[2]/div[1]/div/div[4]/div[1]/i') 
element.click()
time.sleep(1)
pyautogui.write('Deadpool')
pyautogui.press('enter')
time.sleep(10)

titles = driver.find_elements(By.XPATH, '//*[@id="news"]/div[2]/div/div[1]/main/article/div[1]/a/div[2]/div[2]/h2')
dates = driver.find_elements(By.XPATH, '//*[@id="news"]/div[2]/div/div[1]/main/article/div[1]/a/div[2]/div[1]/div[2]')

for title, date in zip(titles, dates):
    print(f'Título: {title.text}, Data: {date.text}')

with open('noticias_deadpool.txt', 'w') as file:
    for title, date in zip(titles, dates):
        file.write(f'Título: {title.text} - Data: {date.text}\n')

driver.quit()