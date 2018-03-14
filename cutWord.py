# -*- coding:utf-8 -*-
import jieba
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

'''
Segmentation:cut the word
if you wanna use the customized  list of word segmentation ,plz set the segcust to be 1
if you set the stopwordlabel to be 1,this method will support to delete the word those in the stop-word list
切分：剪切单词
如果你想使用分词自定义的列表，请设置segcust是1
如果你设置stopwordlabel为1，此方法将支持删除单词在停词列表
'''
stopword_path = 'C:\\Users\\chenyang\\Desktop\\dict.txt'
def Segmentation(sentence,stopwordlabel,segcust):
    if segcust==0:
            jieba.load_userdict('D:\\ideal\\cx\\ipsos\\weibo\\dict.txt')
    stopword_file = open(stopword_path, "r").readlines()
    stopwords = [word.replace("\n", "") for word in stopword_file] #replace the /n in the word
    if stopwordlabel==0:
        wordlist = [word for word in jieba.cut(sentence) if word not in stopwords] #delete the stop-word and cut the word
    else:
        wordlist = [word for word in jieba.cut(sentence)]#only cut the word
    wordloc = {word: loc for loc, word in enumerate(wordlist)}
    return wordlist#, wordloc



'''
create the corpus for tfidf model
创建语料库TFIDF模型
'''
def tfidfCorpus(text):
    ticorpus=[]
    for review in text:
        #wordlist,wordloc=Segmentation(review.replace("\n",""),1,1)
        wordlist = Segmentation(review.replace("\n", ""), 1, 1)
        #for word in wordlist:
        ticorpus.append(" ".join(wordlist))
    return ticorpus

'''
let words change to matrix of wordvec
让单词变为单词向量矩阵
'''
def tfidf_transformer(corpus):
    vectorizer = CountVectorizer()#get the matrix of word-freq 获取单词频率矩阵
    transformer = TfidfTransformer()#count the tfidf value 统计tfidf值
    tfidf_mod = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf_mod.toarray()
    for i in range(len(weight)):
        print(u"-------第", i, u"类文本的词语tf-idf权重------")
        for j in range(len(word)):
            print(word[j], weight[i][j])


if __name__ == '__main__':
    test='C:\\Users\\chenyang\\Desktop\\shanghai-company.txt'
    text = open(test,'r',encoding='UTF-8')
    tfidf_transformer(tfidfCorpus(text))
