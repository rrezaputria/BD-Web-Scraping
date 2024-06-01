#penggunaan library
from selenium import webdriver
import sys, getopt
import argparse
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#menghubungkan ke chrome 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#fungsi parse_args untuk menjalankan skrip dengan argument input otput file
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", default = "", help = "input filename")
    parser.add_argument("-o", "--outfile", default = "", help = "output filename")
    return parser.parse_args()


#fungsi main untuk skrip utama
def main():
    
    args = parse_args()
    outfile = args.outfile
    infile = args.infile
    
    data = []

    with open(infile, "r", encoding = "utf-8") as f:
        urls = f.read().splitlines()
        
    #mengambil dua url-teratas
    top_two_url = urls[:2]
     
    for u in top_two_url:
        driver.get(u)
        elems = driver.find_element(By.TAG_NAME, "body").text
        data.append(elems)
    
    with open(outfile, "w", encoding = "utf-8") as f:
        f.write(str(data))
    
    driver.close()
    
#menjalankan kode   
if __name__ == "__main__":
    main()