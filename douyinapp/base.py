#分享主页获得的url，主页url
from lxml import etree
import requests
share_url='https://www.iesdouyin.com/share/user/83072448142'
#fiddler抓包获取的url，直接访问404
# video_url='https://www.iesdouyin.com/share/video/6721320262584814851/?region=CN&mid=6721577103768292109&u_code=k3im8mm6&titleType=titleshare_url=https://www.iesdouyin.com/share/video/6721320262584814851/?region=CN&mid=6721577103768292109&u_code=k3im8mm6&titleType=title'
#谷歌浏览器的抓包获取的，就是视频教学里的url
video_url='https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200fcd0000bjpq3av2gddtitq6ri40&line=0'
# video_url="https://www.iesdouyin.com/share/video/6721129212725513485/?region=CN&mid=6721189109739866892&u_code=k3im8mm6&titleType=title"
headers={"Host":"api-hl.amemv.com",
"Connection":"keep-alive",
# "Cookie":"install_id=80755043984; ttreq=1$e0c35ca8326f4064195f0f0cef96db69b464cf5d; odin_tt=55195865bc9d34e4e5d0777adead252f26b7ab6463270842ce4908b2428ee9e713a5fc693ef4de923133fdf41d7026e9ef457015f4236f7ea7a75c5fe91a2e38; qh[360]=1",
"Accept-Encoding":"gzip",
"sdk-version":"1",
"User-Agent":"com.ss.android.ugc.aweme/730 (Linux; U; Android 5.1.1; zh_CN; HUAWEI MLA-AL10; Build/HUAWEIMLA-AL10; Cronet/58.0.2991.0)",
"X-Gorgon":"0300b71d4001237cb4cc5a176a78a7d7c8f2862a8cfa600d9b33",
"X-Khronos":"1565002284",}
# headers={"Connection":"keep-alive",
# "Cache-Control":"max-age=0",
# "Upgrade-Insecure-Requests":"1",
# "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.142 Safari/537.36",
# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
# "Accept-Encoding":"gzip,deflate,br",
# "Accept-Language":"zh-CN,zh;q=0.9",}
response=requests.get(video_url,headers=headers)
print(response.text,response.status_code)
with open('douyin.mp4','wb') as f:
    f.write(response.content)
import requests

