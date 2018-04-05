import os, files, hasher, csv
from progressbar import Percentage,ProgressBar,Bar,ETA

fileshare = '\\\\gvfs01\\Datavol\\'

def main():
	global dirList
	global fileshare
	
	# pbar = ProgressBar(widgets=[Bar('>', '[', ']'), '', Percentage(), '', ETA()],
						# maxval=N).start()
	
	with open('file_share_audit.csv', 'wb') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = ['filename', 'hash'])
		writer.writeheader()
	
	try:
		#dirList.append(os.listdir(fileshare))
		for root, dirs, files in os.walk(fileshare):
			for file in files:
				# TODO hash the file
				# TODO add hash to list
				#hash = hasher(file)
				writer.writerow({'filename': file})#hash: hash
	except:
		writer.writerow({'filename': "ACCESS DENIED"})
		pass
	
	os.system('copy file_share_audit.csv C:\\Users\\alienvault_AD\\Desktop\\')
	os.system('del file_share_audit.csv')

main()
