import sys 
import os 


for root, dirs, files in os.walk(".", topdown=True):
	for name in files:
		if name[0] == '_':
			print name
		elif name[-4:] == '.php':
				os.remove(os.path.join(root, name))
				print 'removing ' + name

for root, dirs, files in os.walk(".", topdown=True):
	for name in files:
		if name[0] == '_':
			os.rename(os.path.join(root, name), os.path.join(root, name[1:]))
		else: 
			continue

if os.path.isfile('manual_review.txt'):
	os.remove('manual_review.txt')
