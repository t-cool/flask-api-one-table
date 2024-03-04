# Flask で作るシンプルな API

## 利用法

```
pip install flask
```

```
python server.py
```

ブラウザで http://localhost:5000/?word=hello のようにリクエストを送信します。


## 説明

データベースは、 [dict.db](./dict.db) です。

表のスキームは、以下の通りです。

```
CREATE TABLE dict (
    level INTEGER,
    en TEXT,
    sound TEXT,
    ja TEXT
);
```

データベース内のデータ構造は、以下の通りです。

```
level,en,sound,ja
1,something,サムスィング,何か，あるもの
1,also,オールソウ,もまた，さらに
1,all,オール,すべての，全部の
```

次のリクエストに対して、

```
http://localhost:5000?word=something
```

以下のようなレスポンスを返します。

```
{
  "level": 1,
  "ja": "何か，あるもの",
  "sound": "サムスィング"
}
```
