# socketとosモジュールをインポートします
import socket
import os
from faker import Faker

fake = Faker('ja_JP')

people_info = []
for _ in range(200):
    person = {
        'name': fake.name(),
        'address': fake.address(),
        'phone_number': fake.phone_number()
    }
    people_info.append(person)

# UNIXソケットをストリームモードで作成します
# //パイプを作る役割と同じ
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# このサーバが接続を待つUNIXソケットのパスを設定します
server_address = '/tmp/socket_file'

# 以前の接続が残っていた場合に備えて、サーバアドレスをアンリンク（削除）します
try:
    os.unlink(server_address)
# サーバアドレスが存在しない場合、例外を無視します
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

# サーバアドレスにソケットをバインド（接続）します
sock.bind(server_address)

# ソケットが接続要求を待機するようにします
sock.listen(1)

# 無限ループでクライアントからの接続を待ち続けます
while True:
    # クライアントからの接続を受け入れます
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # ループが始まります。これは、サーバが新しいデータを待ち続けるためのものです。
        while True:
            prefectures = []
            for person in people_info:
                address = person['address']
                for char in ['都', '道', '府', '県']:
                    if char in address:
                        end_pos = address.index(char)
                        prefecture = address[:end_pos + 1]
                        prefectures.append(prefecture)
                        break

            prefectures_str = ', '.join(prefectures)
            connection.sendall(prefectures_str.encode('utf-8'))
            connection.sendall(b'END')
            print("終わり")


            data = connection.recv(1024)  # バッファサイズを大きくすることで一度にもっと多くのデータを受け取れるようにします
            if data:
                requested_prefecture = data.decode('utf-8').strip()
                print(f"Received request for people from {requested_prefecture}")

                # 要求された県を含む住所の人物を検索
                matched_people = [person for person in people_info if requested_prefecture in person['address']]
                
                # 検索結果を送信
                if matched_people:
                    for person in matched_people:
                        person_info = f"Name: {person['name']}, Address: {person['address']}, Phone: {person['phone_number']}\n"
                        connection.sendall(person_info.encode('utf-8'))
                else:
                    response = f"No people found from {requested_prefecture}\n"
                    connection.sendall(response.encode('utf-8'))
            else:
                print("No data received or data is incomplete.")

            # 受け取ったデータはバイナリ形式なので、それを文字列に変換します。
            # 'utf-8'は文字列のエンコーディング方式です。
            data_str =  data.decode('utf-8')

            # 受け取ったデータを表示します。
            print('Received ' + data_str)

            # もしデータがあれば（つまりクライアントから何かメッセージが送られてきたら）以下の処理をします。
            if data:
                # 受け取ったメッセージを処理します。
                response = 'Processing ' + data_str

                # 処理したメッセージをクライアントに送り返します。
                # ここでメッセージをバイナリ形式（エンコード）に戻してから送信します。
                connection.sendall(response.encode())

            # クライアントからデータが送られてこなければ、ループを終了します。
            else:
                print('no data from', client_address)
                break

    # 最終的に接続を閉じます
    finally:
        print("Closing current connection")
        connection.close()