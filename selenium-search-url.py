#penggunaan library
from bs4 import BeautifulSoup #parsing page web
from selenium import webdriver #otomatisasi brower
from selenium.webdriver.chrome.service import Service as ChromeService #penggunaan chrome
from webdriver_manager.chrome import ChromeDriverManager

#inisiasi chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

#inisiasi driver
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#kata kunci yang ingin dicari
query = "Joko Widodo"

#jumlah page yang ingin dicari
n_pages = 10

#looping
for page in range (1, n_pages):
    url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    #soup = BeautifulSoup(r.text, "html.parser")
    
    search = soup.find_all('div', class_ = "yuRUbf")
    for h in search:
        #links.append(h.a.get('href'))
        
        #kemudian, untuk hanya menampilkan url-nya saja, dilakukan penambahan "#" pada cetak teksnya
        #print(h.a.text)
        
        print(h.a.get('href'))