# encoding: utf-8
import requests
import re

pattern = u'<td>(.+?)</td>'
result = []
session = requests.session()

def get_data(url):
    global result, session
    resp = session.get(url)
    resp.encoding = 'utf-8'
    data = re.findall(pattern, resp.text)[3:]
    result += [data[i:i + 3] for i in range(0, len(data), 3)]


get_data('http://axe-level-1.herokuapp.com/lv3/')
for i in range(75):
    get_data('http://axe-level-1.herokuapp.com/lv3/?page=next')

line = u'{"town": "%s", "village": "%s", "name": "%s" }'
lines = [line % tuple(r) for r in result]
output = "[%s]" % ",\n".join(lines)
print(output)
