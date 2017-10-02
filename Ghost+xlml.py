# Python
#_*_ coding:'utf-8' _*_

import urllib
from ghost import Ghost
import lxml.html

login_url = 'https://www.dmv.ca.gov/wasapp/foa/findDriveTest.do'
data = {
    'numberItems':'1',
    'officeId':'618',
    'requestedTask':'DT',
    'firstName':'zhe',
    'lastName':'tang',
    'dlNumber':'Y8538769',
    'birthMonth':'10',
    'birthDay':'06',
    'birthYear':'1996',
    'telArea':'626',
    'telPrefix':'731',
    'telSuffix':'8573',
    'resetCheckFields':'true'
}
ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2526.106 Safari/537.36'
url = login_url + '?' + urllib.urlencode(data)

# ghost
gh = Ghost()
ghost = gh.start(wait_timeout=60)
page,res = ghost.open(url, user_agent=ua)
#text  = ghost.content
#print text

# lxml

html = lxml.html.fromstring(ghost.content)
time = html.xpath('//body/div[2]/div[2]/form[2]/div/div[2]/table/tbody/text()')




# Reference
# https://my.oschina.net/1123581321/blog/411943
