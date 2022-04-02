import gzip
import numpy as np
from my_ml import *
import  matplotlib.pyplot as plt


def read_zip_data(file_path, file_offset):
   with gzip.open(file_path) as f:
       data = np.frombuffer(f.read(), np.uint8, offset=file_offset)           #f返回文件的句柄
   return data

def load_data():
   file_root = r'E:/Desktop/fashion mnist/fashion mnist/'
   y_train = read_zip_data(file_root + 'train-labels-idx1-ubyte.gz', 8)
   x_train = read_zip_data(file_root + 'train-images-idx3-ubyte.gz', 16)    #读取出来后为线性数据
   x_train = x_train.reshape(len(y_train), 28, 28)            #len(y_train)表示有多少张图片
   y_test = read_zip_data(file_root + 't10k-labels-idx1-ubyte.gz', 8)
   x_test = read_zip_data(file_root + 't10k-images-idx3-ubyte.gz', 16)   #8和16为去掉文件头(文件存储机制)
   x_test = x_test.reshape(len(y_test), 28, 28)
   return x_train, y_train, x_test, y_test

def visualize_data(images, labels):
   class_names = list('ABCDEFGHIJ')
   plt.figure(figsize=(10, 10))
   for i in range(25):
       plt.subplot(5, 5, i+1)
       plt.xticks([])
       plt.yticks([])
       plt.imshow(images[i], cmap=plt.cm.binary)
       plt.xlabel(class_names[labels[i]])
   plt.show()

x_train, y_train, x_test, y_test=load_data()

#visualize_data(x_train,y_train)
x_train = x_train.reshape(x_train.shape[0],-1)

x_test = x_test.reshape(x_test.shape[0],-1)

#
HIDDEN_COUNTS=[50] #隐层的层数
OUTPUT_COUNTS=10
INPUT_COUNTS=x_train.shape[1]
nn=MyNeuralNetwork(INPUT_COUNTS,OUTPUT_COUNTS,HIDDEN_COUNTS,lr=0.08)

epoch = 30
for _ in range(epoch):
   for row_x,row_y in zip(x_train,y_train):
       x = row_x / 255*0.99 + 0.01
       y = np.zeros(10) + 0.01
       y[row_y] = 0.99
       nn.train(x,y)

scores = []
for row_x,row_y in zip(x_test,y_test):
   x = row_x / 255 * 0.99 + 0.01
   y = nn.query(x)
   scores.append(row_y == np.argmax(y))
print(np.count_nonzero(scores) / len(scores)