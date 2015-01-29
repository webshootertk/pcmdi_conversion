import sys 
import os 

starts_with = "<?php include_once('2015_templates/_includes/header.php') ?>\n" + \
              "<?php include_once('2015_templates/_includes/nav.php') ?>\n"
ends_with =   "<?php include_once('2015_templates/_includes/footer.php') ?>"



for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        if (name.endswith('.html') or name.endswith('.php')):
            inFile = open(os.path.join(root, name))
            os.rename(os.path.join(root, name), os.path.join(root, '_'+name))
            text = inFile.read()
            startIndex = text.find("<!-- startprint -->") 
            stopIndex = text.find("<!-- stopprint -->") 
            newText = starts_with + text[(startIndex+len("<!-- startprint -->")):stopIndex] + ends_with 
            outFile = open(os.path.join(root, name.split('.')[0] + ".php"), "w") 
            outFile.write(newText) 
        else: 
            continue
