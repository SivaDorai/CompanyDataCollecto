from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class wspider:
    def get_companies():
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        country =['AU'] #list of countries to check
        search_keyword = "fruits+&+vegetables+wholesaler" 
        ret_comp_data = []
        f = open("companies.txt", "w")
        for i in range(len(country)):
            if (country[i] == "SG"):  
                f.write("SG\n")
                search_tag = 'div' #div for SG
                url = "https://www.yellowpages.com.sg/search/all/"
                driver.get(url + search_keyword)
                elements = driver.find_elements_by_tag_name(search_tag)
                for e in elements:
                    if e.get_attribute('data-comp-name') is not None:                        
                        f.write(e.get_attribute('data-comp-name'))
                        f.write('\n')
                        #ret_comp_data.append(e.get_attribute('data-comp-name'))            
            if (country[i] == "AU"):
                f.write("AU\n")  
                search_tag = 'h3' #h3 for AU
                url = "https://www.yellowpages.com.au/search/listings?clue="
                driver.get(url + search_keyword)
                elements = driver.find_elements_by_tag_name(search_tag)
                for e in elements:
                    #ret_comp_data.append(e.get_attribute('innerHTML'))      
                    f.write(e.get_attribute('innerHTML'))
                    f.write('\n')
            if (country[i] == "AE"):
                f.write("AE\n")  
                search_tag = 'img' #h3 for AU
                for i in range(1,23):
                    url = "http://best-food-importers.com/business-directory/wpbdp_category/uae/page/"+str(i)
                    driver.get(url)
                    elements = driver.find_elements_by_tag_name(search_tag)
                    for e in elements:
                        #ret_comp_data.append(e.get_attribute('title'))      
                        f.write(e.get_attribute('title'))
                        f.write('\n')
            if (country[i] == "HK"):
                f.write("HK\n")  
                search_tag = 'a' #h3 for AU
                #for i in range(1,23):
                url = "https://sg.kompass.com/searchCompanies/facet?value=HK&label=Hong%20Kong&filterType=country&searchType=SUPPLIER&checked=true"
                driver.get(url)
                elements = driver.find_elements_by_tag_name(search_tag)
                for e in elements:
                    #ret_comp_data.append(e.get_attribute('title'))      
                    f.write(e.get_attribute('innerHTML'))
                    f.write('\n')


             

        driver.quit()
        f.close()
