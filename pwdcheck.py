import hashlib
import requests
import sys

def api_check(pwd):
	shapwd=hashlib.sha1(pwd.encode('utf-8')).hexdigest().upper()
	first5,tail=shapwd[:5],shapwd[5:]
	reponse=request_api(first5)
	return count(reponse,tail)
def request_api(query):
	url='https://api.pwnedpasswords.com/range/'+query
	res=requests.get(url)
	if(res.status_code!=200):
		raise RuntimeError("Error fetching")
	return res
def count(response,to_check):
	response=(line.split(':')for line in response.text.splitlines())
	for h,v in response:
		if(h==to_check):
			return v
	return 0
#to check by command line
# b=sys.argv[1:]
# for word in b:
# 	ct=api_check(word)
# 	if ct:
# 		print('the given password {} was found {}times..\nconsider change your password'.format(word,ct))
# 	else:
# 		print('good password:{}\n carry on'.format(word))

#the passwords should be stored in the to check.txt file with spaces left
with open("tocheck.txt","r") as file:
	ip=file.read()
	ip=ip.split()
	for word in ip:
		ct=api_check(word)
		if ct:
			print('the given password {} was found {}times..\nconsider change your password'.format(word,ct))
		else:
			print('good password:{}\n carry on'.format(word))
