# Discord-LogBot example
Version 1.0  

## 概要
Discord.pyで動くやつです(超 簡 単 説 明)  

こんな感じでBotが入ってるサーバーのメッセージとDMのメッセージのデータを収集します
![](https://api.shifts.tk/pngs/LogBot_example_sample.png)

一応画像もできるし、ボイスチャンネルのログ(参加時・離脱時)や、編集、削除された時のログも収集可能です

## 導入方法
適当にmain.pyの一番下にある`bot.run("TOKEN")`のTOKENにTOKENを入れればokです  
TOKENの入手方法は各自調べてください  

また別で用意されているlog.pyはCogで動かせるようになってます  
`bot.load_extension("Cog.log")`とかmain.pyでコード書き足せばokです(多分)  

replとかで実行しててTOKEN漏洩がこわいよーって人は`import os`とかしてあーだこーだすれば大丈夫です

## その他
このソースコードについてライセンスなどはありません 改変してもいいし、何してもokです  
自作発言はやめてね(モラルとしてもやめてほしい)