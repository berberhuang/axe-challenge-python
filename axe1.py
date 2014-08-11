# encoding: utf-8
import requests
import re

resp = requests.get('http://axe-level-1.herokuapp.com')
resp.encoding = 'utf-8'
pattern = u'<td>.+?</td>'
data = re.findall(pattern, resp.text)[6:]
p_data = [re.sub('</?td>', '', d) for d in data]
result = [p_data[i:i + 6] for i in range(0, len(p_data), 6)]

line = u'{"name": "%s", "grades": {"國語": %s, "數學": %s, "自然": %s, "社會": %s, "健康教育": %s}}'
lines = [line % tuple(r) for r in result]
output = "[%s]" % ",\n".join(lines)
print(output)
