import os

def pulldirectory(dirlist):

	for file in [item for item in dirlist if os.path.isfile(item)]:
		return file
