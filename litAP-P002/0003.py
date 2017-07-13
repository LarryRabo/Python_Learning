# 第 0002题： 做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？生成序列号并存放到数据库中
# coding：utf-8
import string,random
import pymysql.cursors

# 获得四个字符和数字的随机组合
def getRandom1(string_code):
        return "".join(random.sample(string_code, 4))

# 生成的每个激活码中有几组
def concatenate1(str1,group):
    return "-".join([getRandom1(str1) for i in range(group)])

# 生成n组激活码
def generate1(str1,group,n):
    return [concatenate1(str1,group) for i in range(n)]

if __name__=="__main__":
    string_code = string.ascii_letters + string.digits
    string_code=str(string_code)
    keys=generate1(string_code,4,200)
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='litappdatabase',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor()

    cursor.execute("INSERT INTO code (id, idcode) values(%s,%s)", (1003, keys[1]))

    for i in range(len(keys)):
        sql = "INSERT INTO code (id, idcode) VALUES ( '%s', '%s')"
        data = (i,keys[i])
        cursor.execute(sql % data)
        connect.commit()  #执行sql语句
     # 关闭连接
    cursor.close()
    connect.close()


