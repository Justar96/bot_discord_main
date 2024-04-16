import requests
import time

url = 'https://weather.bangkok.go.th/Images/Radar/radar.gif'
date_time = int(time.time()*1000)

r = requests.get(url)

print(r.status_code)

if r.status_code == 200:
    with open(f"weather{date_time}.gif" ,'wb') as f:
        f.write(r.content)
    print("Downloading...")
    
else:
    print("Fail requests")
    
