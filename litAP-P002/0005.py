# 第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
import os


def word_counts(inputfile):
    """
        # 统计单词数量
    """
    # 判断当前文件是否可以打开
    if os.path.isfile(inputfile) != True:
        print("inputfile not exists")
        #system.exit()
    word_count = 0
    words = open(inputfile, "r").readlines() #按行读取

    for word in words:
        temp = word.strip().split(' ') #以空格断开存放在list中
        word_count += len(temp)

    return word_count

if __name__=="__main__":
    num=word_counts("enwords.txt")
    print("此文档中总共：%s 个单词"% num)