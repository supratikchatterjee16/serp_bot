from serp_engines import SERPBot, RequestDispatcher

bot = SERPBot()
dispatcher = RequestDispatcher()
engine = bot.get_random_search_engine()
print(engine)
engine.build_base_query('hello world')
print(engine.get_current_url())
dispatcher.get(engine.get_current_url()[0])
print(dispatcher.last_response.text)
with open('sample.html', 'w+') as html_file:
	html_file.write(dispatcher.last_response.text)
