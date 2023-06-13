from lxml import etree

html_str = """
<a href='https://www.baidu.com'>
        百度一下，你就知道
</a>
"""
# 将字符串转化成标签
# 该方法会检测字符串内容是否为标签样式，但是不能检测出内容是否为真的标签
result = etree.fromstring(html_str)
print(result)

# parse 解析
html = etree.HTML('index.html')
print(type(html))
print(html)

# 找到网页内所有的a标签
a = html.xpath('//a')
print(a)
# 根据标签属性找到指定的标签
# 获取指定标签的内容
result = html.xpath('//a/@class')
print(result)
result = html.xpath('//a/@id')
print(result)
# 找到所有标签的超链接属性
result = html.xpath('//a/@href')
print(result)
# 找到指定的文本内容------------------

result = html.xpath('//a/text()')
print(result)
# 如果找某一个标签的文本，而这个标签下面还有其他的标签 那么只找这个标签的文本 子标签的文本不找
result = html.xpath('//div/text()')
print(result)
# //text()找到本标签以及所有子标签的文本
result = html.xpath('//div//text()')
print(result)
for name in result:
    print(name)
# 获取指定id名字的标签的文本
result = html.xpath('//ul//lia[@id="jd"]/text()')
print(result[0])
# last()获取最后一个标签
result = html.xpath('//ul/li[last()]')[0]
print(result)
# 获取拥有指定类名的标签的文本
result = html.xpath('//a[@class="shopping"]/text()')
print(result)

# contains 包含指定属性
result = html.xpath('//div[@class="now"]/p[contains(@class,"third")]/text()')
print(result)
# 找到所有的ul
# 找到所有ul中的所有a标签
# 获取a标签文本和所有a标签的子标签的文本
result = html.xpath('//ul//a//text()')
print(result)