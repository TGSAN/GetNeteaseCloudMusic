#coding:utf-8
import urllib2
import json
import md5
import re
import sys
def encrypted_id(id):
    byte1 = bytearray('3go8&$8*3*3h0k(2)2')
    byte2 = bytearray(id)
    byte1_len = len(byte1)
    for i in xrange(len(byte2)):
        byte2[i] = byte2[i]^byte1[i%byte1_len]
    m = md5.new()
    m.update(byte2)
    result = m.digest().encode('base64')[:-1]
    result = result.replace('/', '_')
    result = result.replace('+', '-')
    return result
if len(sys.argv)<=1:
    print "\r\nURL EMPTY!\r\nPlease using same like 163.py <url>"+"\r\n"
    exit()
url = sys.argv[1]
id = re.findall(r"(?:.*)[^user]id=(\d+)\D*",url)
print "\r\n"+str(id[0])
print "\r\nInfo:"
try:
    id = id[0]
except:
    print "\r\nURL ERROR!\r\nPlease using same like 163.py <url>"+"\r\n"
    exit()
req = urllib2.urlopen("http://music.163.com/api/song/detail/?id=" + id + "&ids=%5B" + id + "%5D")
jsondata = json.loads(req.read())
try:
    dfsid = jsondata['songs'][0]['hMusic']['dfsId']
    print "SplRate:"+str(jsondata['songs'][0]['hMusic']['sr'])+"Hz"
    print "BitRate:"+str(jsondata['songs'][0]['hMusic']['bitrate']/1000)+"kbps"
except:
    try:
        dfsid = jsondata['songs'][0]['mMusic']['dfsId']
        print "SplRate:" + str(jsondata['songs'][0]['mMusic']['sr']) + "Hz"
        print "BitRate:" + str(jsondata['songs'][0]['mMusic']['bitrate'] / 1000) + "kbps"
    except:
        try:
            dfsid = jsondata['songs'][0]['lMusic']['dfsId']
            print "SplRate:" + str(jsondata['songs'][0]['lMusic']['sr']) + "Hz"
            print "BitRate:" + str(jsondata['songs'][0]['lMusic']['bitrate'] / 1000) + "kbps"
        except:
            try:
                dfsid = jsondata['songs'][0]['bMusic']['dfsId']
                print "SplRate:" + str(jsondata['songs'][0]['bMusic']['sr']) + "Hz"
                print "BitRate:" + str(jsondata['songs'][0]['bMusic']['bitrate'] / 1000) + "kbps"
            except:
                print "Not Found Any Sound File"+"\r\n"
                exit()
en_id = encrypted_id(str(dfsid))
name = jsondata['songs'][0]['name']
name = name.encode("UTF8")
albname = jsondata['songs'][0]['album']['name']
albname = albname.encode("UTF8")
artists = jsondata['songs'][0]['artists'][0]['name']
artists = artists.encode("UTF8")
print "\r\n"+name+"\r\n"+artists+"\r\n"+albname
musicurl = "http://m2.music.126.net/"+ en_id + "/" + str(dfsid) + ".mp3"
print "\r\nDownload:"
print musicurl+"\r\n"
exit()