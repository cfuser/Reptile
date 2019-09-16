import urllib
import urllib.request
import os
import re   #正则表达式
from time import sleep  # 根据需要导入，控制下载速度

# 根据url解析包含图片的页面
def load_srt(url):
    request = urllib.request.Request(url)   #发送网络请求
    response = urllib.request.urlopen(request)  # 根据url打开页面
    data = response.read() # 获取页面的响应数据
    return data

# 根据图片对应的html链接下载图片
def get_srt(html):
    regx = r'/course[\S].srt'   # 定义正则表达式，匹配页面jpg图片元素
    pattern = re.compile(regx)  # 编译表达式，构造匹配模式
    print(pattern)
    # 进行正则匹配，返回包含jpg图片的所有链接
    get_srt_assemble = re.findall(pattern,repr(html))
    num = 1
    #print(repr(html))
    print(get_srt_assemble)
    #遍历取出以上所获取的图片
    for srt in get_srt_assemble:
        # 解析img变量取出的图片链接，赋给image变量
        print("work")
        srtfile = load_srt(srt)
        # 将图片存入指定文件夹，并以从1开始递增的数字命名jpg图片
        address='D:\\课\\MIT\\6.858Computer Systems Security\\'
        video='MIT6_858F14_lec'+"%02d" % num+'_300k.mp4'
        srtToDown='MIT6_858F14_lec'+"%02d" % num+'_300k.srt'
        if os.path.exists(address+video):
            with open( address+srtToDown,'wb') as fb:
                fb.write(srtfile) # fb相当于open(...);# wb：以二进制方式打开
                print("正在下载"+srtToDown)
                print("下载结束"+srtToDown)
                num = num+1
    print("下载完成！")

url = 'https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-858-computer-systems-security-fall-2014/video-lectures/'
# 调用：解析url页面的方法
html = load_srt(url)
# 调用：下载图片的方法
get_srt(html)