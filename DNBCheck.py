from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


def checkCompany(comp):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe"
    driver = webdriver.Chrome(ChromeDriverManager().install())    
    comp_found = False
    search_term = comp
    url = "https://www.dnb.com/business-directory/company-search.html?term="+search_term+"&page=1"
    driver.get(url)
    elements = driver.find_elements_by_class_name("primary_name")
    comp_count = 0
    for e in elements : #what to do when multiple companies with same name, different industrry or country is found - this has to be handled
        #print(e.text)
        #e.send_keys()
        comp_found = True        
        comp_count = comp_count+1 
        break
    driver.close()
    return comp_found, comp_count