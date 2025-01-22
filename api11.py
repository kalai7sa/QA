import requests
response=requests.post("https://automationexercise.com/api/createAccount",
                       params={"name":"kalaiSelvi","email":"kal7sa@gmail.com","password":"kal123",
                              "title":"Mrs",
                                "birth_date":"02","birth_month":"01","birth_year":"1981",
                                "first_name":"Kalai","last_name":"Selvi","company":"qa_guru",
                                "address":"2433_Twinoaks","country":"America","zipcode":"75068",
                                "state":"Texas","city":"Frisco","mobile_number":"513213613"
                               })
print(response.status_code)
print(response.text)
if response.status_code==201:
    data=response.json
    print(data['responseCode'])
    print("Account created successfully")

else:
    print("Failed to create account")
    

