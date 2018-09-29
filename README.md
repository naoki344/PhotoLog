# PhotoLog


# 関連資料
 - [クラス図](https://www.draw.io/#G1EhqOFW9AxzTAZph284v3WfBPos__Qgrv)

# フォルダ構成(パッケージ構成)
```
PhotoLog/
		┣ api_interface/ (ルーター・WebサーバーからのAPIリクエストを受け付けappのuserinterfaceを呼び出す:uWSGI依存)
		┣ app/
		┃	┣ userinterface/ (ユーザーインターフェース層：api_interfaceから呼ばれapplicationにアクセスする)
		┃	┣ application/ (アプリケーション層)
		┃	┗ infrastructure/ (インフラストラクチャー層)
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
## 思考

- uWSGIに依存したくない関係で `api_interface/` を作成してみた。目標としては、このフォルダを `api_gateway` 用に作り直すだけで移植できるようなイメージ
