# ROS for solution's calculator 

## 概要

2021年度ロボットシステム学講義内にて上田隆一先生のプログラムを改造し、Raspberry Pi 3 Model Bを使用し課題2用に溶液、溶媒、溶質に関する計算機を製作したものです。

## 動作環境
```
- Raspberry Pi 3 Model B
- Ubuntu 20.04.3 LTS
```
## インストール
rosのワークスぺース内にて以下のコマンドを入力してください。
```
1. git clone https://github.com/mirokuwatanabe/kadai2-ros
2. cd kadai2-ros
3. catkin_make
```
## 実行方法
それぞれの端末に以下のコマンドを入力してください。
### 端末1
roscoreを立ち上げます。
```
roscore
```
"started core service [/rosout]"と表示されれば完了。
### 端末2
モード選択のための"mode.py"を立ち上げます。
```
rosrun mypkg mode.py
```
画面に選択肢が表示されたら完了。
### 端末3
計算機本体の"calculator.py"を立ち上げます。
```
rosrun mypkg calculator.py
```
起動後、端末2に数字を入力した後に文字が表示されれば完了。
### 端末4
"calculator.py"で計算された結果を表示します。
```
rostopic echo /answer
```
計算結果が表示されれば完了。
## 使用方法
端末2に現れた選択肢から計算したい内容を数字で選択。  
その後端末3の指示に従い数字を入力すると端末4に計算結果が表示されます。  
以後繰り返し。
## 実行結果

youtubeにアップ済み

[solution's calculator](https://youtu.be/FA-H9pMvlqI)

## ライセンス

[BSD 3-Clause "New" or "Revised" License](https://github.com/mirokuwatanabe/kadai2-ros/blob/b8bc0559bc651b46e4cf94c16e88b9653dd05eee/COPYING)
