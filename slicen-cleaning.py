#melakukan cleaning slice n
#penggunaan library
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService 

#menghubungkan dengan chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))


#define function utama yang akan dijalankan
def main():
    
    data = []  #menyimpan kedalam list
    
    with open("hasil-search-url.txt", "r", encoding = "utf-8") as f:
        urls = [line.rstrip("\n") for line in f][:2]  #melakukan penghapusan \n pada dua url teratas
       
    #looping for
    for u in urls:  
        driver.get(u)
        elems = driver.find_elements("tag name", "p")  #melakukan ekstraksi paragraf
        
        #penambahan hasil ke dalam list data []
        for elem in elems:
            cleaned_text = re.sub(r'[\\^\n]', " ", elem.text)  #membersihkan teks lebih lanjut
            cleaned_text = re.sub(r'(\[\d+\])|(\d+\s*([.!?])|(\d+\s*(?=\n|$)))', "", cleaned_text) #penghapusan pola angka []
            data.append(cleaned_text)

    driver.close()
    
    #hasilnya akan disimpan dalam "cleaning-filterisasi.txt"
    with open("slicen-cleaning.txt", "w", encoding = "utf-8") as f:
        f.write(str(data))

if __name__ == "__main__":
    main()