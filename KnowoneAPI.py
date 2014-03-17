import re
import urllib2

def getHtml(url):
    reponse = urllib2.urlopen(url)
    return reponse.read()


html = getHtml("http://knewone.com/things")

reg_detail = re.compile('<div class="thing">.+?<a href="(.+?)" target="_blank"',re.MULTILINE)
reg_picurl  =re.compile('<img alt=".+?" class="lazy" data-original="(.+?)"',re.MULTILINE)
reg_description = re.compile('<h5 data-placement="top" data-toggle="tooltip" title="(.+?)">.+?</h5>',re.MULTILINE)

details = re.findall(reg_detail,html)
picurls = re.findall(reg_picurl,html)
descriptions = re.findall(reg_description,html)
# print len(res)
# for c in res :
#     print c

# print len(picurls)
# for c in picurls :
#     print c

print len(descriptions)
for c in descriptions :
    print c