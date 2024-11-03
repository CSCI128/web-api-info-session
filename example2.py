# TICKETMASTER API EXAMPLE
# https://developer.ticketmaster.com/products-and-docs/apis/getting-started/
import requests

API_KEY = 'O25rm2nh73Airm6ZVRGIWW4HEsLGSKAP'

# Event Search
# https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/#search-events-v2
resp = requests.get(f'https://app.ticketmaster.com/discovery/v2/events.json?countryCode=US&postalCode=80401&apikey={API_KEY}')
resp = resp.json()

# get all events in golden
for e in resp['_embedded']['events']:
    print(e['id'])
    print(e['name'])
    print(e['url'])
    print(e['dates'])
    print(e['sales'])

print("\n\n") # separator for output

# Event Details
# https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/#event-details-v2
id = 'Z7r9jZ1A7C3AV'
resp = requests.get(f'https://app.ticketmaster.com/discovery/v2/events/{id}.json?apikey={API_KEY}')
resp = resp.json()

print(resp['name'])
print(resp['url'])
