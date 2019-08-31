from requests_html import HTMLSession

import asyncio

loop = asyncio.get_event_loop()

session = HTMLSession()
resp = session.get('https://python.org/')
resp.html.render(keep_page=True)
 

c = resp.html.page.setViewport({'width': 1024, 'height': 768})
loop.run_until_complete(c)

page = resp.html.page

loop.run_until_complete(page.screenshot({'path': 'example.png'}))
