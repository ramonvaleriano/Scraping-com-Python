from requests_html import HTMLSession
from requests_html import Element, HTML

url = 'http://sintegra.sefaz.to.gov.br/sintegra/servlet/wpsico01'
doc = 'http://sintegra.sefaz.to.gov.br/sintegra/servlet/wpsico01'
script_ = """<script type="text/javascript" src="/sintegra/static/messages.por.js?90633"></script>"""
script_2 = """<script type="text/javascript" src="/sintegra/static/wpsico01.js?20169616563092"></script>"""


"""session = HTMLSession()
response = session.get(doc)
response.html.render()
resp = response.html.xpath(selector='script',clean=False)"""



session = HTMLSession()
response = session.post('http://sintegra.sefaz.to.gov.br/sintegra/servlet/wpsico01')
response.html.render()
print(response.cookies)




