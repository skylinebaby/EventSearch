from django.test import TestCase
from django.core.urlresolvers import reverse
from . import service
# Create your tests here.

class ViewMethodTests(TestCase):

	def test_the_category_page_renders_correctly(self):
		"""
		The categories.html should be rendered correctly 
		and contains specific items
		"""
		response = self.client.get(reverse('events:redirect'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Music")
		self.assertContains(response, "Business")

	def test_redirect_to_category_page_with_choices_less_than_3(self):
		"""
		The category page should be redirected to its own page
		if the choices number is more than 3
		"""
		choices = ['103']
		page = 1
		preload = {'checks':choices, 'page':page}
		response = self.client.post(reverse('events:category_results'), params = preload)
		self.assertRedirects(response, reverse('events:redirect'),
			status_code=302, target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)


	def test_redirect_to_category_page_with_choices_more_than_3(self):
		"""
		The category page should be redirected to its own page
		if the choices number is less than 3
		"""
		choices = ['103','101','110','113']
		page = 1
		preload = {'checks':choices, 'page':page}
		response = self.client.post(reverse('events:category_results'), params = preload)
		self.assertRedirects(response, reverse('events:redirect'),
			status_code=302, target_status_code=200, host=None, msg_prefix='', fetch_redirect_response=True)

	"""
	There should be test methods for the pagination features,
	however, due to the time limitation, I can't finish these 
	test methods ontime.
	"""




class ServiceMethodTests(TestCase):


	def test_get_categories_with_status_code_200(self):
		"""
		get_categories() should return the response with 
		status_code 200
		"""
		response = service.get_categories_test()
		self.assertEqual(response.status_code, 200)

	def test_get_categories_returns_all_20_categories(self):
		"""
		get_categories() should first connect to the 
		end point correctly and get the response with 
		correct status_code
		"""
		response = service.get_categories()
		size = len(response['categories'])
		self.assertEqual(size, 20)


	def test_get_categories_results_should_contain_pagination(self):
		"""
		the resuld from get_categories() should contain 
		a pagination term which can further assure the 
		correctness of the result
		"""
		response = service.get_categories()
		self.assertEqual('pagination' in response, True)

	def test_get_results_with_status_code_200(self):
		"""
		The result from get_results should return a response
		with status_code 200
		The test case for this method is:
			choices = [115, 116, 199]
			page = 1
		"""
		choices = [115, 116, 199]
		page = 1
		response = service.get_results_test(choices, page)
		self.assertEqual(response.status_code, 200)


	def test_get_results_returns_contains_50_events_in_response(self):
		"""
		The result from get_results() should return 50 events under
		the test case 
			choices = [115, 116, 199]
			page = 1
		"""
		choices = [115, 116, 199]
		page = 1
		response = service.get_results(choices, page)
		self.assertEqual(len(response['events']), 50)








