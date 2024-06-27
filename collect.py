# %%

# Parei na segunda aula. https://www.youtube.com/watch?v=JqBLUi9vqgM&list=PLvlkVRRKOYFSrkOL-Bze-42pTdJIAj0_h&index=2

import requests
from bs4 import BeautifulSoup
from time import sleep
#from tqdm import tqdm

# %%
cookies = {
    'masessid': 'WS5TB2745467',
    'PHPSESSID': '8e79d8fa6018c43182ac3bde55e68e70',
    '__utma': '235797405.215517613.1715719786.1717440551.1718394740.5',
    '__utmc': '235797405',
    '__utmz': '235797405.1718394740.5.5.utmcsr=ecosia.org|utmccn=(referral)|utmcmd=referral|utmcct=/',
    'cf_clearance': 'qEQVpmShENRBZGU8Sc85EH475kq8Ze0TUisXrACTLs8-1718394668-1.0.1.1-OUsh.cQBS95rEy7WWltm4L_vtCj9TksGd3PI6PJIiW2cjiK7.yCR9rbysmNCs3RLJHrx38.INanc5XVvDTthhw',
    'phpbb3_qh6oy_u': '1',
    'phpbb3_qh6oy_k': '',
    'phpbb3_qh6oy_sid': '8f71f4dc4ea0298a9e98c417df033458',
    '__utmt': '1',
    '__utmb': '235797405.4.10.1718394740',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,no;q=0.6,ja;q=0.5,af;q=0.4,gl;q=0.3,fr;q=0.2,es;q=0.1,it;q=0.1,zh-CN;q=0.1,zh;q=0.1',
    'cache-control': 'max-age=0',
    # 'cookie': 'masessid=WS5TB2745467; PHPSESSID=8e79d8fa6018c43182ac3bde55e68e70; __utma=235797405.215517613.1715719786.1717440551.1718394740.5; __utmc=235797405; __utmz=235797405.1718394740.5.5.utmcsr=ecosia.org|utmccn=(referral)|utmcmd=referral|utmcct=/; cf_clearance=qEQVpmShENRBZGU8Sc85EH475kq8Ze0TUisXrACTLs8-1718394668-1.0.1.1-OUsh.cQBS95rEy7WWltm4L_vtCj9TksGd3PI6PJIiW2cjiK7.yCR9rbysmNCs3RLJHrx38.INanc5XVvDTthhw; phpbb3_qh6oy_u=1; phpbb3_qh6oy_k=; phpbb3_qh6oy_sid=8f71f4dc4ea0298a9e98c417df033458; __utmt=1; __utmb=235797405.4.10.1718394740',
    'priority': 'u=0, i',
    'referer': 'https://www.metal-archives.com/search?searchString=forest+of+demons&type=band_name',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

def get_content(url):
    resp = requests.get(url, cookies=cookies, headers=headers)
    return resp

def get_basic_info(soup):
    band_info_head = soup.find('div', id = 'band_info')

    bi_title = band_info.find_all('dt')
    bi_data = band_info.find_all('dd')

    data = {}
    for i in range(8): # len(bi_title & bi_data)
        chave, valor = bi_title[i].text, bi_data[i].text
        data[chave] = valor

    return data

# %%
url = 'https://www.metal-archives.com/bands/Forest_of_Demons/18054' 
resp = get_content(url)

if resp.status_code != 200:
    print("Não foi possível obter os dados")
else:
    print('Status Code: ', resp.status_code)
    
    soup = BeautifulSoup(resp.text)
    get_basic_info(soup)
# %%
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# https://medium.com/thedevproject/how-to-scrape-javascript-heavy-sites-like-a-pro-with-python-1ecf6f829538
#chromedriver_autoinstaller.install()

#%%
cookies = {
    'masessid': 'PMCTK1361695',
    'PHPSESSID': 'abf952bf4924ad82afa33d21b590045c',
    '__utmc': '235797405',
    '__utmz': '235797405.1718670823.4.4.utmcsr=duckduckgo.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    'cf_clearance': 'XLU35Jfdw706FtMi0BH.bikyDKR4udMJo_naSvNCklg-1719046801-1.0.1.1-mRVAE2BRo93y1JZWVKaeusOUh7uM3vJuhTdbKpvqdfU3PK0_oaNmvImM7wkMdqri89PKGZQOZ96wTKkXat7UiA',
    '__utma': '235797405.1289721188.1713116770.1718670823.1719047035.5',
    '__utmb': '235797405.1.10.1719047035',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'masessid=PMCTK1361695; PHPSESSID=abf952bf4924ad82afa33d21b590045c; __utmc=235797405; __utmz=235797405.1718670823.4.4.utmcsr=duckduckgo.com|utmccn=(referral)|utmcmd=referral|utmcct=/; cf_clearance=XLU35Jfdw706FtMi0BH.bikyDKR4udMJo_naSvNCklg-1719046801-1.0.1.1-mRVAE2BRo93y1JZWVKaeusOUh7uM3vJuhTdbKpvqdfU3PK0_oaNmvImM7wkMdqri89PKGZQOZ96wTKkXat7UiA; __utma=235797405.1289721188.1713116770.1718670823.1719047035.5; __utmb=235797405.1.10.1719047035',
    'priority': 'u=0, i',
    'referer': 'https://www.metal-archives.com/browse/country',
    'sec-ch-ua': '"Chromium";v="124", "Opera";v="110", "Not-A.Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"110.0.5130.82"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.243", "Opera";v="110.0.5130.82", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0',
}

url2 = 'https://www.metal-archives.com/lists/BR'

#resp2 = requests.get(url2, headers=headers)
#soup2 = BeautifulSoup(resp2.text) # Lista veio em JavaScript

# %%
driver = webdriver.Chrome()
driver.get(url2)

sleep(3)

datatable_info1 = driver.find_element(By.ID, 'bandListCountry_info').text

#next_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID,'bandListCountry_next')))
next_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[3]/div/div/div/div[2]/a[3]')))
next_button = driver.find_element(By.ID,'bandListCountry_next')

#driver.execute_script("arguments[0].scrollIntoView();", next_button)

#next_button.click() ## Não esta clicando!!! tem que aparecer 2 no print.
driver.execute_script('arguments[0].click()', next_button)
#driver.maximize_window() # se usar esse, funciona.

sleep(3)

datatable_info2 = driver.find_element(By.ID, 'bandListCountry_info').text
#datatable_info = driver.find_element(By.CLASS_NAME, 'paginate_active').text
#print(datatable_info)

next_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[3]/div/div/div/div[2]/a[3]')))
next_button = driver.find_element(By.ID,'bandListCountry_next')

#driver.execute_script("arguments[0].scrollIntoView();", next_button)

driver.execute_script('arguments[0].click()', next_button)

sleep(3)

datatable_info3 = driver.find_element(By.ID, 'bandListCountry_info').text

driver.quit()

# %%
driver = webdriver.Chrome()
driver.get(url2)

page_source_list = []
active_page = '0'
last_page = '17' ## class = 'next paginate_button paginate_button_disabled'

while active_page != last_page:
    sleep(3)
    pg_act_elem = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "paginate_active")))
    active_page = driver.find_element(By.CLASS_NAME, 'paginate_active').text
    print('Page', active_page, 'of', last_page)
    
    list_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "odd")))
    
    page_source_list.append(driver.page_source)

    sleep(3)

    next_button = driver.find_element(By.ID,'bandListCountry_next')
    driver.execute_script('arguments[0].click()', next_button)

    sleep(3)

driver.quit()

# %%
page_qtd = len(page_source_list)
band_list = []

for i in range(1,page_qtd):
    soup = BeautifulSoup(page_source_list[i])
    soup.find('tbody', role='alert')
    bands_td = soup.find_all('td')
    bands_qtd = len(bands_td)

    for i in range(0, bands_qtd, 4):
        band_name = bands_td[i].text
        band_genre = bands_td[i+1].text
        band_city = bands_td[i+2].text
        band_status = bands_td[i+3].text
        band_list.append([band_name, band_genre, band_city, band_status])

# %%
import pandas as pd
# %%
band_df = pd.DataFrame(band_list).rename(columns={0: 'Name', 1: 'Genre', 2: 'City', 3: 'Status'})

band_df.sample(5)
# %%
