from os import remove
from util import util
from leach import wspider
from DNBCheck import checkCompany

def check_company_authenticity():
    company_list = []
    f = open("companies.txt", "r")
    c = (f.read())
    company_list = c.split("\n")
    company_found = False
    company_count = 0
    for comp in company_list:
        company_found, company_count = checkCompany(comp);
        if (company_found == False): #if company is not found in DNB remove from list
            company_list.remove(comp)
        else:
            if (company_count>1):
                print("More than 1 found check manually" + comp)        

    print(company_list)
    f2 = open("final_companies.txt", "w")
    for k in range(len(company_list)):
        f2.write(company_list[k])
        f2.write('\n')            
        
    f.close()
    f2.close()

#def find_companies():
    #wspider.get_companies()

check_company_authenticity()
