# ROS for solution's calculator 

## 概要

2021年度ロボットシステム学講義内にて __上田隆一先生__ のプログラムを改造し、Raspberry Pi 3 Model Bを使用し課題2用に溶液,溶媒,溶質に関する計算機を製作したものです。

## 動作環境
```
- Raspberry Pi 3 Model B
- Ubuntu 20.04.3 LTS
```
## インストール
```
1. cd ~/catkin_ws
2. catkin_make
```
## 実行方法
### 端末1
```
roscore
```
### 端末2
```
rosrun mypkg mode.py
```
### 端末3
```
rosrun mypkg calculator.py
```
### 端末4
```
rostopic echo /answer
```

## 実行結果

youtubeにアップ済み

[solution's calculator ]()

## ライセンス

[BSD 3-Clause "New" or "Revised" License](https://github.com/mirokuwatanabe/kadai2-ros/blob/b8bc0559bc651b46e4cf94c16e88b9653dd05eee/COPYING)
