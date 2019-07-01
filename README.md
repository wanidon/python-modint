# python-modint
競技プログラミングでしばしば見られる解を巨大な素数で割った余りを出力する問題用のクラスです。
ModIntオブジェクトを生成すると普通の整数のように算術演算や比較演算、rangeを用いたイテレータ生成を行えます。
a / b では aにbの逆元をかけます。
a // b では通常の整数のようにaをbで割った商を返します。
absやビット演算等は行えません。

##参考
[Pythonでmodintを実装してみた - Qiita](https://qiita.com/wotsushi/items/c936838df992b706084c)
[operator --- 関数形式の標準演算子 — Python 3.7.4rc1 ドキュメント](https://docs.python.org/ja/3/library/operator.html)
