from faker import Faker

# Fakerインスタンスの生成。デフォルトでは英語のデータを生成します。
fake = Faker()

# 基本的な偽データの生成
print(fake.name())  # 例: John Doe
print(fake.address())  # 例: 539 Chad Motorway, Lake Jennifer, AL 65010
print(fake.email())  # 例: example@example.com
print(fake.date_of_birth())  # 例: 1978-06-09

#何を作るか
  #個人情報をreturn
  　#個人情報がランダムに作られる
  　　#ランダムに複数つくって、そこからデータを取る形式がよさそう？
    #ソートをかける機能
      #ソートの入力値
        #日本の県でソートをかけるようにする
          #クライアント
          #サーバー

  #何を作るかは今回のパイプを理解するのにぴったりなものがいい
    #送信と受信がどこからきているのか→プロセスの理解
      #serverとclientが親プロセスと子の関係？