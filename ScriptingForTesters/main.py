import requests

site_photos_json_url='https://jsonplaceholder.typicode.com/photos'

# Make an HTTP GET request to the API to fetch the JSON resources located at the specified url. 
site_json_response = requests.get(site_photos_json_url)

print(site_json_response.json())


# Making an HTTP POST request
jsonPayload = {'AlbumId': 1, 'Title': 'Test', 'url': 'Nothing.com', 'ThumbnailUrl': 'Nothing.com'}

response = requests.post(site_photos_json_url, json=jsonPayload)

print(response.json())


# Making an HTTP PUT request
site_photos_json_url_specific = 'https://jsonplaceholder.typicode.com/photos/100'
response = requests.put(site_photos_json_url_specific, json=jsonPayload)

print(response.json())


# Making an HTTP DELETE request
response = requests.delete(site_photos_json_url_specific)
print(response.json())