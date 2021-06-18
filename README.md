# SERP Bot

This is a utility that has gives the basic use of scraping web engines. This is simple in the way it works, however, just using some common sense would allow you to make some rather advanced uses of this.

Caution : SERP bots are a legal gray zone.

This can be installed through pip.
```shell
pip install serp-bot
```

Alternatively, you could download this repository and install it with pip.
```shell
pip3 install .
```

## Using

This has 3 components that can be made use of. SERPBot, GenericSearchEngine and RequestDispatcher.

Sample usage :
```python
from serp_bot import SERPBot, RequestDispatcher

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
```

Alternatively, using the RequestDispatcher can help avoid some Web Scraping detection units.

```python
from serp_bot import RequestDispatcher

request_dispatcher = RequestDispatcher()
response = request_dispatcher.get('https://google.com/search?q=crapper+zapper')
print(response.content)
```
