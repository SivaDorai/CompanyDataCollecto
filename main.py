from util import util
from leach import wspider

company_list = []
wspider.get_companies()
f = open("companies.txt", "r")
print(f.read())
f.close()