# -*- coding:utf-8 -*-

import jieba
import jieba.analyse


def frequency_statistics(file):
    resultFile = "C:\\Users\\chenyang\\Desktop\\Result.txt"
    resultTxt = open(resultFile, "w", errors='ignore', encoding='utf-8')
    word_dict = {}
    for line in open(file, 'rU', errors='ignore', encoding='utf-8'):
        item = jieba.cut(line.strip("\n"))
        for word in item:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
    for key in word_dict:
        resultTxt.write(key+"\t"+ str(word_dict[key])+"\n")


if __name__ == '__main__':
    filepath = 'C:\\Users\\chenyang\\Desktop\\content_seg.txt'
    frequency_statistics(filepath)
