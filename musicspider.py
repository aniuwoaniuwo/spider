#-*-coding:utf-8-*-
import urllib.request
import requests

url='http://music.163.com/song/media/outer/url?id=64006'
#https://m10.music.126.net/20181117110048/4b06c02be820d01382ff74a2b8d4294a/ymusic/508f/c8ec/bd88/105f8a6e29a8bc135a0b0bdc80bbe7d2.mp3
#https://m10.music.126.net/20181117111324/dc471894a89a19a71f5d909d76d02346/ymusic/dbe5/8fad/6669/fa79f603372adf2b745d7c3d84d898a5.mp3
#https://m10.music.126.net/20181117111342/899a95cb07aba47ccd8610f1678f27db/ymusic/e96f/4285/b663/132e9b267041c5f473243df2b30576eb.mp3
urllib.request.urlretrieve(url,'c:\\pachong\\'+'1.mp3')
'''with open('C:/pachong/'+'555.mp3', 'wb') as f:
    f.write(requests.get(url).content)'''
#https://music.163.com/#/search/m/?s=%E9%99%88%E5%A5%95%E8%BF%85&type=1
#https://m10.music.126.net/20181115161329/f3eef7c6c3e945b932f59222d0e0d645/ymusic/a3c6/87ff/4bdb/58a9fc1e0ed73e96c6324439c8ac0783.mp3
#https://m10.music.126.net/20181115161446/427480d1f116dc00073427fd1dc6b207/ymusic/a3c6/87ff/4bdb/58a9fc1e0ed73e96c6324439c8ac0783.mp3
#https://m10.music.126.net/20181115161519/39b0754b05d842ad63e3658e5c3d1e10/ymusic/a158/036f/7274/427fef3e26d6fe0adaff9e86ee3760b4.mp3
#https://m10.music.126.net/20181115164033/175089ce634890afd9c2ce16a576a9df/ymusic/b3ef/a73b/2912/6aaf5fef2aac1e1ccbaca792918c456a.mp3