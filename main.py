import datetime


def update_readme():
    f = open('README.md', encoding='UTF-8', mode='w')

    # 获取当前时间
    now = datetime.datetime.now()

    # 转换为年月日格式
    year = now.year
    month = now.month
    day = now.day

    # 格式化输出
    formatted_date = f"{year}-{month}-{day}"

    readmeText = """
# Hello , 今天是 {date} 日 
    
![img]({image})
    
""".format(date=formatted_date,
           image="https://github-readme-stats.vercel.app/api?username=xiaxiayige")

    f.write(readmeText)
    f.flush()
    f.close()


update_readme()
