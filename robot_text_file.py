import urllib.request
import io

def get_robots_txt(url):
	if url.endswith('/'):
		path=url
	else:
		path=url+'/'
	print("Requesting robots.txt from "+url)
	req= urllib.request.urlopen(path+"robots.txt",data=None)		#Requests Robots.txt file from the URL

	#Robots.txt is a file which contains the pages which a web crawler should not crawl.
	#Web Crawler is used by search engines to locate pages within the website. 
	#Add pages to robots.txt to avoid crawler from showing them in search engine, 
	#as some pages contain sensitive data (Eg: Admin Login Page)
	data = io.TextIOWrapper(req, encoding='utf-8')		#Make sure data is encoded in standard utf-8 format
	print("Robots.txt obtained and encoded ('utf-8' format)")
	return data.read()

print("Initalizing Robot module...")