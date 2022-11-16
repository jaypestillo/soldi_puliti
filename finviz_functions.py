#import
try: 
    import urllib3
    from bs4 import BeautifulSoup
except ImportError:
    print ("Error importing")


http = urllib3.PoolManager()

def get_url(url, header):
    response = http.request('GET', url, headers=header)

    if response.status == 503:
        print (response.status)
    if response.status == 200:
        # return response object
        return (response)

def struct_response(response):
    response_body = BeautifulSoup(get_url_response.data, features="html.parser")
    return (response_body)

def get_tickers(html):
    array = [1,2,3]
    return (array)

site_url = 'https://finviz.com/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}

get_url_response = get_url(site_url, header)
html_struct = struct_response(get_url_response)
ticker_array = get_tickers(html_struct)

# response_status = get_url_response.status
# response_headers = get_url_response.headers

# print (html_struct)
print (ticker_array)
