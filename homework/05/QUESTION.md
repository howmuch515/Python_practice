# 05
## q1.py
1. 0以上の整数nを引数としてとり、nの階乗を戻り値として返す再起関数factorialを定義しろ。
2. 0以上の整数nを引数としてとり、フィボナッチ数列のn番目の値を戻り値として返す再起関数fibonacciを定義しろ。ただしフィボナッチ数列の0番目の値を1, 1番目の値を1とする。
3. 上記の関数を使って0から10までのそれぞれの階乗、0から10番目のフィボナッチ数列の値をそれぞれ標準出力しろ。

## q2.py
次のようなProfessorクラスがある。

```python
class Professor():
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("I'am {}!".format(self.name))
```

Professorクラスを継承してRyoichiクラスを定義しろ。
なおRyoichiクラスの初期化メソッド内でnameに"Ryoichi"を代入すること。
また"I love Security!"と標準出力するgreet2メソッドを追加すること。

参考: [【Python基礎】クラスの継承](https://qiita.com/Tocyuki/items/155ec12bcd087803c817)

## q3.py
osがwindowsの場合は"calc.exe"を、linux, mac osの場合は"ls"コマンドを実行するプログラムをpythonを用いて書け
