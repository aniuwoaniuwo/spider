#-*-coding:utf-8-*-
#这是正则表达式的测试模板，在网页中复制需要匹配的HTML，然后这里匹配是否正确
import re

HTML='''
<div class="layout grid-s730m0">
        <div class="col-main">
            <div class="main-wrap">
                <div class="property"  id="J_Property">
    <h1 class="title">华为荣耀4&#039;x顶级配置可玩大型游戏送16g储存卡送刀模 魔方</h1>
    <ul class="price-info">
        <li class="price-block">
            <span class="para">转&nbsp;&nbsp;卖&nbsp;&nbsp;价：</span>
            <span class="price big"><b>&yen;</b><em>900.00</em></span>
							    				<span class="bargain-tip">
                        <i class="i-tip"></i>该商品拒绝讲价！
                    </span>
    						        </li>
		    </ul>
    <ul class="idle-info" data-spm="2007.1000338.3">
		<li>
    		 <span class="para">成　　色：</span>
             <em>全新</em>
        </li>
        <li>
            <span class="para">所&nbsp;&nbsp;在&nbsp;&nbsp;地：</span>
            <em>黑龙江齐齐哈尔 建华区</em>
        </li>
					<li class="contact">
                <span class="para">联系方式：</span>
    			    							<div style="display:none">
                    <span class="J_WangWang" data-nick="t_1483577804985_0679" data-icon="large"></span>
                </div>
            </li>
            <li class="trade-terms" id="J_TradeWrap">
                <span class="para">交易方式：</span>
    			    				<a href="#"><span data-term="0" class="J_Term term">在线交易</em></em></span><i></i></a>
				    <li id="J_Freight" class="freight">
                        <a id="J_Region" class="region" href="#" data-default="">
        					至 <em id="J_RegionName"></em><i></i>
                        </a>
                        <span id="J_Carriage" class="fee" data-url="//adpmanager.taobao.com/detail/delivery_detail.do?itemId=592838761902">运费：<em class="rmb">&yen;</em><span id="J_Fee">加载中...</span></span>
                    </li>
    			            </li>
		    </ul>
	    	<div class="buy-now" data-spm="2007.1000338.4">
    <a id="J_BuyNow" data-url="//buy.2.taobao.com/buy/buy.htm?from=itemDetail&amp;x_id=&amp;id=592838761902&amp;item_id=592838761902" class="btn" href="#">立刻购买</a>'''

pattern = re.compile(
            '<div.*?main-wrap.*?title.*?>(.*?)</h1>.*?price big.*?<em>(.*?)</em>.*?para.*?<em>(.*?)</em>.*?para.*?<em>(.*?)</em>',
            re.S)
pattern1=re.compile('客户开始\*{15}(.*?)\*{14}客户结束',re.S)
items = re.findall(pattern,HTML)
print(items)
for item in items[0]:
    print(item)