# SoundDino
用自己的聲音遊玩Chrome Dino

## 建立虛擬環境
`python -m venv SoundDino`

## 安裝所需套件
`pip install sounddevice`
`pip install scipy`
`pip install keyboard`
`pip install librosa`
`pip install scikit-learn`
`pip install resampy`

## 錄製自己的聲音作為model的training data
`python recorder.py`

## 利用自己的聲音train一個ML model
`python trainModel.py`

## 用train好的model辨識聲音，並交由程式控制鍵盤上下鍵來聲控小恐龍
`開啟網址 : https://chrome-dino-game.github.io/`
`python modelPredict.py`

# Play and enjoy
