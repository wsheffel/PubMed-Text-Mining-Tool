pmidList = "".join(open("[3]pmidList.txt", 'r').readlines()).split('\n')
pmidList.pop(); #remove last one which is ''
head = """<html>
<head>
<title>
PMID List
</title>
</head>
<body>"""
print head
urlHead = '<h3> #> <a href="'
urlTail = "</h3></a>"
for pmid in pmidList:
    _pmid, title = pmid.split('!!')
    entry = urlHead + _pmid[5:-1] + '" target="_blank">' + _pmid[5:-1] + urlTail
    print "<h3>" + title[7:-1] + "</h3>"
    print entry

tail = """
</body>
</html>"""
print tail