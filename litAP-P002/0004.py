import GennerateCode,string

if __name__=="__main__":
    string_code = string.ascii_letters + string.digits
    string_code = str(string_code)


    keys=GennerateCode.generate1(string_code, 4, 200)


    # 将生成的激活码存入数据库中
    for i in range(len(keys)):
        r.sadd("code", keys[i])
    r.save()