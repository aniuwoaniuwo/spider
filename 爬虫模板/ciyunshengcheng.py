from wordcloud import WordCloud
import matplotlib.pyplot as plt

def wordcloud(ss):
    text = open('%s.txt' % ss).read()
    wc = WordCloud(
        # 设置背景颜色
        background_color="white",
        # 设置最大显示的词云数2000
        max_words=2000,
        # 这种字体都在电脑字体中，一般路径1200 1600
        font_path='C:\Windows\Fonts\simfang.ttf',
        #字体间隔，清晰度
        height=1200,
        width=1600,
        # 设置字体最大值100
        max_font_size=100,
        # 设置有多少种随机生成状态，即有多少种配色方案30
        random_state=30,
    )
    mywc = wc.generate(text)
    plt.imshow(mywc)
    plt.axis("off")
    plt.show()
    wc.to_file('wcbook.png')

if __name__ == '__main__':
    wordcloud('ciyun')
