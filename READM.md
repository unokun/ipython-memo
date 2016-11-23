# Summary
IPythonデータサイエンスクックブックメモ

# python環境の構築
Mac OS X Sieraで行った。
pyenvを使って実行環境を構築した。

```
pyenv install anaconda3-4.1.1
pyenv global anaconda3-4.1.1
```

# 1章 IPythonによる対話的コンピューティング入門
## レシピ1.1 IPython notebook入門
使い方
- notebookを開く
- セルに処理を入力する
- Shift-Enterで評価する

### 実行履歴
[recipi_1.1](sec1/recipi_1.1.ipynb)

### リンク
- [Jupyter Notebook Viewer](http://nbviewer.jupyter.org/)
- [The Jupyter Notebook — IPython](https://ipython.org/notebook.html)
- [The Jupyter notebook — Jupyter Notebook 5\.0\.0\.dev documentation](http://jupyter-notebook.readthedocs.io/en/latest/)
- [IPython Notebook チュートリアル \- Qiita](http://qiita.com/payashim/items/d4fe5227b21a5215e78b)
- [【チュートリアル】IPythonNotebook：再生可能でインタラクティブなWebブラウザ上で作業できるIPython実行用ノート| DERiVE コンピュータビジョン ブログ](http://derivecv.tumblr.com/post/95686651704)

## レシピ1.2 初めてのIPython探索データ分析
csvファイルをダウンロードできなかった。

## レシピ1.3 高速配列計算のためのNumPy多次元配列
###リンク
- [The N\-dimensional array \(ndarray\) — NumPy v1\.11 Manual](https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html)
## レシピ1.4 カスタムmagicコマンドによるIPython拡張の作成
## レシピ1.5 IPythonの設定システム
できなかった。

## レシピ1.6 簡単なIPythonカーネルの作成
できなかった。

# 2章 対話的コンピューティングのベストプラクティス
## レシピ2.1 Python 2かPython3かの選択
Python 3を使っていく(過去の遺産はない)。

## レシピ2.7 noseを使った単体テスト
### 概要
- test_XXXメソッドをテストしてくれる
- setup, teardownが使える。
- Mockが使える
- テストごとにsetup, teadownで一時ファイルを使う場合には、そのパスをインスタンス変数に覚えておく。

### テストクラス
```
class TestHTTPHandler(HTTPHandler):
    TEST_FOLDER = ''

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_XXX(self):
        pass
```

### 実行
```
$ nosetests
.
----------------------------------------------------------------------
Ran 2 tests in 0.018s

OK

# --nocaptureを付けると標準出力への出力が表示される
$ nosetests --nocapture
```

### 網羅率を調べる
```
$ pip install coverage

$ nosetests --with-cov --cover-package defaults
..
Name          Stmts   Miss  Cover
---------------------------------
defaults.py      11      1    91%
----------------------------------------------------------------------
Ran 2 tests in 0.021s

OK
```
