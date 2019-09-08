from requests_html import HTMLSession

import asyncio

loop = asyncio.get_event_loop()

session = HTMLSession()
resp = session.get('http://gdnd.wikidot.com/races')
resp.html.render(keep_page=True)
 

c = resp.html.page.setViewport({'width': 1024, 'height': 768})
loop.run_until_complete(c)

page = resp.html.page

loop.run_until_complete(page.screenshot({'path': '5eraces.png'}))

core = resp.html.find('.list-pages-box', first=True)


races = core.text
print(races)