import webbrowser, requests, yaml
from bs4 import BeautifulSoup
#python -m pip install beautifulsoup4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
country =['SG','AU','AE']
search_keyword = "fruits+&+vegetables+wholesaler" 
ret_comp_data = []
for i in range(len(country)):
    if (country[i] == "SG"):  
        search_tag = 'div' #div for SG
        url = "https://www.yellowpages.com.sg/search/all/"
        driver.get(url + search_keyword)
        elements = driver.find_elements_by_tag_name(search_tag)
        for e in elements:
            ret_comp_data.append(e.get_attribute('data-comp-name'))            
    if (country[i] == "AU"):  
        search_tag = 'h3' #h3 for AU
        url = "https://www.yellowpages.com.au/search/listings?clue="
        driver.get(url + search_keyword)
        elements = driver.find_elements_by_tag_name(search_tag)
        for e in elements:
            if (e.get_attribute('innerHTML') != 'None'):
                ret_comp_data.append(e.get_attribute('innerHTML'))      
            
    
driver.quit()
print(ret_comp_data)
