import requests
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from datetime import datetime 

# задание нубское с простыми опциями 
# третий раз в жизни на питоне пишу - прошу, судите строго
# R01235 - доллар, доллар, доллар - грязная зеленая бумажка
# R01239 - евро

value_ = "R01235"
dateStart_ = "01/01/2024"
dateEnd_ = "21/10/2024"


def GetData(value_, dateStart_, dateEnd_):
    url_ = f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={dateStart_}&date_req2={dateEnd_}&VAL_NM_RQ={value_}"
    res = requests.get(url_)
    if res.status_code == 200:
        return res.content
    else:
        print("The data getting is failed...")


def ParseData(xml_data):
    root = ET.fromstring(xml_data)
    dates = []
    values = []
    for record in root.findall('Record'):
        date = record.get('Date')
        value = record.find('Value').text.replace(',', '.')
        dates.append(datetime.strptime(date, '%d.%m.%Y'))
        values.append(float(value))
    return dates, values


xmlData = GetData(value_, dateStart_, dateEnd_)  
dates, values = ParseData(xmlData)

plt.figure(figsize=(12, 6))
plt.plot(dates, values, marker='o', linestyle='-', color='b')
plt.title('Jan 2024')  
plt.xlabel('Date')
plt.ylabel('USD to RUB')
plt.grid(True)
plt.tight_layout()  
plt.show()
