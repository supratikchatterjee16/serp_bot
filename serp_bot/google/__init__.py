# https://www.google.com/search?q=hello+world
from serp_bot import GenericSearchEngine
class GoogleEngine(GenericSearchEngine):
	def __init__(self):
		self.protocol = 'https://'
		self.base_url = 'www.google.com'
		self.search_extension = 'search'
		self.query_key = 'q'
		self.index_key = 'start'
		self.key_seperator = '&'
		self.search_seperator = '+'
		self.index = 1
		self.increment_factor = 10
		self.additional = '' # This must start with a & symbol
		self.cooldown = 60

engine = GoogleEngine()
