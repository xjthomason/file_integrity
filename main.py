import os, files, hasher, csv, datetime
#from progressbar import Percentage,ProgressBar,Bar,ETA

yesterday = datetime.date.today()
today = unicode(yesterday - datetime.timedelta(days=1))#datetime.date.today()

#fileshare = '\\\\gvfs01\\Datavol\\'
fileshare = '/media/sf_Faux_File_Share/'
#fileshare = '/home/rick/Documents/'

#output_path = '/home/rick/'	
#output_path = 'C:\\Users\\alienvault_AD\\Desktop\\'
output_path = '/root/'

def main():
	global fileshare
	
	os.system('rm %s' % output_path + 'file_share_audit_%s.csv' % today)
	
	# pbar = ProgressBar(widgets=[Bar('>', '[', ']'), '', Percentage(), '', ETA()],
						# maxval=N).start()
	
	with open('file_share_audit_%s.csv' % today, 'wb') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = ['filename', 'hash'])
		writer.writeheader()
	
		try:
			#dirList.append(os.listdir(fileshare))
			for root, dirs, files in os.walk(fileshare):
				for file in files:
					path = os.path.join(root, file)
					md5 = hasher.hasher(path)
					writer.writerow({'filename': file,
									 'hash': md5})

		except Exception, e:
			print e
			writer.writerow({'filename': "ACCESS DENIED"})
			pass
	
	#os.system('copy file_share_audit.csv C:\\Users\\alienvault_AD\\Desktop\\')
	#os.system('del file_share_audit.csv')
	os.system('cp file_share_audit_%s.csv %s' % (today, output_path))
	os.system('rm file_share_audit_%s.csv' % today)

main()
