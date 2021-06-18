# https://in.search.yahoo.com/search?p=flockers+dockers&pz=10&ei=UTF-8&fr=yfp-t&fp=1&b=31&pz=10&pstart=2
# p is search keywords seperated by a +
# b is page index n * 10 + 1
from serp_bot import GenericSearchEngine
class YahooEngine(GenericSearchEngine):
	def __init__(self):
		self.protocol = 'https://'
		self.base_url = 'in.search.yahoo.com'
		self.search_extension = 'search'
		self.query_key = 'p'
		self.index_key = 'b'
		self.key_seperator = '&'
		self.search_seperator = '+'
		self.index = 1
		self.increment_factor = 10
		self.additional = '' # This must start with a & symbol
		self.cooldown = 60
		# bare is https://in.search.yahoo.com/search?p=flockers+dockers&b=31

engine = YahooEngine()
