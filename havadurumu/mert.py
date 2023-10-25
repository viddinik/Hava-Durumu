import requests

sehir = "İstanbul"
api_key = "cebd3e3e62f880dcfe1ed2d84ca66af1"
ana_url = "https://api.openweathermap.org/data/2.5/weather?"
birim = "&units=metric"
url = ana_url+"q="+sehir+"&appid="+api_key+birim
response = requests.get(url)
hava_verisi = response.json()

print(hava_verisi)

if hava_verisi['cod'] != 401:
    print(("Şehir: "), hava_verisi["name"])
    print(("Hava: "), hava_verisi["weather"])
    print(("Hava: "), hava_verisi["weather"][0]["main"])
    print(("Sıcaklık: "), hava_verisi["main"]["temp"])

else:
    print("şehir bulunamadı")