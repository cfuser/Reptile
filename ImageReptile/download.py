import requests
 
hd = {
    'Connection':'keep-alive',
    'Host':'upos-hz-mirrorkodo.acgvideo.com:443',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}

start='https://archive.org/download/MIT6.858F14/'

for i in [2,6,10,11,23]:
    lecture='MIT6_858F14_lec'+"%02d" % i+'_300k.mp4'
    print(lecture+"开始下载")
    url=start+lecture
    #url = 'https://archive.org/download/MIT6.858F14/MIT6_858F14_lec01_300k.mp4'
    
    r = requests.get(url, headers=hd, stream=True)
    with open('D:\\课\\MIT\\6.858Computer Systems Security\\'+lecture, "wb+") as mp4:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                mp4.write(chunk)
    
    print(lecture+"下载结束")
