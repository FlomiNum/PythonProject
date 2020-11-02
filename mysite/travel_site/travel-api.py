from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryList'
queryParams = '?' + urlencode({
quote_plus('ServiceKey') : '27O0k589oA5o%2BF5kUfkJP2%2BwG0HHH49h38HZuJVS%2BFyPFOmAJpcXakTCbIcMEVp3nJFH8%2BmQeykai%2FNzdvq8Hg%3D%3D',
quote_plus('pageNo') : '1',
quote_plus('numOfRows') : '10',
quote_plus('MobileOS') : 'ETC',
quote_plus('MobileApp') : 'AppTest',
quote_plus('arrange') : 'A' 
})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)