import numpy as np

'''
创建数据集
return: 单词列表，所属类别
'''
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'], #[0,0,1,1,1......]
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec

'''
构建数据矩阵，获取所有单词的集合
'''

def createVocList(dataset):
    vocSet=set()                #转换为集合
    for doc in dataset:
        vocSet=vocSet | set(doc)
    return list(vocSet)

'''
遍历查看单词是否出现，出现则在向量中置1
vocList: 单词列表
inputSet: 输入的数据集
return: 列表[0,1,0,1,1,.....],1代表词汇表中的单词出现在输入数据集中，
'''

def setOfWord2Vector(vocList,inputSet):
    voc = [0]*len(vocList)
    for w in inputSet:
        if w in vocList:
            voc[vocList.index(w)] = 1
        else:
            print('%s not in'%w)
    return voc

def trainNB0(trainMatrix, trainCateory):     #trainMatrix:为构建好的词向量
    m = len(trainMatrix)
    numWords = len(trainMatrix[0])
    p_abusive = sum(trainCateory)/float(m)      #有多少列言论
    p0Num = np.ones(numWords)
    p1Num = np.ones(numWords)
    p0Denom = 2
    p1Denom = 2
    for i in range(m):                            #遍历是否为污辱性言论
        if trainCateory[i] == 1:
            p1Num += trainMatrix[i]               #对应位置单词相加
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]                #对应位置单词相加
            p0Denom += sum(trainMatrix[i])
    p1Vect = np.log(p1Num/p1Denom)
    p0Vect = np.log(p0Num/p0Denom)
    return p0Vect, p1Vect, p_abusive
'''
lst, cates = loadDataSet()
voc_list = createVocList(lst)
trainMatrix = []
for words in lst:
    trainMatrix.append(setOfWord2Vector(voc_list, words))
p0Vec, p1Vec, p_abusive = trainNB0(trainMatrix, cates)
'''
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass):
    p1 = sum(vec2Classify*p1Vec) + np.log(pClass)
    p0 = sum(vec2Classify*p0Vec) + np.log(1.0-pClass)
    if p1 > p0:
        return 1
    else:
        return 0

def testingNB():
    '''
    测试朴素贝叶斯算法
    '''
    list0Posts, listClasses = loadDataSet()
    myVocabList = createVocList(list0Posts)
    trainMat = []
    for postinDoc in list0Posts:
        trainMat.append(setOfWord2Vector(myVocabList,postinDoc))
    p0V, p1V, pAb=trainNB0(np.array(trainMat), np.array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = np.array(setOfWord2Vector(myVocabList, testEntry))
    print(testEntry, 'classified as:',classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = np.array(setOfWord2Vector(myVocabList, testEntry))
    #testEntry = ['tostupid', 'bisgarbage']
    #thisDoc = np.array(setOfWord2Vector(myVocabList, testEntry))
    print(testEntry, 'classified as:', classifyNB(thisDoc, p0V, p1V, pAb))

testingNB()

import re
def textParse(words):
    lst0fToken = re.split(r'\w',words)
    return [t.lower() for t in lst0fToken if len(t) > 2]       #过滤掉字母小于2的单词,并返回小写单词的列表

def spamTest():
    docList = []
    classList = []
    fullyText = []
    for i in range(1,26):
        wordList = textParse(
            open("E:/Desktop/email/email/spam/%d.txt" % i,
                 encoding='utf-8').read())
        docList.append(wordList)
        classList.append(1)

        wordList = textParse(
            open("E:/Desktop/email/email/ham/%d.txt" % i,
                 encoding='utf-8').read())
        docList.append(wordList)
        classList.append(0)
    voc_list = createVocList(docList)
    trainSet = [i for i in range(50)]
    testSet = []

    for i in range(10):                   #随机选10封邮件做为测试集，并删除
        randIndex = int(np.random.uniform(0, len(trainSet)))
        testSet.append(trainSet[randIndex])
        del (trainSet[randIndex])
    trainMat = []
    trainClass = []

    for index in trainSet:
        trainMat.append(setOfWord2Vector(voc_list, docList[index]))
        trainClass.append(classList[index])
    p0v, p1v, pSam = trainNB0(np.array(trainMat), np.array(trainClass))
    errors = 0

    for index in testSet:
        wordVector = setOfWord2Vector(voc_list, docList[index])
        if classifyNB(np.array(wordVector), p0v, p1v, pSam) != classList[index]:
            errors += 1
    print('errors:', errors)
    print('errors rate:', errors/len(testSet))

spamTest()