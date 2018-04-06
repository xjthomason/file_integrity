import os, hashlib, variables

BUF_SIZE = 65536

def hasher(file):
	
	fileshare = variables.fileshare
	md5 = hashlib.md5()
	
	try:
		hash = hashlib.md5()
		with open('%s%s' % (fileshare, file), 'rb') as f:
			while True:
				data = f.read(BUF_SIZE)
				if not data:
					break
				result = md5.update(data)
			return result
	except Exception, e:
		print e
		pass
	
