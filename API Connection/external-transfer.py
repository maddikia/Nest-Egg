import http.client, json

conn = http.client.HTTPSConnection("api.fusionfabric.cloud")

# post a new external transfer (recurring, parent => kid)
# modify material below to create different post requests
payload = "{\n  \"internalAccountId\": \"6787147\",\n  \"externalAccountId\": \"169026\",\n  \"amount\": 25.00,\n  \"transferDirection\": \"send\",\n  \"fee\": 2,\n  \"startDate\": \"2020-12-20\",\n  \"serviceType\": \"standard\",\n  \"recurringCount\": 12,\n  \"recurringFrequency\": \"Monthly\"\n}"

# generate new token using Postman
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJjNTRVUnJqTVV3Q2pVTFRVUV93QUVBQW9GemxoN1l0LU5xVXFRZGR5TGg0In0.eyJqdGkiOiI1MzYzODJmYy1hMzY5LTRhZmMtOTY5ZS1hMGUyYTEyOTQxNmEiLCJleHAiOjE2MDg0ODI2MjQsIm5iZiI6MCwiaWF0IjoxNjA4NDgyMzI0LCJpc3MiOiJodHRwczovL2FwaS5mdXNpb25mYWJyaWMuY2xvdWQvbG9naW4vdjEiLCJhdWQiOiJiMmMtZXh0ZXJuYWwtdHJhbnNmZXJzLXYxLThjMWQyM2Q1LWM4ZWItNDc1ZS1hZDE2LThjNjlhYmE3MGE2OCIsInN1YiI6ImZmZGN1c2VyMSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImI5NDI1NDYwLWI1MWUtNGFiMy1iMGNjLWI0MjZiMTA5OWZmNyIsIm5vbmNlIjoiNjEwMDcxYjktMzczZC00MTc0LTlkYmMtODU0NjZjMjJiMzIwIiwiYXV0aF90aW1lIjoxNjA4NDgyMzIzLCJzZXNzaW9uX3N0YXRlIjoiNzgyZDYyM2QtMWZjMy00MDIyLWI5YmYtM2I0NjNhMDg2NzA3IiwiYWNyIjoiMSIsInNjb3BlIjoib3BlbmlkIGIyYy1leHRlcm5hbC10cmFuc2ZlcnMtdjEtOGMxZDIzZDUtYzhlYi00NzVlLWFkMTYtOGM2OWFiYTcwYTY4IiwiYXBwIjoiZGY0MjdhYmItNDdlNy00YWVhLTk5NmQtZGQ4MTJiNDM0YzU1IiwiaXB3aGl0ZWxpc3QiOiIiLCJpbnRJcFdoaXRlbGlzdCI6IiIsInRlbmFudCI6InNhbmRib3giLCJ1c2VybmFtZSI6ImZmZGN1c2VyMSJ9.EnDo7YAkdoisw02ZpmbByEIl9iWuFHk-CNrWjcPf5fwxpS_5zWTm9Jq6G9LXtzKIOiM-jkjN3CHLEiqf6YuluDS4l30p9fYi8doe4fkT-4RRyYboYwqSnVX_WmnE2G72LxCJcL83plklef4gqy0qHeGwRAEi-NLP3ERQ8rc32QeGTmldrrbARcBS89w8GtKwBFIudMcXRtiZSJnhnI2x05L1jcN7nKCHRCcBlpZMydTsY-FNw7tEF3syIB-78vnIZEt_gM-OL546p1rQvZhBBzgA91IxCrxzoBS0agdEUWLdub9yBBFmNNRTVD1g4Hx_yHoqKWpRgxAsn7UQyXGwqg'
access = 'Bearer ' + token
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Request-ID': 'b86aab1f-851f-4d9c-aa30-abd3ab4c3f89',
  'X-IP-Address': '{{X-IP-Address}}',
  'X-User-Agent': '{{X-User-Agent}}',
  'X-Device-Type': 'iphone',
  'X-Device-ID': '{{X-Device-ID}}',
  'Authorization': access,
  'Cookie': 'LTMSESSIONID=!7/G7s6II73Ztp+4bnaptHfLSS+0mYwS/msocl9fuV1uzVQeOFEZiWH4V4WrTa3V6myfP9BkUIXSJOfo=; TS016a938c=017d2d345809d003196a616307f21058f68d8d1a36956a6ee45cd43de405e622a34fbc22aa5913bc9f8dddb308c5e0b5309b2004003c82ebe760aa1f1d235c469e0f343437'
}
conn.request("POST", "/retail-us/me/external-transfers/v1/external-transfers", payload, headers)
res = conn.getresponse()
data = res.read()
data_json = json.loads(data.decode("utf-8"))
transfer_id = data_json['id']

# get external transfer information from the transfer made above
payload2 = ''
request_url = "/retail-us/me/external-transfers/v1/external-transfers/" + transfer_id
conn.request("GET", request_url, payload2, headers)
res = conn.getresponse()
data = res.read()
data_json2 = json.loads(data.decode("utf-8"))
print(data_json2)