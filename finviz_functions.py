import requests
import urllib3

http = urllib3.PoolManager()

def get_url(url, header):
    response = http.request('GET', url, headers=header)

    if response.status == 503:
        print (response.text)
    if response.status == 200:
        return (response)
        # return response.text

site_url = 'https://finviz.com/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}

get_url_response = get_url(site_url, header)

print (get_url_response)
