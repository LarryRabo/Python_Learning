#第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
#coding：utf-8
import string,random
import uuid

class Genration:
    #采用uuid库产生唯一的编码，但是与我们要求的xxxx-xxxx-xxxx-xxxx要求不想符合
    def __init__(self):
        self.num=0
        self.listid=[]

    def generate_uuid(self,num):
        for i in range(int(num)):
            self.listid.append(uuid.uuid1())

    def get_uuid(self):
        return self.listid



# 激活码中的字符和数字

# 字符串:string_code=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

# 获得四个字符和数字的随机组合

def getRandom1():
        return "".join(random.sample(string_code, 4))
# 生成的每个激活码中有几组
def concatenate1(str1,group):
    return "-".join([getRandom1(str1) for i in range(group)

# 生成n组激活码
def generate1(str1,group,n):
    #return [concatenate1(str1,group) for i in range(n)]




if __name__=="__main__":
    string_code = string.ascii_letters + string.digits
    print(type(string_code))
    #gencode=Genration() #实例化类
    #gencode.generate_uuid(200) #调用generate_uuid（）方法
    #keys=gencode.get_uuid() #调用get_uuid()方法
    #getcode=GeneratorRandom()


    #keys=generate1(string_code,4,200)





    filekeys=open("gencodes.txt",'w') #打开文件只写
    for k in keys:
        filekeys.write(str(k)+'\n')
    filekeys.close()