# response=requests.get('https://www.iesdouyin.com/share/user/83072448142',headers=headers).text
# print(response)
response='''<!DOCTYPE html><html><head>  <meta charset="utf-8"><title>快来加入抖音短视频，让你发现最有趣的我！</title><meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0,minimum-scale=1,maximum-scale=1,minimal-ui,viewport-fit=cover"><meta name="format-detection" content="telephone=no"><meta name="baidu-site-verification" content="szjdG38sKy"><meta name="keywords" content="抖音、抖音音乐、抖音短视频、抖音官网、amemv"><meta name="description" content="抖音短视频-记录美好生活的视频平台"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="default"><link rel="apple-touch-icon-precomposed" href="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/image/logo/logo_launcher_v2_40f12f4.png"><link rel="shortcut icon" href="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/image/logo/favicon_v2_7145ff0.ico" type="image/x-icon"><meta http-equiv="X-UA-Compatible" content="IE=Edge;chrome=1"><meta name="screen-orientation" content="portrait"><meta name="x5-orientation" content="portrait"><script type="text/javascript">!function(){function t(t){return this.config=t,this}t.prototype={reset:function(){var t=Math.min(document.documentElement.clientWidth,750)/750*100;document.documentElement.style.fontSize=t+"px";var e=parseFloat(window.getComputedStyle(document.documentElement).fontSize),n=t/e;/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)||document.documentElement.setAttribute("flatform","android"),1!=n&&(document.documentElement.style.fontSize=t*n+"px")}},window.Adapter=new t,window.Adapter.reset(),window.onload=function(){window.Adapter.reset()},window.onresize=function(){window.Adapter.reset()}}();</script>  <meta name="screen-orientation" content="portrait"><meta name="x5-orientation" content="portrait"><script>tac='i)69e3nhroas!i#bsqs"0,<8~z|\x7f@QGNCJF[\\^D\\KFYSk~^WSZhg,(lfi~ah`{md"inb|1d<,%Dscafgd"in,8[xtm}nLzNEGQMKAdGG^NTY\x1ckgd"inb<b|1d<g,&TboLr{m,(\x02)!jx-2n&vr$testxg,%@tug{mn ,%vrfkbm[!cb|'</script><script type="text/javascript">!function(){function t(t){return this.config=t,this}t.prototype={reset:function(){var t=Math.min(document.documentElement.clientWidth,750)/750*100;document.documentElement.style.fontSize=t+"px";var e=parseFloat(window.getComputedStyle(document.documentElement).fontSize),n=t/e;/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)||document.documentElement.setAttribute("flatform","android"),1!=n&&(document.documentElement.style.fontSize=t*n+"px")}},window.Adapter=new t,window.Adapter.reset(),window.onload=function(){window.Adapter.reset()},window.onresize=function(){window.Adapter.reset()}}();</script><meta name="pathname" content="aweme_mobile_user">  <meta name="screen-orientation" content="portrait"><meta name="x5-orientation" content="portrait"><meta name="theme-color" content="#161823"><meta name="pathname" content="aweme_mobile_video"><link rel="dns-prefetch" href="//s3.bytecdn.cn/"><link rel="dns-prefetch" href="//s3a.bytecdn.cn/"><link rel="dns-prefetch" href="//s3b.bytecdn.cn/"><link rel="dns-prefetch" href="//s0.pstatp.com/"><link rel="dns-prefetch" href="//s1.pstatp.com/"><link rel="dns-prefetch" href="//s2.pstatp.com/"><link rel="dns-prefetch" href="//v1-dy.ixigua.com/"><link rel="dns-prefetch" href="//v1-dy.ixiguavideo.com/"><link rel="dns-prefetch" href="//v3-dy.ixigua.com/"><link rel="dns-prefetch" href="//v3-dy.ixiguavideo.com/"><link rel="dns-prefetch" href="//v6-dy.ixigua.com/"><link rel="dns-prefetch" href="//v6-dy.ixiguavideo.com/"><link rel="dns-prefetch" href="//v9-dy.ixigua.com/"><link rel="dns-prefetch" href="//v9-dy.ixiguavideo.com/"><link rel="dns-prefetch" href="//v11-dy.ixigua.com/"><link rel="dns-prefetch" href="//v11-dy.ixiguavideo.com/"><link rel="stylesheet" href="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/style/base_99078a4.css"><style>@font-face{font-family:iconfont;src:url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/font/iconfont_9eadf2f.eot);src:url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/font/iconfont_9eadf2f.eot#iefix) format('embedded-opentype'),url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/font/iconfont_9eb9a50.woff) format('woff'),url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/font/iconfont_da2e2ef.ttf) format('truetype'),url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/font/iconfont_31180f7.svg#iconfont) format('svg')}.iconfont{font-family:iconfont!important;font-size:.24rem;font-style:normal;letter-spacing:-.045rem;margin-left:-.085rem}@font-face{font-family:icons;src:url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/icons/iconfont_2f1b1cd.eot);src:url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/icons/iconfont_2f1b1cd.eot#iefix) format('embedded-opentype'),url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/icons/iconfont_87ad39c.woff) format('woff'),url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/icons/iconfont_5848858.ttf) format('truetype'),url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/icons/iconfont_20c7f77.svg#iconfont) format('svg')}.icons{font-family:icons!important;font-size:.24rem;font-style:normal;-webkit-font-smoothing:antialiased;-webkit-text-stroke-width:.2px;-moz-osx-font-smoothing:grayscale}@font-face{font-family:Ies;src:url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/icons/Ies_1275df9.woff2?ba9fc668cd9544e80b6f5998cdce1672) format("woff2"),url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/icons/Ies_749cd27.woff?ba9fc668cd9544e80b6f5998cdce1672) format("woff"),url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/icons/Ies_1bdf889.ttf?ba9fc668cd9544e80b6f5998cdce1672) format("truetype"),url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/icons/Ies_e0dc663.svg?ba9fc668cd9544e80b6f5998cdce1672#Ies) format("svg"),url(//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/icons/Ies_38cffe8.eot?af1f602fa7fb95e7bba3cc051e0c9236#Ies) format("embedded-opentype")}i{line-height:1}i[class^=ies-]:before,i[class*=" ies-"]:before{font-family:Ies!important;font-style:normal;font-weight:400!important;font-variant:normal;text-transform:none;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.ies-camera_add_music:before{content:"\f101"}.ies-camera_beauty_off:before{content:"\f102"}.ies-camera_beauty_on:before{content:"\f103"}.ies-camera_change_music:before{content:"\f104"}.ies-camera_clip:before{content:"\f105"}.ies-camera_cover:before{content:"\f106"}.ies-camera_details_determine:before{content:"\f107"}.ies-camera_details_determine1:before{content:"\f108"}.ies-camera_details_determine2:before{content:"\f109"}.ies-camera_expression:before{content:"\f10a"}.ies-camera_fangdou_close:before{content:"\f10b"}.ies-camera_fangdou_open:before{content:"\f10c"}.ies-camera_flip:before{content:"\f10d"}.ies-camera_flip2:before{content:"\f10e"}.ies-camera_lighting_auto:before{content:"\f10f"}.ies-camera_lighting_close:before{content:"\f110"}.ies-camera_lighting_open:before{content:"\f111"}.ies-camera_more:before{content:"\f112"}.ies-camera_night_off:before{content:"\f113"}.ies-camera_night_on:before{content:"\f114"}.ies-camera_picmovie:before{content:"\f115"}.ies-camera_picmovie2:before{content:"\f116"}.ies-camera_rotate_cutting:before{content:"\f117"}.ies-camera_rotate_cutting1:before{content:"\f118"}.ies-camera_rotate_cutting2:before{content:"\f119"}.ies-camera_selected:before{content:"\f11a"}.ies-camera_shooting:before{content:"\f11b"}.ies-camera_sound:before{content:"\f11c"}.ies-camera_speedoff:before{content:"\f11d"}.ies-camera_speedon:before{content:"\f11e"}.ies-camera_time_15:before{content:"\f11f"}.ies-camera_time_60:before{content:"\f120"}.ies-camera_unselected:before{content:"\f121"}.ies-camera_video_delete:before{content:"\f122"}.ies-checked:before{content:"\f123"}.ies-chevron-left:before{content:"\f124"}.ies-chevron-right:before{content:"\f125"}.ies-clear:before{content:"\f126"}.ies-close:before{content:"\f127"}.ies-copy:before{content:"\f128"}.ies-delete:before{content:"\f129"}.ies-edit:before{content:"\f12a"}.ies-help-circle:before{content:"\f12b"}.ies-info:before{content:"\f12c"}.ies-loading:before{content:"\f12d"}.ies-location:before{content:"\f12e"}.ies-paste:before{content:"\f12f"}.ies-query:before{content:"\f130"}.ies-remove:before{content:"\f131"}.ies-search:before{content:"\f132"}.ies-settings:before{content:"\f133"}.ies-shopping-bag:before{content:"\f134"}.ies-shopping-car:before{content:"\f135"}.ies-sort-left:before{content:"\f136"}.ies-sort-right:before{content:"\f137"}.ies-start-o:before{content:"\f138"}.ies-start:before{content:"\f139"}.ies-sticker_collection:before{content:"\f13a"}.ies-sticker_collection_m:before{content:"\f13b"}.ies-title-decorate-left:before{content:"\f13c"}.ies-title-decorate-right:before{content:"\f13d"}.ies-triangle-right:before{content:"\f13e"}.ies-triangle-top:before{content:"\f13f"}.ies-video:before{content:"\f140"}.ies-video_icon:before{content:"\f141"}.ies-zplus:before{content:"\f142"}</style>   <link rel="stylesheet" href="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/component/loading/index_8201db7.css" />
<link rel="stylesheet" href="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/component/banner/index_6ee9000.css" />
<link rel="stylesheet" href="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/pkg/common_84d74c0.css" />
<link rel="stylesheet" href="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/page/reflow_user/index_9f2bf42.css" />
<link rel="stylesheet" href="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/pkg/video_51ce97c.css" /></head>  <body><img id="weixinShareLogo" src="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/image/logo/logo_launcher_v2_40f12f4.png" style="position:absolute;top:-1000px;left:-1000px;">  <input type="hidden" name="shareTitle" value="快来加入抖音，让你发现最有趣的我！"> <input type="hidden" name="shareDesc" value="抖音——新奇好玩的15秒短视频社区！"> <input type="hidden" name="shareTimelineTitle" value="快来加入抖音，让你发现最有趣的我！"> <input type="hidden" name="shareAppTitle" value="快来加入抖音，让你发现最有趣的我！"> <input type="hidden" name="ShareAppDesc" value="抖音——新奇好玩的15秒短视频社区！"> <input type="hidden" name="shareImage" value="https://p3-dy.byteimg.com/aweme/720x720/3ee4002394be9e82bff2.jpeg">   <div class="page-reflow-user"><div class="pagelet-user-info" id="pagelet-user-info"><div class="bg"  style="background-image: url(https://p3-dy.byteimg.com/aweme/720x720/3ee4002394be9e82bff2.jpeg)" ></div><div class="personal-card"><div class="info1">  <span class="author"><img class="avatar" src="https://p3-dy.byteimg.com/aweme/720x720/3ee4002394be9e82bff2.jpeg"> </span><span class="focus-btn go-author" data-id="58747607165"><span>关注</span></span><p class="nickname">红星舵主</p><p class="shortid">抖音ID：     <i class="icon iconfont ">9</i><i class="icon iconfont ">8</i><i class="icon iconfont ">8</i><i class="icon iconfont ">7</i><i class="icon iconfont ">8</i><i class="icon iconfont ">4</i><i class="icon iconfont ">5</i><i class="icon iconfont ">9</i>   </p></div><div class="info2">  <p class="signature">做人晶莹剔透，做事滴水穿石。</p><p class="follow-info"><span class="focus block"><span class="num">    <i class="icon iconfont follow-num">1</i><i class="icon iconfont follow-num">3</i><i class="icon iconfont follow-num">0</i> </span><span class="text">关注</span> </span><span class="follower block"><span class="num">    <i class="icon iconfont follow-num">9</i><i class="icon iconfont follow-num">2</i> </span><span class="text">粉丝</span> </span><span class="liked-num block"><span class="num">    <i class="icon iconfont follow-num">6</i><i class="icon iconfont follow-num">5</i> </span><span class="text">赞</span></span></p></div></div><div class="video-tab">  <div class="tab-wrap"><div class="user-tab active tab get-list" data-type="post">作品<span class="num">    <i class="icon iconfont tab-num">7</i> </span></div>  <div class="like-tab tab get-list" data-type="like">喜欢<span class="num">    <i class="icon iconfont tab-num">9</i><i class="icon iconfont tab-num">4</i> </span></div></div></div></div><div id="pagelet-worklist" class="pagelet-worklist"><ul class="list js-list"></ul></div><div id="scaleImageWrapper" class="hidden"><div class="enlarge-wrapper"></div><button class="close"></button></div> <div class="pagelet-loading" id="pagelet-loading"><i class="icon"></i> <span class="txt">加载中...</span></div> <div id="pagelet-banner" class="pagelet-banner"><div class="icon hide"><img class="logo" src="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/image/logo/logo_launcher_v2_40f12f4.png"></div><div class="desc hide"><div class="title"><span>抖音短视频</span></div><div class="text">专注新生代的音乐短视频社区</div></div>  <div class="app-download" id="download"><div class="download-btn"><span class="txt">打开看看</span></div></div>  </div> </div>  <script src="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/script/lib/base_327cc85.js" crossorigin="anonymous"></script>   <script>;(function(window) {
        window.Raven && Raven.config('//key@m.toutiao.com/log/sentry/v2/174', {
          whitelistUrls: [/bytecdn\.cn/],
          shouldSendCallback: function(data) {
            return true;
          }
        }).install();
      })(window);</script>         <script src="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/component/loading/index_9d34b6b.js"></script>
<script src="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/pkg/third_89a176f.js"></script>
<script src="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/pkg/common_2d8e9f2.js"></script>
<script src="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/component/banner/index_0abc16e.js"></script>
<script src="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/pkg/video_1ebe932.js"></script>
<script src="//s3.pstatp.com/ies/resource/falcon/douyin_falcon/page/reflow_user/index_98797cc.js"></script>
<script type="text/javascript">
(function() {
            var GA = __M.require('douyin_falcon:common/ga/ga');
            GA.init(1, 'UA-75850242-4');
        
})();
(function() {
    var weixinUtil = __M.require('douyin_falcon:common/weixinUtil');
    $(function () {
        FastClick.attach(document.body);
        // 激活 ios active 样式
        document.body.addEventListener('touchstart',function(){},false);
        if ($.browser.weixin) {
            weixinUtil.init();
        }
    });
     
})();
(function() {
    $(function(){
        __M.require('douyin_falcon:page/reflow_user/index').init({
            uid: "58747607165",
            dytk: 'a5c195dd350b5480ca4646e0ce166456'
        });
    });
})();
</script>
</body></html>'''
# douyin_id =etree.HTML(response).xpath("/html/body/div[@class='page-reflow-user']/div[@id='pagelet-user-info']/div[@class='personal-card']/div[@class='info1']/p[@class='shortid']/i[@class='icon iconfont ']/text()")
# focus = ''.join(etree.HTML(response).xpath(
#     "/html/body/div[@class='page-reflow-user']/div[@id='pagelet-user-info']/div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']/span[@class='focus block']/span[@class='num']/i[@class='icon iconfont follow-num']/text()"))
# print(response)
# print(douyin_id,focus)

