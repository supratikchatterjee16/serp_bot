# https://search.aol.com/aol/search?q=hello+world&pz=100&b=301
# Change b=n to get the page number.
from serp_engines import GenericSearchEngine
class AOLEngine(GenericSearchEngine): # This is copied from google. Change
	def __init__(self):
		self.protocol = 'https://'
		self.base_url = 'www.google.com'
		self.search_extension = 'search'
		self.query_key = 'q`'
		self.index_key = 'start'
		self.key_seperator = '&'
		self.search_seperator = '+'
		self.index = 1
		self.increment_factor = 10
		self.additional = '' # This must start with a & symbol
		self.cooldown = 60

engine = AOLEngine()
