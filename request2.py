import requests
response=requests.get("https://automationexercise.com/api/brandsList")

if response.status_code == 200:
    #data = requests.get("https://automationexercise.com/api/brandsList").json()
    data = response.json()
    #print(data['responseCode'])
    print(data['brands'][2])
else:
    print("Failed to retrive data:",response.status_code)