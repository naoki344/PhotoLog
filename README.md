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


# 2018/09/12 木目沢さんレビュー
> share_value_object.pyはドメインの言葉でファイル名を表現した方がいいかな。DDDのモジュールの項をおさらいしてみてください。

こちら不要なものと判断し削除しました。(前回のレビューを受けて `lib/model/folder.py` の中に移植しておりました)



> app_interface(interface層？）とappを分けた意味はあるのかな？

分けた経緯としては、ルーターみたいなの欲しいなと考え、 `api_interface` をrouterとして振る舞わせようと考えました。
`api_interface` フォルダをappの外に出したのは、appとは違うし、そもそもappの中身はrouterに依存しちゃダメなんじゃないかと考えてフォルダを別に置いた方がいいかなと考えたからです
	こちらいかがでしょうか、、？



> application層のクラスの名前はアプリケーションサービスを表す名詞の方がいいかな。（○○サービスのような)
> それから、application層のクラスのコンストラクタで色々やりすぎている気がします。initは生成のみ(例えばinfrastracture層のオブジェクトを渡すとか)にして、具体的なことはサービスメソッドで実装してみてください。

なんとなくapplication層とinfrastructure層混同していた気がします。違和感があったりした部分でしたのでアドバイス頂いてなるほどと合点がいきました。



