from setuptools import setup, Extension, find_packages

requirements_noversion = [
'requests'
]
setup(
	# Meta information
	name				= 'serp_bot',
	version				= '0.0.1',
	author				= 'Supratik Chatterjee',
	author_email		= 'chatterjee.supratik@tcs.com',
	# license			= '2-clause BSD',
	url					= 'https://github.com/supratikchatterjee16/workbench',
	description			= 'Search Engine Results Page Bot',
	keywords			= ['serp bot webscraping scraping search engine package python'],
	install_requires	= requirements_noversion,
	# build information
	py_modules			= ['serp_bot'],
	packages			= find_packages(),
	package_dir			= {'serp_bot' : 'serp_bot'},
	include_package_data= True,
	# package_data		= {'serp_bot' : [
	# 							'databank/*',
	# 							'datadump/*',
	# 							'factuals/*'
	# 							]},

	zip_safe			= True,
	# https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py
	# entry_points		= {'console_scripts' : ['news_raker = news_raker:run'],},
	# ext_modules			= [bjoern_extension],
	classifiers			= [
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
)
