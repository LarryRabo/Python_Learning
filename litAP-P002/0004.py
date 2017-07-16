# 未解决

import string,random

class GenCode:
    def __init__(self):

    # 获得四个字符和数字的随机组合
    def getRandom1(self,string_code):
        return "".join(random.sample(string_code, 4))

    # 生成的每个激活码中有几组
    def concatenate1(str1, group):
        return "-".join([getRandom1(str1) for i in range(group)])

    # 生成n组激活码
    def generate1(str1, group, n):
        return [concatenate1(str1, group) for i in range(n)]

if __name__=="__main__":
    string_code = string.ascii_letters + string.digits
        #string_code="qwertyuiopasdfghjklzxcvbnm1234567890"
    code1=GenCode() #实例化类
    keys=code1.concatenate1(string_code,4,200)
    #keys=code1.generate1(string_code, 4, 200)
    # 将生成的激活码存入数据库中
    for i in range(len(keys)):
        r.sadd("code", keys[i])
    r.save()

    # print(type(string_code))
    # gencode=Genration() #实例化类
    # gencode.generate_uuid(200) #调用generate_uuid（）方法
    # keys=gencode.get_uuid() #调用get_uuid()方法