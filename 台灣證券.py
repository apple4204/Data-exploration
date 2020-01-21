import requests
import json
import csv

url = requests.get('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20191124&stockNo=2330&')


s = json.loads(url.text)

print(s)
#for data in (s['data']):
#    print(data)


outputfile = open(r'C:\vscode\爬蟲\output.csv', 'w', newline='')
outputwrite = csv.writer(outputfile)

outputwrite.writerow(s['title'])
outputwrite.writerow(s['fields'])

for data in (s['data']):
    outputwrite.writerow(data)
  
outputfile.close()


