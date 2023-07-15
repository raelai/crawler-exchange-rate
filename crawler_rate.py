# pip install selenium
# pip install pandas
from bs4 import BeautifulSoup
import pandas as pd
import csv
import io
import sys
sys.path.insert(0,'./chromedriver')
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def getData(outputfile):
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://portal.sw.nat.gov.tw/APGQO/GC331#")

  # use beautfiulsoup-find function to locate css selector and get the data
  query = driver.find_element("id", "queryButton")
  query.click()
  bs = BeautifulSoup(driver.page_source,'html.parser')


  with io.open(outputfile, "w", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["country", "currency", "currency_code", "year", "month", "period", "purchase_in"\
                      ,"sales_out"])
    for row_num in range(1, 29):
      # row_num = 1
      country = bs.find("tr", id = row_num).find_all("td")[1].string.strip()
      currency = bs.find("tr", id = row_num).find_all("td")[2].string.strip()
      currency_code = bs.find("tr", id = row_num).find_all("td")[3].string.strip()
      year = bs.find("tr", id = row_num).find_all("td")[4].string.strip()
      month = bs.find("tr", id = row_num).find_all("td")[5].string.strip()
      period = bs.find("tr", id = row_num).find_all("td")[6].string.strip()
      purchase_in = bs.find("tr", id = row_num).find_all("td")[7].string.strip()
      sales_out = bs.find("tr", id = row_num).find_all("td")[8].string.strip()

      # write into csv
      writer.writerow([country, currency, currency_code, year, month, period, purchase_in, sales_out])
      # read_file = pd.read_csv(output_file_name)
      # read_file.to_excel ('/content/drive/MyDrive/output.xlsx', index = None, header=True)

if __name__ == '__main__':
  # configurable parameter 
  # link:https://portal.sw.nat.gov.tw/APGQO/GC331#

  output_file_name = './output.csv' # set location and file name

  
  getData(output_file_name) # csv output
  read_file = pd.read_csv (output_file_name)
  read_file.to_excel ('./output.xlsx', index = None, header=True) #excel output
  print("\nfinish")
