import hashlib

def hashIt(type_hash):
	it =''
	if type_hash == 'md5':
		it = hashlib.md5(enc_wrd.strip())
	elif type_hash == 'sha256':
		it = hashlib.sha256(enc_wrd.strip())
	else: 
		print("Not compatible")

	digest = it.hexdigest()
	return digest

flag = 0

pass_hash = input("Enter hash: ")

type_hash = input("What hash? (md5, sha256)")


try: 
	pass_file = open("List.txt","r")
except:
	print("No file found")
	quit()
for word in pass_file:
		#encode to UTF8
		enc_wrd = word.encode('utf-8')
		#Hashing test then Making into hexa-decimal or hexadigest
		digest = hashIt(type_hash)
		
		if digest == pass_hash:
			print("Password: " +word)
		
			flag = 1
			break
if flag == 0:
	print("Not found")




	