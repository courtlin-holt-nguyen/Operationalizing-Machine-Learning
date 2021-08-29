import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://9bb1c313-7ae1-4ef6-8f3e-3d71ac4357a6.eastus2.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "UrkfakBrtDdToczQW87eQ7D5kwfMbefZ"

# Two sets of data to score, so we get two results back
data = {
    "data": [
        {
         "age": 43,
         "job": "blue-collar",
         "marital": "single",
         "education": "basic.9y",
         "default": "no",
         "housing": "yes",
         "loan": "no",
         "contact": "cellular",
         "month": "jul",
         "day_of_week": "thu",
         "duration": 982,
         "campaign": 1,
         "pdays": 999,
         "previous": 0,
         "poutcome": "nonexistent",
         "emp.var.rate": 1.4,
         "cons.price.idx": 93.918,
         "cons.conf.idx": -42.7,
         "euribor3m": 4.963,
         "nr.employed": 5228.1
        },
    ]
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
