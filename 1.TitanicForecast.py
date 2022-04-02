import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from my_ml.ml_algorithms import *

filename = 'train.csv'
data_train = pd.read_csv(filename)
data_test = pd.read_csv('test.csv')
pd.set_option('display.max_columns', None)

#因为Cabin缺失值过多，所以放弃作为特征
data_train = data_train.drop(columns=['Cabin', 'PassengerId'])

#使用中位数处理年龄的缺失
data_train['Age'] = data_train['Age'].fillna(data_train['Age'].median())

ans = data_train['Embarked'].value_counts()
filled = ans.idxmax()
data_train['Embarked'] = data_train['Embarked'].fillna(filled)
data_train.loc[data_train['Sex'] == 'male', 'Sex'] = 0
data_train.loc[data_train['Sex'] == 'female', 'Sex'] = 1
data_train.loc[data_train['Embarked'] == 'C', 'Embarked'] = 0.0
data_train.loc[data_train['Embarked'] == 'Q', 'Embarked'] = 1.0
data_train.loc[data_train['Embarked'] == 'S', 'Embarked'] = 2.0

ans1 = data_train['Embarked'].value_counts()
filled1 = ans1.idxmax()
data_test['Embarked'] = data_test['Embarked'].fillna(filled1)
data_test.loc[data_test['Sex'] == 'male', 'Sex'] = 0
data_test.loc[data_test['Sex'] == 'female', 'Sex'] = 1
data_test.loc[data_test['Embarked'] == 'C', 'Embarked'] = 0.0
data_test.loc[data_test['Embarked'] == 'Q', 'Embarked'] = 1.0
data_test.loc[data_test['Embarked'] == 'S', 'Embarked'] = 2.0

train_corr = data_train.corr()
# a = plt.subplots(figsize=(15, 9))
# a = sns.heatmap(train_corr, vmin=-1, vmax=1, annot=True)
test_x = data_test[['Pclass', 'Age', 'Parch', 'Fare', 'Sex', 'Embarked']].values
test_X = add_bias(test_x)
x_data = data_train[['Pclass', 'Age', 'Parch', 'Fare', 'Sex', 'Embarked']].values
y_data = data_train['Survived'].values

#训练
alpha = 0.012
iters = 3333
X = mean_normalization(x_data)
X = add_bias(X)
T, costs = gradient_descend(iters, alpha, X, y_data)


#评估模型
ans = X@T
ans[ans >= 0.5] = 1
ans[ans < 0.5] = 0
accuracy = sum(ans == y_data)/len(ans)
print(accuracy)
