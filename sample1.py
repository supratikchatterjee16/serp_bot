from serp_bot import RequestDispatcher

request_dispatcher = RequestDispatcher()
response = request_dispatcher.get('https://google.com/search?q=crapper+zapper')
print(response.content)
