import cv2
#参考文件：https://blog.csdn.net/weixin_42588672/article/details/129613023?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-129613023-blog-125329001.235%5Ev38%5Epc_relevant_anti_vip&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-129613023-blog-125329001.235%5Ev38%5Epc_relevant_anti_vip&utm_relevant_index=3
# 读取视频文件
cap = cv2.VideoCapture('/Users/shuangmindeng/PycharmProjects/pythonProject2/vedio/屏幕录制2023-06-13 17.09.27.mov')

while cap.isOpened():
    # 逐帧读取视频
    ret, frame = cap.read()
    if not ret:
        break

    # 显示视频帧
    cv2.imshow('Video Player', frame)

    # 等待用户按下q键退出
    if cv2.waitKey(25) & 0xFF == ord('q'):  # 按‘q’退出
        break