from selenium import webdriver
# driver=webdriver.Firefox()
# #谷歌驱动要放在C:\ProgramData\Anaconda3\Scripts目录下，
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com/')
get_video_url='https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id=58558645805&sec_uid=&count=21&max_cursor=0&aid=1128&_signature=RWqGVRAQGCSAD97YlheqnUVqhk&dytk=5f753a5de510917371e8e0d313f0747b'
'''https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id=58558645805
sec_uid=
count=21
max_cursor=0
aid=1128
_signature=RWqGVRAQGCSAD97YlheqnUVqhk
dytk=5f753a5de510917371e8e0d313f0747b'''
# search,想知道某个参数怎么加密来的，不知道哪个文件，先search，然后有该参数的文件都会出来了，接着继续寻找，这也是一种思想
'_signature'
'signature'
'_bytedAcrawler.sign(nonce)'#nonce就是uid,也就是share_id
#sign是_bytedAcrawler的一种方法，继续寻找_bytedAcrawler
'_bytedAcrawler = require("douyin_falcon:node_modules/byted-acrawler/dist/runtime")'
#该文件没有require，search寻找require，base_327***找到一个require方法（一个一个试试看），
't.__M.require = e'#找e方法，整个函数就是复制下来，是解密的一部分
#试一下能不能成功，不能。接着找这个douyin_falcon:node_modules/byted-acrawler/dist/runtime参数，search
'''__M.define("douyin_falcon:node_modules/byted-acrawler/dist/runtime", function(l, e) {
    Function(function(l)***'''
#解密函数一部分，试一下有参数出来，但是不是最终的参数
#查阅资料还缺少一个tac变量，在源代码有，和dytk一样可以获取

