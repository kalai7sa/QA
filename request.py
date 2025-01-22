import requests

# Make the GET request
response = requests.get("https://automationexercise.com/api/productsList")
#print(response)
# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()
    #print(data)
    # Print the first item in the response
    print(data['responseCode'])
    print("First post:", data['products'][0])
else:
    print("Failed to retrieve data:", response.status_code)