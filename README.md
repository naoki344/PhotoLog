# PhotoLog


# 関連資料
 - [クラス図](https://www.draw.io/#G1EhqOFW9AxzTAZph284v3WfBPos__Qgrv)

# フォルダ構成(パッケージ構成)
```
PhotoLog/
    ┣ app/
    ┃    ┣ userinterface/ (ユーザーインターフェース層：api_interfaceから呼ばれapplicationにアクセスする)
    ┃    ┣ application/ (アプリケーション層)
    ┃    ┗ infrastructure/ (インフラストラクチャー層)(ルーター・WebサーバーからのAPIリクエストを受け付けappのuserinterfaceを呼び出す:flask依存)
         ┗ lib/
             ┗ model/ (モデルが集約されている)
```
<!--
フォルダ構成図制作用記号
┣ ┠ ┝ ├
┫ ┨ ┥ ┤ 
│ ┃
─ ━
┌ ┏ ┓ ┐
└ ┗ ┛ ┘
-->
