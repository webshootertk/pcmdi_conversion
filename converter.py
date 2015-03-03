import sys 
import os 
import re

starts_with = "<?php include_once('/var/www/pcmdi-site/2015_templates/_includes/header.php') ?>\n" + \
              "<?php include_once('/var/www/pcmdi-site/2015_templates/_includes/nav-www-pcmdi.php') ?>\n"
ends_with =   "\n<?php include_once('/var/www/pcmdi-site/2015_templates/_includes/footer.php') ?>"


file_count = 0
html_count = 0
php_count = 0
manual_review_count = 0

def stripPhp(text):
    newText = text
    if "<?" in text:
        startIndex = text.find("<?")
        stopIndex = text.find("?>")
        newText = text[:startIndex]
        newText += text[:stopIndex]
    return newText

def writeOut(text, name):
    file_count += 1
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
            file_count += 1
            inFile = open(os.path.join(root, name))
            text = inFile.read()
            inFile.close()
            os.rename(os.path.join(root, name), os.path.join(root, '_'+name))
            text = stripPhp(text) 

            if "<!-- startprint -->" in text:
                if name.endswith('.html'):
                    html_count += 1
                elif name.endswith('.php'):
                    php_count += 1
                startIndex = text.find("<!-- startprint -->")
                stopIndex = text.find("<!-- stopprint -->")
                newText = text[(startIndex+len("<!-- startprint -->")):stopIndex]
                writeOut(newText, name)
            else:
                manual_review_count += 1
                writeReview(name, root)
                writeOut(text, name)
        else: 
            continue


print "\nTotal file count: " + str(file_count)
print ".html files converted: " + str(html_count)
print ".php files touched: " + str(php_count)
print "There are " + str(manual_review_count) + " files to be manually reviewed"

