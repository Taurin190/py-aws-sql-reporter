# py-aws-sql-reporter
AWS上にあるRDSのデータを与えられたSQLから読み、
エクセル形式にした複数のファイルをzipファイルでまとめて、
メールで添付するスクリプト。

## Design
AWSのData pipelineを用いて使えるシンプルなものを作りたい。
- SQLと設定を元にスクリプトを読みエクセルファイルを作成してローカルに保存する
- 全てのファイルをzipに固め、ローカルに保存する
- zipを取り出し、SESで送信する

## Usage
    sql-reporter retrieve
    sql-reporter compression
    sql-reporter send (not yet created)
    sql-reporter all
    sql-reporter help