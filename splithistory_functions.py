import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'https://www.splithistory.com/')
r.status
# r.data
print(r.status)
# print(r.data)