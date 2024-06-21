import datetime


def update_readme():
    f = open('README.md', encoding='UTF-8', mode='w')

    # 获取当前时间
    now = datetime.datetime.now()

    # 转换为年月日格式
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    # 格式化输出
    formatted_date = f"{year}-{month}-{day}"

    readmeText = """
# Hello , 今天是 {date} , 加油鸭 🤭
    
![img]({image})

![img](https://v1.jinrishici.com/all.svg?font-size=18&spacing=4)

""".format(date=formatted_date,
           image="https://content.codecademy.com/courses/learn-cpp/community-challenge/highfive.gif")

    f.write(readmeText)
    f.flush()
    f.close()


update_readme()
