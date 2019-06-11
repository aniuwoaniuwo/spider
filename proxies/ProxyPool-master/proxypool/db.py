#ip池的存储部分
#测试是从分数高到低测试，每次重新运行都会重新开始测试
import redis
from proxypool.error import PoolEmptyError
from proxypool.setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY
from proxypool.setting import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from random import choice
import re


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
    
    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理，设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """
        if not re.match('\d+\.\d+\.\d+\.\d+\:\d+', proxy):
            print('代理不符合规范', proxy, '丢弃')
            return
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY,{proxy:score})#添加新元素，为10分
    
    def random(self):
        """
        随机获取有效代理，首先尝试获取最高分数代理，如果不存在，按照排名获取，否则异常
        :return: 随机代理
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)#通过分数返回有序集合指定区间内的成员
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)#0-100直接的随便一个
            else:
                raise PoolEmptyError

    def test(self):
        """
        随机获取有效代理+对应分数，首先尝试获取最高分数代理，如果不存在，按照排名获取，否则异常
        :return: 随机代理
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)#通过分数返回有序集合指定区间内的成员
        if len(result):
            ip = choice(result)
            # dict = {'ip': ip,
            #         'score': str(self.db.zscore(REDIS_KEY, ip))}
            score = str(self.db.zscore(REDIS_KEY, ip)) #获取指定元素的分数
            return 'ip:{}<br/>score:{}'.format(ip, score)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                ip = choice(result)
                # dict = {'ip': ip,
                #         'score': str(self.db.zscore(REDIS_KEY, ip))}
                score=str(self.db.zscore(REDIS_KEY, ip))
                return 'ip:{}<br/>score:{}'.format(ip,score)
            else:
                raise PoolEmptyError
    
    def decrease(self, proxy):
        """
        代理值减一分，小于最小值则删除
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            return self.db.zincrby(REDIS_KEY, -1, proxy)#某元素-1
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy) #移除
    
    def exists(self, proxy):
        """
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        """
        return not self.db.zscore(REDIS_KEY, proxy) == None
    
    def max(self, proxy):
        """
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        """
        print('代理', proxy, '可用，设置为', MAX_SCORE)
        # self.db.zadd(REDIS_KEY, {proxy: score})
        #redis更新了，所以原代码需要修改成下面这样的
        return self.db.zadd(REDIS_KEY,{proxy: MAX_SCORE} )#更新为100分
    
    def count(self):
        """
        获取数量
        :return: 数量
        """
        return self.db.zcard(REDIS_KEY) #获取数量
    
    def all(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
        # return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
        return self.db.zrange(REDIS_KEY,0,-1,withscores=True)#返回所有元素以及对应分数

    def batch(self, start, stop):
        """
        批量获取，配合测试获取ip
        :param start: 开始索引
        :param stop: 结束索引
        :return: 代理列表
        """
        return self.db.zrevrange(REDIS_KEY, start, stop - 1) #索引，第几个到第几个的区间,分数从高到底


if __name__ == '__main__':
    conn = RedisClient()
    result = conn.batch(680, 688)
    print(result)
