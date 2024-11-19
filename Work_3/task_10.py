import requests

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

payload = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <CountryIntPhoneCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
            <sCountryISOCode>RU</sCountryISOCode>
        </CountryIntPhoneCode>
    </soap:Body>
</soap:Envelope>"""

headers = {'Content-Type': 'text/xml; charset=utf-8'}


response = requests.post(url, headers = headers, data = payload)

print(response.text)
print(response.status_code)

############################################################

import zeep

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = zeep.Client(wsdl=wsdl_url)
country_code = "RU"
result = client.service.CountryIntPhoneCode(sCountryISOCode=country_code)

print(f"Country's telephone code: {country_code} - {result}")
