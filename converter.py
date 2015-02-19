import sys 
import os 
import re


starts_with = "<?php include_once('2015_templates/_includes/header.php') ?>\n" + \
              "<?php include_once('2015_templates/_includes/nav.php') ?>\n"
ends_with =   "\n<?php include_once('2015_templates/_includes/footer.php') ?>"

file_count = 0

def writeOut(text, name):
    #file_count += 1
    text = starts_with + text + ends_with
    filtered = filter(lambda x: not re.match(r'^\s*$', x), text)
    outFile = open(os.path.join(root, name.split('.')[0] + '.php'), 'w') 
    outFile.write(text)
    outFile.close()

def writeReview(name, root):
    print 'Adding ' + name + ' to manual review'
    listFile = open(os.path.join('.', 'manual_review.txt'), 'a')
    listFile.write(os.path.join(root,name) + '\n')
    listFile.close()


for root, dirs, files in os.walk(".", topdown=True):
    
    for name in files:
        if (name.endswith('.html') or name.endswith('.php')):
            inFile = open(os.path.join(root, name))
            text = inFile.read()
            inFile.close()
            os.rename(os.path.join(root, name), os.path.join(root, '_'+name))

            startIndex = text.find("<!-- startprint -->")
            if startIndex == -1:
                newText = text
                writeReview(name, root)
                writeOut(newText, name)
                continue
            stopIndex = text.find("<!-- stopprint -->")
            newText = text[(startIndex+len("<!-- startprint -->")):stopIndex]
            writeOut(newText, name)
        else: 
            continue


print "total file count: " + str(file_count)

