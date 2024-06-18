# %%

# Parei na segunda aula. https://www.youtube.com/watch?v=JqBLUi9vqgM&list=PLvlkVRRKOYFSrkOL-Bze-42pTdJIAj0_h&index=2

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

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

# https://medium.com/thedevproject/how-to-scrape-javascript-heavy-sites-like-a-pro-with-python-1ecf6f829538
#chromedriver_autoinstaller.install()

#%%
url2 = 'https://www.metal-archives.com/lists/BR'

resp2 = requests.get(url2, headers=headers)

soup2 = BeautifulSoup(resp2.text) # Lista veio em JavaScript
# %%
driver = webdriver.Chrome()
driver.get(url2)

# https://selenium-python.readthedocs.io/waits.html

html = driver.page_source
soup3 = BeautifulSoup(html)
# %%
