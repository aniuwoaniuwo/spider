from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

from matplotlib.image import imread

#生成词云
def create_word_cloud(filename):
    text= open("{}.txt".format(filename)).read()
    # 结巴分词
    
    # 设置词云
    wc = WordCloud(
        # 设置背景颜色
        background_color="white",
         # 设置最大显示的词云数
       max_words=20000,
         # 这种字体都在电脑字体中，一般路径
       font_path='C:\Windows\Fonts\simfang.ttf',

       height= 1080,
       width= 1920,

	   # 设置字体最大值
       max_font_size=600,
     # 设置有多少种随机生成状态，即有多少种配色方案
       random_state=30,
       relative_scaling=.3
         
    )

    myword = wc.generate(text)  # 生成词云
    
    wc.to_file('hello.png')  # 把词云保存下

if __name__ == '__main__':
    
    create_word_cloud('kongjian')
    