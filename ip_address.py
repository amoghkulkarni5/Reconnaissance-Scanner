import os

def get_ip_address(domain_name):
	command= "host "+ domain_name	#command "host google.com", will return IP, IPv6 and other data

	#Eg:
	#$- host facebook.com
	#facebook.com has address 157.240.16.35
	#facebook.com has IPv6 address 2a03:2880:f12f:83:face:b00c:0:25de
	#facebook.com mail is handled by 10 msgin.vvv.facebook.com.

	process= os.popen(command)		#perform command and store result in process
	results=str(process.read())		#Read the result we get in process variable, convert process to string variable

	print("IP Found!")
	marker=results.find('has address')+12 
	#finds 'has address' substring in results, and returns the index of "h"
	#We add 12 beccause we want index of start of IP address.

	print("Getting first IP...")
	return results[marker:].splitlines()[0]
	#splitlines is called only to give one IP address, as the domain can be hosted by multiple IPS.

	#    Working: Consider 
	#$- host facebook.com
	#facebook.com has address 157.240.16.35
	#facebook.com has address 157.234.135.65
	#facebook.com has IPv6 address 2a03:2880:f12f:83:face:b00c:0:25de
	#facebook.com mail is handled by 10 msgin.vvv.facebook.com.

	# results[marker:] gives us all indexes from marker position to last
	#splitlines converts it to a list where the first element is till \0, ie, till the end of IP, and we return it.

print("Initalizing IP module...")