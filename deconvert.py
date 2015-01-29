import sys 
import os 


for root, dirs, files in os.walk(".", topdown=True):
	for name in files:
		if os.path.join(root, name).startswith('_'):
			os.rename(os.path.join(root, name), os.path.join(root, name[1:]))
		else: 
			continue
