import sys 
import os 
import re


starts_with = "<?php include_once('2015_templates/_includes/header.php') ?>\n" + \
              "<?php include_once('2015_templates/_includes/nav.php') ?>\n"
ends_with =   "<?php include_once('2015_templates/_includes/footer.php') ?>"



for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        if (name.endswith('.html') or name.endswith('.php')):
            inFile = open(os.path.join(root, name))
            text = inFile.read()
            inFile.close()
            os.rename(os.path.join(root, name), os.path.join(root, '_'+name))

            startIndex = text.find("<!-- startprint -->")
            if startIndex == -1:
				continue 
            stopIndex = text.find("<!-- stopprint -->")
           	''' Im assuming if there is a start tag there will also be an end tag '''
            newText = starts_with + text[(startIndex+len("<!-- startprint -->")):stopIndex] + ends_with
            filtered = filter(lambda x: not re.match(r'^\s*$', x), newText)

            outFile = open(os.path.join(root, name.split('.')[0] + ".php"), "w") 
            outFile.write(newText)
            outFile.close() 
        else: 
            continue