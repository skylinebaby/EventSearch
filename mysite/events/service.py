import requests



def get_categories():
	url = 'https://www.eventbriteapi.com/v3/categories/'
	response = requests.get(
		url,
		headers = {
			"Authorization": "Bearer DVFXYAEUNTU73VDFSBZG",
		},
		verify = True,
	)
	return response.json()



def get_results(choices, page):
	url ='https://www.eventbriteapi.com/v3/events/search/'
	response = requests.get(
		url,
		headers = {
			"Authorization": "Bearer DVFXYAEUNTU73VDFSBZG",
		},
		verify = True,
		params = {'categories':choices, 'page': page},
		)
	return response.json()



"""
The following two methods are used in Unit Test
to assure the correct status code
"""

def get_categories_test():
	url = 'https://www.eventbriteapi.com/v3/categories/'
	response = requests.get(
		url,
		headers = {
			"Authorization": "Bearer DVFXYAEUNTU73VDFSBZG",
		},
		verify = True,
	)
	return response

def get_results_test(choices, page):
	url ='https://www.eventbriteapi.com/v3/events/search/'
	response = requests.get(
		url,
		headers = {
			"Authorization": "Bearer DVFXYAEUNTU73VDFSBZG",
		},
		verify = True,
		params = {'categories':choices, 'page': page},
		)
	return response