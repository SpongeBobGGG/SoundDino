# SoundDino
用自己的聲音遊玩Chrome Dino <br>

[video tutorial](https://youtu.be/YufBR7AyX24)

## 建立虛擬環境
```shell
python -m venv SoundDino
```
<br>

## 安裝所需套件
```shell
pip install sounddevice
pip install scipy  
pip install keyboard  
pip install librosa  
pip install scikit-learn  
pip install resampy
```
<br>

## 錄製自己的聲音作為model的training data
```shell
python recorder.py
```
<br>

## 利用自己的聲音train一個ML model
```shell
python trainModel.py
```
<br>

## 用train好的model辨識聲音，並交由程式控制鍵盤上下鍵來聲控小恐龍
```shell
開啟網址 :joy: : https://chrome-dino-game.github.io/

python modelPredict.py
```
<br>

## Play and enjoy
