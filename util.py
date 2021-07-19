from re import search
import yaml
from leach import wspider

class util:
    global config 
    config = "d:\\Siva\\CompanyDataCollector\\criteria.yaml"
     
    def load_yaml(self):
        ret_data = []
        with open(config) as f:
            data = yaml.load_all(f, Loader=yaml.FullLoader)
            country_dict = next(data)                  
            for key in country_dict:
                country = key
                for search_args in country_dict[key].items():
                    ret_data.append(search_args[1])
            print(ret_data)
        return ret_data
                    
                    