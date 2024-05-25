# ソースコードの構成、概要  

## 使用技術 
- APサーバー  
    - Django 
    - Gunicorn(WSGI)   
- Webサーバー  
    - Nginx 
    - Let's Encrypt
- バージョン管理
    - git
    - GitHub
- ビルドツール
    - Docker 
    - docker compose 
- デプロイ
    - EC2

## 構成  
fib_api/  
├── docker-compose.yml  
├── Dockerfile  
├── Dockerfile.nginx  
├── nginx.conf  
├── README.md  
├── requirements.txt  
├── nginx/certs  
│   └── server.password  
└── src/  
    ├── fib/  
    ├── fib_api/  
    ├── front/  
    └── manage.py  

## 概要 
### src/fib  
- views.py フィボナッチ数列の計算、jsonで返す  
- tests.py ユニットテスト  
- urls.py リクエストに対するルーティング  
### src/fib_api  
- settings.py プロジェクトの設定  
### src/front  
- ドメインでのリクエストで表示するページを作成  
### nginx  
- nginx.conf サーバの設定, gunicornの設定  
- Dockerfile.nginx nginxのイメージを作成  
### docker  
- services:fib_api  
- services:nginx  

## 保守運用性  
### EC2インスタンス  
- EC2インスタンスでユーザー名を変更  
- インバウンドルールを変更  

### nginx  
- SSL証明書を配置  

## 変更容易性  
- docker-composeで簡単なデプロイ  

