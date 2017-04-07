#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:21:32 2017

@author: Takanori
"""

"""
scikit-learnを用いいたパーセプトロンのトレーニング
"""

from sklearn import datasets
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron

# irisデータセットをロード
iris = datasets.load_iris()

# 3, 4列目の特徴量を抽出
X = iris.data[:, [2, 3]]

# クラスラベルを取得
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

sc = StandardScaler()

# トレーニングデータの平均と標準偏差の計算
sc.fit(X_train)

# 平均と標準偏差を用いて標準化
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# エポック数40, 学習率0.1でパーセプトロンのインスタンスを生成
ppn = Perceptron(n_iter=40, eta0=0.1, random_state=0, shuffle=True)

# トレーニングデータをモデルに適合
ppn.fit(X_train_std, y_train)

# 予測する
y_pred = ppn.predict(X_test_std)

# 誤分類のサンプルの個数を表示
print('Misclassified samples: %d' % (y_test != y_pred).sum())








