import os


def create_dir(directory):		#Creating directory if it doesn't exist
	if not os.path.exists(directory):
		print("Directory doesn't exist. Creating new directory.")
		os.makedirs(directory)

def write_file(path,data):		#Appending data to file specified by "path"
	file=open(path,'w')
	print("File"+ path +" exists. Appending to file.")
	file.write(data)
	file.close()

print("Creating Directory...")