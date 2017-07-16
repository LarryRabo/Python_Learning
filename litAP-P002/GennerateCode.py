import random

class GenCode:
    def __init__(self,name):
        self.name = name

    def getRandom1(string_code):
        return "".join(random.sample(string_code, 4))


    # 生成的每个激活码中有几组
    def concatenate1(str1, group):
        return "-".join([getRandom1(str1) for i in range(group)])


    # 生成n组激活码
    def generate1(string_code, group, n):
        return [concatenate1(string_code, group) for i in range(n)]
