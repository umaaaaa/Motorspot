# -*-coding:utf-8-*-

# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    # app.run(host='0.0.0.0') # どこからでもアクセス可能に
    app.run(port=9999) # どこからでもアクセス可能に
