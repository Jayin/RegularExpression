import re
import urllib2

def getHtml(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html

html = getHtml("http://news.dbanotes.net/")
reg_title = re.compile(r'<td class="title"><a target="_blank" href=".+?"(?: rel="nofollow")?>(.+?)</a>',re.MULTILINE)
reg_url   =re.compile(r'<td class="title"><a target="_blank" href="(.+?)"(?: rel="nofollow">|>)',re.MULTILINE)
titles = re.findall(reg_title,html)
urls   = re.findall(reg_url,html)

print "title:",len(titles)
for title in titles :
    print title
print "urls:",len(urls)
for url in urls:
    print url
