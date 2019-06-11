#html网页接受的是字符串，list，数字都要转化为字符串才可以
#ip池的接口部分，flask框架写的，
from flask import Flask, g


from .db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        #调用存储部分的RedisClient类，
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    #主页
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    #返回的是RedisClient类中的random功能，就是获取随机的一个ip
    return str(conn.random())


@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    #记得加str，因为html页面前端html展示出来的是字符串
    return str(conn.count())

@app.route('/test')
def get_test():
    """
    Get the count of proxies
    :return: 随机的代理以及他的分数
    """
    conn = get_conn()
    return conn.test()

@app.route('/all')
def get_all():
    """
    Get the count of proxies
    :return: 总的ip，list的形式，也要先变成str
    """
    conn = get_conn()
    return str(conn.all())

if __name__ == '__main__':
    app.run()
