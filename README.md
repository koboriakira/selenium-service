# Selenium API

## 目的

Seleniumを使ったスクレイピングを用意にできるよう、専用のAPIを設置した。

### いまできること



### やりたいができてないこと



## アーキテクチャ

- Dockerコンテナ上で動作
  - app: アプリケーション
    - python3.11
  - chrome: seleniarm/standalone-chromiumイメージをベースにした、Chromiumを起動するためのコンテナ
  - アプリケーション(appコンテナ)がSelenium(chromeコンテナ)にリモート接続し、Chromiumを操作する

### Selenium採用の理由

BeautifulSoupなどのHTMLパーサーを使っても良いが、スクレイピング対象のページがJavaScriptで動的に生成されるため、Seleniumを採用した。

## システム概要

クラスが少ないため省略。

## テスト

現時点でテストは未実装。

## 使用例

### プログラムの実行

```bash
docker-compose up
docker-compose exec app python -m tjpw_schedule.scraping
```
