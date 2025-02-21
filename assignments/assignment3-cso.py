import json
import requests

#CSO URL 
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
response = requests.get(url)
list = response.json()

with open("cso_finance.json", "wt") as f:
    f.write(json.dumps(list))