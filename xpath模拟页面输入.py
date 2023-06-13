import requests
from lxml import etree

url = "https://kap.staging.adm-corp.kuaishou.com/aias-data/budget/detail/list"
params = {"bizRange": 1,
          "bizCategory": -1,
          "pageNum": 1,
          "pageSize": 12,
          "totalCount": 0
          }

response = requests.post(url, params=params )
# print(response)
html = response.text
# print(html)
tree = etree.HTML(html)
results = tree.xpath("//div[@id='mainContent']/main[contains(@class,'ks-main')]")

for result in results:
    print(result)