# python-modint
python3用です。  
競技プログラミングでしばしば現れる整数を素数で割った余りを出力する問題のために、演算を行うと自動的に余りを取るようにしたクラスです。  
ModIntオブジェクトを生成すると普通の整数のように算術演算や比較演算、rangeを用いた繰り返し処理を行えます。  
a / b では aにbの逆元をかけます。  
a // b では通常の整数のようにaをbで割った商を返します。  
absやビット演算等は行えません。  

## 参考
[Pythonでmodintを実装してみた - Qiita](https://qiita.com/wotsushi/items/c936838df992b706084c)  
[operator --- 関数形式の標準演算子 — Python 3.7.4rc1 ドキュメント](https://docs.python.org/ja/3/library/operator.html)
