# _*_ coding:utf-8 _*_
import os,glob
def readpos_neg():
    files=glob.glob('data/*.txt')
    filepath=files[0]
    generatedate=filepath[5:15]
    fr=open(filepath,'r')
    dataMat=[]
    for line in fr.readlines():
        curLine=line.strip().split('\t')
        lineArr=[]
        lineArr.append(curLine[0])
        lineArr.append(float(curLine[1]))
        lineArr.append(curLine[2])
        dataMat.append(lineArr)
    poss=[x for x in dataMat if x[2]=='pos']
    negs=[x for x in dataMat if x[2]=='neg']
    return poss,negs,generatedate

