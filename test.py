#_*_ coding:'utf-8' _*_

import urllib
import urllib2
import cookielib
import re

class library:
    def __init__(self):
        self.self.loginURL='https://www.dmv.ca.gov/wasapp/foa/findDriveTest.do'
        self.Data = urllib.urlencode({
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
        })
        self.requestURL = self.loginURL + '?' + self.Data
        self.cookies=cookielib.CookieJar()
        self.handler=urllib2.HTTPCookieProcessor(self.cookies)
        self.opener=urllib2.build_opener(self.handler)



    def getPage(self):
        request = urllib2.Request(self.requestURL)
        result = self.opener.open(request)
        return result.read()
    def getInformation(self):
        page = self.getPage()
        pattern = re.compile('<table.*?id="tb.*?width="50%"><font size=2>(.*?)</font>.*?<tr>.*?<tr>.*?'+
                        '<font size=2>(.*?)</font>.*?<font size=2>(.*?)</font>.*?</TABLE>',re.S)
        items = re.findall(pattern,page)

        contents = []
        for item in items:
            content = item[0]+'    from   '+item[1]+'   to   '+item[2]+'\n'
            contents.append(content)
        self.writeData(contents)
    def writeData(self,contents):
        file = open('libraryBooks.txt','w+')
        for content in contents:
            file.write(content)
        file.close()

lib = library()
lib.getInformation()









2
3
4
5
6
7
8
9
10
11
import urllib

loginURL = 'http://202.118.250.131/lib/opacAction.do'
queryString = urllib.urlencode({
            'method':'DoAjax',
            'dispatch':'login',
            'registerName':'',
            'rcardNo':'16S137028 0',
            'pwd':'******'
            })
requestURL = self.loginURL + '?' + self.queryString
