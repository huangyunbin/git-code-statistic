# git-code-statistic
根据git代码提交记录，得到统计数据，网页动态展示，可以方便生成视频


# 使用方式
#### 步骤1
   复制git.py到你的git项目目录 ，执行git.py，会生成一个result.csv文件
  
#### 步骤2
   打开html目录下的show.html,点击网页中的选择文件，选择刚才生成的result.csv，就可以看到一个动画了
   ![image.png](https://upload-images.jianshu.io/upload_images/7835103-c99d099963211070.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 使用效果 
   ![image.png](https://upload-images.jianshu.io/upload_images/7835103-ad35303c324ed34f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

   
  
# 自定义
 默认是一天的停留时间是0.3s，如果觉得太快或太慢，可以修改html目录下的config.js,修改interval_time这个参数
