"""词云图片制作"""
import re
from pathlib import Path

import matplotlib.pyplot as plt
import wordcloud
import jieba


# 创建词云对象
# word = wordcloud.WordCloud(
#     width=500, height=500, prefer_horizontal=0.2,
#     min_font_size=2, scale=2, max_words=200,
#     stopwords=['One', 'night'], mode='RGBA', background_color=None
# )
#
# # 传入需要制作词云的文本
# # TODO: 将用户的关键词整理
# word.generate('this is my house, i am leborn james One day,we donlt have to say goodoye,just say good night.')
#
# # 将生成的词云保存为图片，保存路径在当前目录的文件夹下
# image = word.to_image()
# image.save('ss.png')
#
# # 图像颜色生成器
# # image_generator = wordcloud.ImageColorGenerator()
#
# # 随机颜色，色相生成器
# wordcloud.random_color_func()
#
# # 创建一个颜色函数，该函数返回单个色调和饱和度
# color_func1 = wordcloud.get_single_color_func('deepskyblue')
import logging

my_logger = logging.getLogger('my_log')


class WorldCloud(object):
    """词云制作类"""

    BACKGROUND_PATH = '/Users/wangdong/Desktop/Learn/practice/cms/utils/f3870d3bfe00707cc46c600b5e581c10.jpg'

    def __init__(self):
        self.word_cloud = wordcloud.WordCloud(
            width=500, height=500, prefer_horizontal=0.2,
            min_font_size=2, scale=2, max_words=1000, mode='RGBA',
            background_color='white', font_path='/System/Library/Fonts/PingFang.ttc'
        )

    def get_content(self):
        """获取生成词云的文本"""
        my_logger.info('正在读取文本')
        dir = Path(__file__).resolve(strict=True).parent.parent / 'word_cloud.txt'
        with open(dir, 'r') as f:
            content = f.read()
        my_logger.info('文本内容读取成功')
        return content

    def strip_whitespace(self, content):
        """去空格"""
        my_logger.info('正在对文本进行处理')
        re_obj = re.compile('\s')
        my_logger.info('处理完成')
        return re.sub(re_obj, '', content)

    def participle(self, content):
        """对文本进行分词"""
        # 启用paddle模式
        my_logger.info('正在对文本进行中文分词')
        # 去空格
        clean_content = self.strip_whitespace(content)

        # 分词处理,使用精确模式
        generator = jieba.cut(clean_content, cut_all=False)
        result = "/ ".join(generator)
        my_logger.info('分词完成, 分词结果为:%s' % (result))
        return result

    def load_background_image(self):
        """加载背景图片"""
        my_logger.info('开始加载背景图片')
        backgroud_image = plt.imread(self.BACKGROUND_PATH)
        my_logger.info("加载背景图片成功")
        self.word_cloud.mask = backgroud_image

    def make_word_cloud(self, content=None):
        """制作词云图片"""
        my_logger.info('开始制作词云图片')
        self.load_background_image()
        if not content:
            content = self.get_content()
        content = self.participle(content)
        self.word_cloud.generate(content)

        # 将生成的词云保存为图片，保存路径在当前目录的文件夹下
        image = self.word_cloud.to_image()
        image.save('word_cloud.png')
        my_logger.info('制作成功')


if __name__ == '__main__':

    wcloud = WorldCloud()
    wcloud.participle()
    wcloud.make_word_cloud()