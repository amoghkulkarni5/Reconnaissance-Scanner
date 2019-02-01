import os

def get_nmap(options,IP):
	options=options+" "
	command= "nmap "+ options + IP
	print("Starting nmap")
	process=os.popen(command)
	print("Nmap scan results obtained.")
	result=str(process.read())

	return result

print("Initalizing nmap...")