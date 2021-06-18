import re
import os
import random
import requests
import datetime
import logging

logger = logging.getLogger(__name__)

# Classes
# Purpose : SERP bot with delayed search between multiple search engines with different user-agents to prevent bot capture
class RequestDispatcher():
	def __init__(self):
		self.domain_hit_times = {}
		self.default_headers  = {
			'Accept' : '*/*',
			'Accept-Encoding' : 'gzip, deflate, br',
			'Accept-Language' : 'en-US,en;q=0.5',
			'Connection' : 'keep-alive',
			'Content-Length' : '0'
		}
		self.user_agents = [
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.61',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0',
			'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
			'Mozilla/5.0 (iPad; CPU OS 10_15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/28.0 Mobile/15E148 Safari/605.1.15',
			'Mozilla/5.0 (Android 10; Mobile; rv:68.0) Gecko/68.0 Firefox/79.0',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.44',
			'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
			'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
			'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
			'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2)',
			'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
			'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
			'Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko'
		]
		self.last_response = {}
	def get_random_user_agent(self):
		return random.choice(self.user_agents)
	def get(self, url):
		headers = self.default_headers
		headers['User-Agent'] = self.get_random_user_agent()
		domain = url[url.find('://') + 3 : url.find('/', 8)] # In case of error let it propagate.
		domain = domain.split('.')
		domain = ''.join([domain[-2], '.', domain[-1]])
		logger.debug("Hit domain : ", domain)
		self.domain_hit_times[domain] = datetime.datetime.now()
		self.last_response = requests.get(url, headers = headers)
		return self.last_response
	def post(self, url, data):
		headers = self.default_headers
		headers['User-Agent'] = self.get_random_user_agent()
		domain = url[url.find('://') + 3 : url.find('/', 8)] # In case of error let it propagate.
		domain = domain.split('.')
		domain = ''.join([domain[-2], '.', domain[-1]])
		logger.debug("Hit domain : ", domain)
		self.domain_hit_times[domain] = datetime.datetime.now()
		self.last_response = requests.post(url, data, headers = headers)
		return self.last_response


class GenericSearchEngine: # We'll take the example of google's search engine. This is the same in a lot of search engines.
	#Sample url : https://www.google.com/search?q=hello+world&start=10
	protocol = 'https://'
	base_url = None
	search_extension = None# Similar to 'search' in google's search URL
	query_key = None
	search_seperator = '+'
	query = ''
	key_seperator = '&'
	index_key = None
	index = 1
	increment_factor = 10
	additional = '' # This must start with a & symbol
	cooldown = 0
	last_triggered = None
	common_links_file = None# filepath required
	last_response = {}
	last_used = None
	def build_base_query(self, phrase):
		phrase = phrase.replace(' ', self.search_seperator)
		self.query = self.protocol + self.base_url + '/' + self.search_extension + '?' + self.query_key + '=' + phrase
	def get_next_page(self):
		url = self.query + self.additional + self.key_seperator + self.index_key + '=' + str(self.index * self.increment_factor)
		self.index += 1
		return url
	def get_current_url(self):
		return self.query, self.query + self.additional + self.key_seperator + self.index_key + '=' + str(self.index)
	def get_content(self):
		return self.last_response.content
	def get_links(self):
		# fetch links. Remove duplicates and common links for each engine.
		url_split = self.base_url.split('.')
		domain = url_split[len(url_split) - 2]
		content = str(self.last_response.content)
		# all_links = re.findall('https://[A-Za-z0-9/.\-_=%]+', content)
		all_links = re.findall('https?://[A-Za-z0-9/.\-_\=\%;]+', content)
		links = list(dict.fromkeys(all_links))
		# self.remove_common_links()
		return links
	def __repr__(self):
		return '<SERP Engine object({})>'.format(self.base_url)
	def __str__(self):
		return repr(self)


# Available utilities
from serp_bot import google, yahoo#, lycos, yandex, aol, bing, ddg, excite,
class SERPBot:
	def __init__(self):
		self.lock = None
		self.workers = 4
		self.engines_list =  {
			# 'aol' : aol.engine,
			# 'bing' : bing.engine,
			# 'duckduckgo' : ddg.engine,
			# 'excite' : excite.engine,
			'google' : google.engine,
			# 'lycos' : lycos.engine,
			'yahoo' : yahoo.engine,
			# 'yandex' : yandex.engine,
		}
	def get_engine(self, name):
		return self.engines_list[name]
	def get_random_search_engine(self):
		choices = list(self.engines_list.keys())
		choice = random.choice(choices)
		return self.engines_list[choice]
	def run(self, phrase, task = None):
		# Strategy : Each domain is hit at an interval of 1 second after completion
		# A random User Agent is made use of.
		# Another strategy is to keep hashes of engine name and User agents
		# and compare it, to determine if it should be triggered.
		# That is slightly more expensive in terms of computation
		engines = self.engines_list.items()
		instance_queue = []
		for engine in engines:
			instance = {}
			instance['engine_name'] = engine[0]
			instance['engine'] = engine[1]
			instance['iteration'] = 0
			instance['']
