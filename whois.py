import os

def get_whois(url):
	command="whois "+url
	process=os.popen(command)

	print("Performing whois on "+ url)
	result=str(process.read())
	print("Results obtained.")
	return result

print("Initalizing whois module...")