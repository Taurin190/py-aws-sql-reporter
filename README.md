# py-aws-sql-reporter
AWS上にあるRDSのデータを与えられたSQLから読み、
エクセル形式にした複数のファイルをzipファイルでまとめて、
メールで添付するスクリプト。

## Design
AWSのData pipelineを用いて使えるシンプルなものを作りたい。
- SQLと設定を元にスクリプトを読みエクセルファイルを作成してS3に保存する
- 全てのファイルが作成されていることを確認して、ダウンロードしてzipに固め、固めたファイルをs3に上げる
- zipを取り出し、SESで送信する

## Usage
    ./aws-sql-reporter retrieve [sqlファイルパス]
    ./aws-sql-reporter compression
    ./aws-sql-reporter send