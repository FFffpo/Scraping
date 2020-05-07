from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup
from io import open

#wordFile = urlopen('http://pythonscraping.com/pages/AWordDcument.docx').read()
wordFile = open('C:/Users/jzwdq/Desktop/aa.docx', 'rb').read()

wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'xml')
testStrings = wordObj.find_all('w:t')

for textElem in testStrings:
    style = textElem.parent.parent.find('w:pStyle')
    if style is not None and style['w:val'] == 'Title':
        print('Title is: {}\n'.format(textElem.text))
    # else:
        # print(textElem.text)

for textElem in testStrings:
    print(textElem.text)
