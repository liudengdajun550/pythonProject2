xpath的基本用法
//元素标签名    例如：//div 功能是查找网页内的所有div
//元素标签名[@属性名=’具体内容‘]   例如：//div[@class='box'] 功能是查找存在属性@class='box'的div
//元素标签名[第几个]     例如：//div[@class="box"][2] 查找符合条件的第二个div
//元素1/元素2/元素3...   例如：//ul/li/div/a/img  查找ul下的li下的div下的a下的img标签
//元素1/@属性名          例如：//ul/li/div/a/img/@src  查找ul下的li下的div下的a下的img标签的src属性
//元素/text()   例如：//a/text() 获取a标签下的文本(一级文本)
//元素//text()  例如：//div[@class='box']//text() 获取class=‘box’的div下的所有文本
//元素[contains(@属性名，'相关属性值')]   例如：//li[contains(@class,'zhangsan')]  查找class中包含zhangsan的div
//*[@属性='值']  例如：//*[@name='lisi'] 查找name为lisi的元素
————————————————
版权声明：本文为CSDN博主「伪装的TA」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_42543301/article/details/81252895

https://www.jianshu.com/p/dd7ad5c1a778
口播神器,基于Edge,微软TTS(text-to-speech)文字转语音免费开源库edge-tts实践(Python3.10)
该命令可以将Edge浏览器中，内置的语言角色列表列出来：
edge-tts --list-voices

该命令含义是通过zh-CN-XiaoyiNeural角色合成语音："你好啊，我是智能语音助手"的内容，随后将音频流写入hello_in_cn.mp3文件。
edge-tts --voice zh-CN-XiaoyiNeural --text "你好啊，我是智能语音助手" --write-media hello_in_cn.mp3

与此同时，我们也可以调整合成语音的语速：
edge-tts --rate=-50% --voice zh-CN-XiaoyiNeural --text "你好啊，我是智能语音助手" --write-media hello_in_cn.mp3
--rate参数可以通过加号或者减号同步加快或者减慢合成语音的语速。

亦或者，调整合成语音的音量：
edge-tts --volume=-50%  --voice zh-CN-XiaoyiNeural --text "你好啊，我是智能语音助手" --write-media hello_in_cn.mp3



https://blog.csdn.net/DynmicResource/article/details/125500199
Python将语音识别成文字
pyaudio
speechrecognition
https://blog.csdn.net/hutianle/article/details/123309961
https://blog.csdn.net/weixin_49891576/article/details/127407341

音频格式转换
https://blog.csdn.net/qq_41860526/article/details/122141676


安装：pip和brew区别
https://www.cnblogs.com/stu2018/p/9419324.html


