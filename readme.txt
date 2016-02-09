Hi, 

Thank you for your time reading this file.

The EventSearch App was developed on 
	Django 1.9.1
	Python 3.4
		requires:
			requests 2.6.2
			sqlite 3.8.5

To run the App, please unpack go to the dir: /EventSearch/mysite/
and enter the command: "python manage.py runserver"
and then open a browser with url"127.0.0.1:8000/events/categories",
then select three categories you are interested in and the results will be 
returned with pagination.

Implementation logic:
	There is a file service.py which has two methods:
		get_categories() to call the RESTapi to return the 20 categories,
		get_events(choices, page) to call the RESTapi to return a page of events.

	And paginations are supported.


Unit Tests are in the file tests.py.

Thanks,
Yingjie Tang
