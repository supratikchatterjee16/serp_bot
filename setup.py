from setuptools import setup, Extension, find_packages



with open('README.md') as f:
	extd_desc = f.read()

requirements_noversion = [
'requests'
]
setup(
	# Meta information
	name				= 'serp_bot',
	version				= '0.1.0',
	author				= 'Supratik Chatterjee',
	author_email		= 'supratikdevm96@gmail.com',
	# license			= '2-clause BSD',
	url					= 'https://github.com/supratikchatterjee16/serp_bot',
	description			= 'Search Engine Results Page Bot',
	keywords			= ['serp','bot', 'webscraping', 'scraping', 'search engine', 'package', 'python', 'crawler'],
	install_requires	= requirements_noversion,
	# build information
	py_modules			= ['serp_bot'],
	packages			= find_packages(),
	package_dir			= {'serp_bot' : 'serp_bot'},
	include_package_data= True,
	long_description = extd_desc,
	long_description_content_type='text/markdown',
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
