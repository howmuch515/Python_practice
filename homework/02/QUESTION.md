# 02
## q1.py
3.141592 + "2.718281"をfloatとして計算し，結果を変数resultに格納しint型として出力せよ。

## q2.py
文字数15文字の3つの文字列a,i,cを以下のような処理で一つの文字列に混ぜた。
```
for j in range(15):
    print(a[j] + i[j] + c[j], end="")
    
# 出力結果
"AICvnoatnieflgiardbieltniytt!iy?a!!l??i!!t??y"
```
a,i,cを抽出してそれぞれ出力しろ。

## q3.py
数のリスト[3, 8, 10, 4, 110, 45, 89, 20, 67]を降順にソートし，文字列連結して出力しろ。

例：リスト[1, 2, 3]の場合，出力は"321"になる。

## q4.py
ユーザに標準入力された整数が閏年であれば"<入力値> is a leap year"、平年であれば"<入力値> is a normal year"を出力せよ．
不正な値が入力された際は"invalid input"と出力しプログラムを終了すること.

閏年の規則はグレゴリオ暦を採用するものとする．
ただし，if文のネストは1回までとする．

以下はグレゴリオ暦の規則である．
```
1.西暦年が4で割り切れる年は閏年．
2.ただし，西暦年が100で割り切れる年は平年．
3.ただし，西暦年が400で割り切れる年は閏年．
```
## q5.py
二重ループを用いて以下のような模様を出力しろ。
```
XOXOXOXOXO
OXOXOXOXOX
XOXOXOXOXO
OXOXOXOXOX
XOXOXOXOXO
OXOXOXOXOX
XOXOXOXOXO
OXOXOXOXOX
XOXOXOXOXO
OXOXOXOXOX
```
