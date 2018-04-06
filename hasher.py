import os, hashlib

BUF_SIZE = 65536

def hasher(file):
	
	#fileshare = variables.fileshare
	
	try:
		hash = hashlib.md5()
		with open('%s' % (file), 'rb') as f:
			#while True:
			for block in iter(lambda: f.read(BUF_SIZE), b""):
				hash.update(block)
		return hash.hexdigest()
	except Exception, e:
		print e
		pass

	
