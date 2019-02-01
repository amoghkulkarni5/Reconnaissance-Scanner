from tld import get_tld
from tld import get_fld

def get_domain_name(url):
	print("Getting Domain Name...")
	domain_name=get_fld(url)
	return domain_name

print("Initializing Domain Module...")