import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'https://finviz.com/')
r.status
# r.data
print(r.status)
# print(r.data)
