'''
Author: Jay Patel
Organization: GDG Cloud Auburn
Google Places API Doc: https://developers.google.com/places/web-service/search
'''

import requests

# Google Maps API Key
MAPS_API_KEY = "AIzaSyAykjZ7BBpIjQ0UQbgPuWsa6H8F5s9QTmU"

def main():
	
	# Create Request URL
	places_search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
	input_val = "input=arigato"
	input_type = "&inputtype=textquery"
	api_key = "&key=" + MAPS_API_KEY 

	request_url = places_search_url + input_val + input_type + api_key
	
	# Send Request
	r = requests.get(request_url)
	
	# Check the response
	json_data = r.json()

	# Create a request for place details
	place_details = "https://maps.googleapis.com/maps/api/place/details/json?"
	place_id = "place_id=" + json_data['candidates'][0]['place_id']
	request_place_details_url = place_details + place_id + api_key
	
	# Send Request
	r = requests.get(request_place_details_url)

if __name__ == '__main__':
    main()