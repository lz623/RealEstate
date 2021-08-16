from os import listdir
from os.path import isfile, join
import pandas as pd
import json
def load_json_homes(folder):
    folder = r'/Users/yuchenzhang/Documents/Reps/actor-zillow-api-scraper/apify_storage/datasets/default'
    ls_files = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]
    homes = []
    for f in ls_files:
        with open(f, 'r') as rf:
            home = json.load(rf)
            if 'address' in home:
                for k in home['address']:
                    home[k] = home['address'][k]
                if ("streetAddress" in home) and \
                    ("city" in home) and \
                    ("state" in home) and \
                    ("zipcode" in home):
                    home['address'] = home["streetAddress"] + ', ' + home["city"] + ', ' + home["state"] + ', ' + home["zipcode"]
            homes.append(home)
    return pd.DataFrame(homes)


    