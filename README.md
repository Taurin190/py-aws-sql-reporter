# py-aws-sql-reporter
AWS上にあるRDSのデータを与えられたSQLから読み、
エクセル形式にした複数のファイルをzipファイルでまとめて
S3にアップロードするスクリプト。

## Design
AWSのData pipelineを用いて使えるシンプルなものを作りたい。
- SQLと設定を元にスクリプトを読みエクセルファイルを作成してローカルに保存する
- 全てのファイルをzipに固め、ローカルに保存する
- S3にzipファイルをアップロードする
- ~~zipを取り出し、SESで送信する~~

## Memo
- SESは現状限られたリージョンのみ使用可能で日本リージョンでは使えない。
- 

## ToDo
- 設計を変えたい
  - binではオプション等を読み必要なserviceのコマンドを使う
  - serviceは何をするかというのが分かるメソッドにする
  - databaseやexcel、S3を触る部分はgatewayというまとまりにする
- [x] Python 2系のライブラリに依存していたので修正したい。
   
## Usage
    sql-reporter retrieve
    sql-reporter compression
    sql-reporter send (not yet created)
    sql-reporter all
    sql-reporter help