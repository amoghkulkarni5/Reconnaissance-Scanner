from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robot_text_file import *
from whois import *


def gather_info(name,url):

	robottext= get_robots_txt(url)
	domain_name= get_domain_name(url)
	ip_address=get_ip_address(domain_name)
	nmap= get_nmap('-F', ip_address)
	who= get_whois(domain_name)

	create_report(name,url,domain_name,nmap,robottext,who)

def create_report(name,url,domain_name,nmap,robottext,who):

	project_dir= ROOT_DIR + "/" + name
	create_dir(project_dir)

	write_file(project_dir + "/full_url.txt",url)
	write_file(project_dir + "/domain-name.txt",domain_name)
	write_file(project_dir + "/nmap.txt",nmap)
	write_file(project_dir + "/robots.txt",robottext)
	write_file(project_dir + "/whois.txt",who)



ROOT_DIR = 'Websites'
create_dir(ROOT_DIR)
name= input("Enter Name: ")
url= input("Enter URL: ")
gather_info(name,url)