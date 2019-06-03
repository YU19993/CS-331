import numpy as np
import sys
import csv
import re
import math

def inVocabulary(word, vocabulary):
        for i in range(len(vocabulary)):
                if word == vocabulary[i]:
                        return i
        return -1


train = []
test  = []
vocabulary = []
pro_train = []
pro_test  = []

file = open("trainingSet.txt", "r")
for i in file:
        temp = i
        temp = temp.split('\t')
        train.append(temp)
file.close()

file = open("testSet.txt", "r")
for i in file:
        temp = i
        temp = temp.split('\t')
        test.append(temp)
file.close()

for i in range(len(train)):
        train[i][0] = re.sub(r'[^\w]', ' ', train[i][0]).split()
        train[i][1] = re.sub(r'[^\w]', '', train[i][1]).split()
        for ii in range(len(train[i][0])):
                train[i][0][ii] =  train[i][0][ii].upper()

for i in range(len(test)):
        test[i][0] = re.sub(r'[^\w]', ' ', test[i][0]).split()
        test[i][1] = re.sub(r'[^\w]', '', test[i][1]).split()
        for ii in range(len(test[i][0])):
                test[i][0][ii] =  test[i][0][ii].upper()

for i in range(len(train)):
        for ii in range(len(train[i][0])):
                vocabulary.append(train[i][0][ii])

vocabulary = list(dict.fromkeys(vocabulary))
vocabulary.sort()

vl = len(vocabulary)
for i in range(len(train)):
        pro_train.append([])
        for ii in range(vl):
                pro_train[i].append(0)
        for ii in range(len(train[i][0])):
                position = inVocabulary(train[i][0][ii], vocabulary)
                if position > -1:
                        pro_train[i][position] =  1
        pro_train[i].append(train[i][1][0])

for i in range(len(test)):
        pro_test.append([])
        for ii in range(vl):
                pro_test[i].append(0)
        for ii in range(len(test[i][0])):
                position = inVocabulary(test[i][0][ii], vocabulary)
                if position > -1:
                        pro_test[i][position] =  1
        pro_test[i].append(test[i][1][0])

#output processesd data
file = open("preprocessed_train.txt", "w")
for i in range(len(pro_train)):
        x = str()
        for ii in range(vl):
                x = x + str(pro_train[i][ii])
                x = x + ","
        x = x + pro_train[i][vl] + "\n"
        file.write(x)
file.close()

file = open("preprocessed_test.txt", "w")
for i in range(len(pro_test)):
        x = str()
        for ii in range(vl):
                x = x + str(pro_test[i][ii])
                x = x + ","
        x = x + pro_test[i][vl] + "\n"
        file.write(x)
file.close()

pb = [[], []]
t0 = 0
t1 = 0
for i in range(vl):
        pb[0].append(0)
        pb[1].append(0)

for i in range(len(pro_train)):
        if int(pro_train[i][vl]) == 0:
                t0 = t0 + 1
                for ii in range(vl):
                        if int(pro_train[i][ii]) == 1:
                                pb[0][ii] = pb[0][ii] + 1
        else:
                t1 = t1 + 1
                for ii in range(vl):
                        if int(pro_train[i][ii]) == 1:
                                pb[1][ii] = pb[1][ii] + 1

err = 0
one = 1
zero = 1
for i in range(len(pro_test)):
        one =  math.log(t1 / float(t1 + t0))
        zero = math.log(t0 / float(t1 + t0))
        #print(i, " || ", one, " || ", zero)
        for ii in range(vl):
                if int(pro_test[i][ii]) == 1:
                        p = math.log((pb[0][ii] + 1) / float(t0*2))
                        zero = zero + p
                        p = math.log((pb[1][ii] + 1) / float(t1*2))
                        one =  one + p

        if float(one) >= float(zero):
                p = 1
        else:
                p = 0
        if p != int(pro_test[i][vl]):
                err = err + 1
                #print(i, " || ", one, " || ", zero, " - ", p, " - ", pro_test[i][vl])

print(err, " - ", len(pro_test))

terr = 0
one = 1
zero = 1
for i in range(len(pro_train)):
        one =  math.log(t1 / float(t1 + t0))
        zero = math.log(t0 / float(t1 + t0))
        #print(i, " || ", one, " || ", zero)
        for ii in range(vl):
                if int(pro_train[i][ii]) == 1:
                        p = math.log((pb[0][ii] + 1) / float(t0*2))
                        zero = zero + p
                        p = math.log((pb[1][ii] + 1) / float(t1*2))
                        one =  one + p

        if float(one) >= float(zero):
                p = 1
        else:
                p = 0
        if p != int(pro_train[i][vl]):
                terr = terr + 1
                #print(i, " || ", one, " || ", zero, " - ", p, " - ", pro_train[i][vl])
print(terr, " - ", len(pro_train))
print("In the training set, the accuracy is " + str(1 - float(terr/float(len(pro_train)))) + ".\n")
print("In the testing set,  the accuracy is " + str(1 - float(err/ float(len(pro_test )))) + ".\n")

file = open("results.txt", "w")
file.write("Training on trainingSet.txt, testing on testSet.txt.\n")
file.write("In training set, there is " + str(len(pro_train)) + " examples and there are " + str(terr) + " that is incorrect\n" )
file.write("In the training set, the accuracy is " + str(1 - float(terr/float(len(pro_train)))) + ".\n")
file.write("In testing set, there is " + str(len(pro_test)) + " examples and there are " + str(err) + " that is incorrect\n" )
file.write("In the testing set, the accuracy is " + str(1 - float(err/float(len(pro_test)))) + ".\n")
file.close()
