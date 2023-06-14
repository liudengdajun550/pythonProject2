# 原文链接：https://blog.csdn.net/weixin_45497461/article/details/125850345
# 引入用于编辑视频的所有包
from moviepy.editor import *

# 加载视频并选择 00:00:50 - 00:00:60 的片段
clip = VideoFileClip("/Users/shuangmindeng/PycharmProjects/pythonProject2/vedio/vedio.mp4").subclip(1,30)

# 降低音量 (volume x 0.8)
clip = clip.volumex(0.8)

# 生成字幕片段，可自定义字体和颜色等
txt_clip = TextClip(txt="My Holidays 2013", fontsize=10, color='red')

# 设置在屏幕中央显示 10 秒
txt_clip = txt_clip.set_pos('center').set_duration(10)

# 在载入的原视频上层覆盖文本视频
video = CompositeVideoClip([clip, txt_clip])

# 将输出结果写入文件中
video.write_videofile("/Users/shuangmindeng/PycharmProjects/pythonProject2/vedio/vedio.mp4")

