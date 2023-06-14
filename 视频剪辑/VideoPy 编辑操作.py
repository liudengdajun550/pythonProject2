
'''
————————————————
版权声明：本文为CSDN博主「ZewanHuang」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_45497461/article/details/125850345
VideoPy 编辑操作
MoviePy 处理对象的基本单元为 clips，包含 AudioClips 和 VideoClips，在代码中可以看到，基本每一编辑操作都是作用在一个或多个 clips 上的。
混合片段 Mixing clips
视频合成，也称为非线性编辑，是在一个新剪辑中以一定的效果播放多个片段的现象。下面通过几个简单的样例介绍 MoviePy 的合并功能。
'''
'''
连接视频 Concatenate clips
将视频片段放在一起，最简单的方法是连接它们，在新剪辑中一个接一个地播放。视频连接通过函数 concatenate_videoclips 实现：
from moviepy.editor import VideoFileClip, concatenate_videoclips
clip1 = VideoFileClip("myvideo.mp4")
clip2 = VideoFileClip("myvideo2.mp4").subclip(50,60)
clip3 = VideoFileClip("myvideo3.mp4")
final_clip = concatenate_videoclips([clip1,clip2,clip3])
final_clip.write_videofile("my_concatenation.mp4")
'''

'''
堆叠视频 Stack clips
除了一个接一个播放的合并方式，MoviePy 还能将多个片段在同一画面中同时播放，形成片段堆叠效果，使用 clip_array 实现：
from moviepy.editor import VideoFileClip, clips_array, vfx
clip1 = VideoFileClip("myvideo.mp4").margin(10) # add 10px contour
clip2 = clip1.fx( vfx.mirror_x)
clip3 = clip1.fx( vfx.mirror_y)
clip4 = clip1.resize(0.60) # downsize 60%
final_clip = clips_array([[clip1, clip2],
                          [clip3, clip4]])
final_clip.resize(width=480).write_videofile("my_stack.mp4")

'''

'''
ompositeVideoClip 提供了非常方便的覆盖视频的方法，但是比前面所讲述的方法略显复杂。

video = CompositeVideoClip([clip1,clip2,clip3])
上述代码实现的覆盖关系为，片段 clip2 覆盖在 clip1 上层，clip3 覆盖在 clip2 上层。也就是说，当这三个片段具有相同的尺寸时，我们只看得到位于最上层的片段 clip3，除非 clip2 和 clip3 在尺寸或时长上只显示一部分。

需要注意的是，合成视频的尺寸大小以第一个参数 (clip1) 为准，因为它通常作为背景。而有些时候需要使合成视频尺寸更大，或者让背景更大，可以通过下面代码指定最终合成的尺寸大小：
video = CompositeVideoClip([clip1,clip2,clip3], size=(720,460))
在合成视频中，我们还可以通过 clip.set_start 来设置某片段的开始时刻，例如：
video = CompositeVideoClip([clip1, # starts at t=0
                            clip2.set_start(5), # start at t=5s
                            clip3.set_start(9)]) # start at t=9s
在上面的例子中，clip2 可能在 clip1 还没结束的时候就开始，此时可以通过 crossfadein 设置淡入效果的时间：
video = CompositeVideoClip([clip1, # starts at t=0
                            clip2.set_start(5).crossfadein(1),
                            clip3.set_start(9).crossfadein(1.5)])
如果 clip2 和 clip3 都比 clip1 小，可以通过设置其位置来决定它们出现在哪里。需要注意的是，坐标原点位于视频左上角。
video = CompositeVideoClip([clip1,
                           clip2.set_position((45,150)),
                           clip3.set_position((90,100))])

有更多的方法指定坐标：当指定视频坐标时，注意其遵循下图所示的坐标布局，左上角顶点为视频坐标开始原点。
clip2.set_position((45,150)) # x=45, y=150 , in pixels

clip2.set_position("center") # automatically centered

# clip2 is horizontally centered, and at the top of the picture
clip2.set_position(("center","top"))

# clip2 is vertically centered, at the left of the picture
clip2.set_position(("left","center"))

# clip2 is at 40% of the width, 70% of the height of the screen:
clip2.set_position((0.4,0.7), relative=True)

# clip2's position is horizontally centered, and moving down !
clip2.set_position(lambda t: ('center', 50+t) )

'''

'''
混合音频 Compositing audio clips
将视频混合剪辑在一起时，MoviePy 会自动组合它们各自的音轨，形成最终剪辑的音轨，因此无需考虑手动编辑视频的音轨。

如果想从多个音频源制作自定义音频，可以使用 CompositeAudioClip 和 concatenate_audioclips：
from moviepy.editor import *
# ... make some audio clips aclip1, aclip2, aclip3
concat = concatenate_audioclips([aclip1, aclip2, aclip3])
compo = CompositeAudioClip([aclip1.volumex(1.2),
                            aclip2.set_start(5), # start at t=5s
                            aclip3.set_start(9)])

'''

'''
音频操作 Audio in MoviePy
创建音频 Creating a new audio clip
音频对象可以从音频文件中初始化：
from moviepy.editor import *
audioclip = AudioFileClip("some_audiofile.mp3")
audioclip = AudioFileClip("some_video.avi")
也可以从视频的音轨中创建：
videoclip = VideoFileClip("some_video.avi")
audioclip = videoclip.audio
'''

'''
合并音频 Compositing audio clips
见本篇『混合音频 Compositing audio clips』部分。
'''

'''
设置为视频音轨
将音频剪辑片段指定为视频的配乐：
videoclip2 = videoclip.set_audio(my_audioclip)
'''