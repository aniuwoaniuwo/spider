#-*-coding:utf-8-*-
import re
str='''<h3><strong>
注册一亩三分地论坛，查看更多干货！</strong></h3>
<p>您需要 <a href="member.php?mod=logging&amp;action=login" onclick="showWindow('login', this.href);return false;">登录</a> 才可以下载或查看，没有帐号？<a href="member.php?mod=xregister" title="注册帐号">注册账号</a> 
<a href="javascript:;" onclick="showWindow('wq_login_qrcode', 'plugin.php?id=wq_login&mod=scan')"><img src="source/plugin/wq_login/static/images/wechat_login.png" class="vm" /></a>
</p>
</div>
<span class="atips_close" onclick="this.parentNode.style.display='none'">x</span>
</div>
最近几年无数次搬家，一般只带衣服，书，电脑所有家具，大东西，就地处理掉，轻装上阵去下一个城市，开始全<a href="http://www.1point3acres.com/bbs/thread-259262-1-1.html" target="_blank" class="relatedlink">新生</a>活。<font class="jammer"></font><br />
我个人一般就是散给有需要的朋友，或者捐掉了，可以抵税，有空在craigslist上面卖也可以。<font class="jammer"></font><br />
<font class="jammer"></font><br />
基本所有其他家具，都是去新地方，一个<a href="http://www.amazon.com/b?_encoding=UTF8&tag=1p3a-guanlian-20&linkCode=ur2&linkId=89c11e2c5b86155c5422f19cca1e9880&camp=1789&creative=9325&node=5" target="_blank" class="relatedlink">Amazon</a> order解决大部分问题<font class="jammer"></font><br />
不见得是最便宜的，比从target可能略贵一点<font class="jammer"></font><br />
但是好处是*非常非常*方便，不需要deal with 打包，搬家种种麻烦。<font class="jammer"></font><br />
基本没有down time，也不需要去好几家店一直买买买<font class="jammer"></font><br />
更不需要亲自去店里搬运！省时省心！！！<font class="jammer"></font><br />
<font class="jammer"></font><br />
送货一定要用<a href="http://www.amazon.com/tryprimefree&amp;tag=1point3acres-20" target="_blank">prime，有free trial</a>。<font class="jammer"></font><br />
prime 2 day shipping，要小心2天是order之后的两个business day，<font class="jammer"></font><br />
比如如果我周一到新城市，会之前一周的周二或者周三白天下单<font class="jammer"></font><br />
<font class="jammer"></font><br />
<font class="jammer"></font><br />
先开贴，内容慢慢填。<font color="#ff00ff">图片可点</font>。都是Amazon上被n多人好评的<font class="jammer"></font><br />
<font class="jammer"></font><br />
<br />
<span style="display:none"></span>《一》bedroom stuff <font class="jammer"></font><br />
<font class="jammer"></font><br />
保证马上有地方睡觉。床和床架，memory foam床垫 + 简易床架，不觉得比从前2000刀的床差多少<font class="jammer"></font><br />
<font class="jammer"></font><br />
'''
pattern='<.*?>'
comtent=re.sub(pattern,'',str)
print(comtent)
'''comtent1=str.replace('<br>','')
print(comtent1)'''