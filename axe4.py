# encoding: utf-8
import requests
import re

pattern = u'<td>(.+?)</td>'
result = []
# session = requests.session()

def get_data(url):
    global result, session
    resp = requests.get(url,
        headers={
            'Referer':'http://axe-level-4.herokuapp.com/lv4/',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
        })
    resp.encoding = 'utf-8'
    data = re.findall(pattern, resp.text)[3:]
    result += [data[i:i + 3] for i in range(0, len(data), 3)]


for i in range(1,25):
    get_data('http://axe-level-4.herokuapp.com/lv4/?page=%s' % i)

line = u'{"town": "%s", "village": "%s", "name": "%s" }'
lines = [line % tuple(r) for r in result]
output = "[%s]" % ",\n".join(lines)
print(output)
