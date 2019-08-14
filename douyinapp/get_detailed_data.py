#-*-coding:utf-8-*-
import requests
from lxml import etree
import decode_douyin
import save_database

def detailed_data(share_id):
    share_url = 'https://www.iesdouyin.com/share/user/{}'.format(share_id)
    headers = {"Connection": "keep-alive",
               "Cache-Control": "max-age=0",
               "Upgrade-Insecure-Requests": "1",
               "User-Agent": "com.ss.android.ugc.aweme/730 (Linux; U; Android 5.1.1; zh_CN; HUAWEI MLA-AL10; Build/HUAWEIMLA-AL10; Cronet/58.0.2991.0)",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
               "Accept-Encoding": "gzip,deflate,br",
               "Accept-Language": "zh-CN,zh;q=0.9", }
    response = requests.get(share_url, headers=headers).text
    response=decode_douyin.decode_response(response)
    data={}
    name=''.join(etree.HTML(response).xpath("/html/body/div[@class='page-reflow-user']/div[@id='pagelet-user-info']/div[@class='personal-card']/div[@class='info1']/p[@class='nickname']/text()")).strip('')
    #这里有个坑，如果目录寻到/i[@class='icon iconfont ']，注意最后面还有一个空格，直接复制谷歌的是没有的。
    #如果想上面那样取会取不到id是字符的，所以应该在上一个路径取全部下来（//），就可以解决了
    douyin_id=''.join(etree.HTML(response).xpath("/html/body/div[@class='page-reflow-user']/div[@id='pagelet-user-info']/div[@class='personal-card']/div[@class='info1']/p[@class='shortid']//text()")).strip('抖音ID：').strip(' ')
    print(etree.HTML(response).xpath("/html/body/div[@class='page-reflow-user']/div[@id='pagelet-user-info']/div[@class='personal-card']/div[@class='info1']/p[@class='shortid']"))
    introcdution=etree.HTML(response).xpath("/html/body/div[@class='page-reflow-user']/div[@id='pagelet-user-info']/div[@class='personal-card']/div[@class='info2']/p[@class='signature']/text()")
    focus=''.join(etree.HTML(response).xpath("/html/body/div[@class='page-reflow-user']/div[@id='pagelet-user-info']/div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']/span[@class='focus block']/span[@class='num']/i[@class='icon iconfont follow-num']/text()"))
    fans=''.join(etree.HTML(response).xpath("/html/body/div[@class='page-reflow-user']/div[@id='pagelet-user-info']/div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']/span[@class='follower block']/span[@class='num']/i[@class='icon iconfont follow-num']/text()"))
    #判断有无上万，获取元素不会报错，没有则返回空
    fans1=etree.HTML(response).xpath("/html/body/div[@class='page-reflow-user']/div[@id='pagelet-user-info']/div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']/span[@class='follower block']/span[@class='num']/text()")
    if fans1:
        if 'w' in fans1[-1].strip(' '):
            fans=str(int(fans)/10)+'万'
    like=''.join(etree.HTML(response).xpath("/html/body/div[@class='page-reflow-user']/div[@id='pagelet-user-info']/div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']/span[@class='liked-num block']/span[@class='num']/i[@class='icon iconfont follow-num']/text()"))
    like1=etree.HTML(response).xpath("/html/body/div[@class='page-reflow-user']/div[@id='pagelet-user-info']/div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']/span[@class='liked-num block']/span[@class='num']/text()")
    if like1:
        if 'w' in like1[-1].strip(' '):
            like=str(int(like)/10)+'万'
    data['name']=name
    data['douyin_id']=douyin_id
    data['introcdution']=introcdution
    data['focus']=focus
    data['fans']=fans
    data['like']=like
    data['share_id']=share_id
    save_database.detaildata_save(data)
    print(data)
detailed_data(50327075327)