#melakukan cleaning slice n, filterisasi penghapusan baris paragraf < 5 kata, dan pengubahan output menjadi dua dimensi
#penggunaan library
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService 
import re

#menghubungkan dengan chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#define function utama yang akan dijalankan
def main():
    
    data = []  #menyimpan data ke dalam list
    
    with open("hasil-search-url.txt", "r", encoding = "utf-8") as f:
        urls = [line.rstrip("\n") for line in f][:2] #melakukan penghapusan \n pada dua url teratas
    
    #looping for
    for u in urls:  
        driver.get(u)
        elems = driver.find_elements("tag name", "p") #melakukan ekstraksi paragraf
        
        #menyimpan teks kedalam sub list dari list data, sehingga menjadi 2 dimensi
        paragraphs = []
        for elem in elems:
            cleaned_text = re.sub(r'[\\^\n]', "", elem.text) #membersihkan teks lebih lanjut
            cleaned_text = re.sub(r'(\[\d+\])|(\d+\s*([.!?])|(\d+\s*(?=\n|$)))', "", cleaned_text) #penghapusan pola angka []
            if len(cleaned_text.split()) >= 5: #filterisasi pengahapusan jumlah baris paragraf < 5 kata
                paragraphs.append(cleaned_text)
        data.append(paragraphs)

    driver.close()
    
    #hasilnya akan disimpan dalam "cleaning-dua-dimensi.txt"
    with open("dua-dimensi-cleaning.txt", "w", encoding = "utf-8") as f:
        f.write(str(data))

if __name__ == "__main__":
    main()