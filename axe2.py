# encoding: utf-8
import requests
import re

pattern = u'<td>(.+?)</td>'
result=[]

class ParseEnd(Exception):
    pass

def get_data(url):
    global result
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    data = re.findall(pattern, resp.text)[3:]
    if len(data) == 0:
        raise ParseEnd()
    result += [data[i:i + 3] for i in range(0, len(data), 3)]

page=1
try:
    while True:
        get_data('http://axe-level-1.herokuapp.com/lv2/?page=%s' % page)
        page+=1
except ParseEnd:
    pass

line = u'{"town": "%s", "village": "%s", "name": "%s" }'
lines = [line % tuple(r) for r in result]
output = "[%s]" % ",\n".join(lines)
print(output)
