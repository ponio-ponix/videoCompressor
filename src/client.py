import socket
# sysモジュールは、Pythonが実行されているシステムに関連する情報を取得したり、
# システム特有の操作を行ったりするためのPythonの組み込みモジュールです。
import sys

# TCP/IPソケットを作成します。
# ここでソケットとは、通信を可能にするためのエンドポイントです。
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)



# サーバが待ち受けている特定の場所にソケットを接続します。
server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

# サーバに接続を試みます。
# 何か問題があった場合、エラーメッセージを表示してプログラムを終了します。
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    # sys.exit()を使うと、Pythonプログラムをすぐに終了することができます。
    # ここでの引数1は、プログラムがエラーで終了したことを示すステータスコードです。
    sys.exit(1)

print('eee')

# サーバに接続できたら、サーバにメッセージを送信します。
try:
    # 送信するメッセージを定義します。
    # ソケット通信ではデータをバイト形式で送る必要があります。
    #data = sock.recv(1024)
    #data = data.decode('utf-8')
    #print('Server response: （生成された都道府県はこちらです）' + data)
    print('aaa')
    def receive_complete_message(sock, buffer_size=1024):
        """完全なデータが受信されるまでソケットからデータを受信します。"""
        buffer = b""
        while True:
            data = sock.recv(buffer_size)
            if not data:
                break  # サーバーからのデータ送信が完了した（または接続が切断された）
                print('break')
            buffer += data
            if buffer.endswith(b'END'):
                buffer = buffer[:-3]  # 'END'マーカーを削除
                break
        print('www')
        return buffer
    print('lll')

    # サーバーから完全なメッセージを受信
    try:
        print('rrr')
        complete_data = receive_complete_message(sock)
        # データをデコード
        print('mmm')
        message = complete_data.decode('utf-8')
        print('kkk')
        print('Server response: （生成された都道府県はこちらです）' + message)
    except UnicodeDecodeError as e:
        print('Unicode Decode Error:', e)
    except Exception as e:
        print('An error occurred:', e)
    print('yyy')



    message = input("どこの国のデータが欲しいか: ")
    message_bytes = message.encode('utf-8')
    sock.sendall(message_bytes)

    # サーバからの応答を待つ時間を2秒間に設定します。
    # この時間が過ぎても応答がない場合、プログラムは次のステップに進みます。
    #sock.settimeout(2)

    # サーバからの応答を待ち、応答があればそれを表示します。
    try:
        while True:
            # サーバからのデータを受け取ります。
            # 受け取るデータの最大量は32バイトとします。
            def receive_complete_message(sock, buffer_size=1024):
                """完全なデータが受信されるまでソケットからデータを受信します。"""
                buffer = b""
                while True:
                    data = sock.recv(buffer_size)
                    if not data:
                        break  # サーバーからのデータ送信が完了した（または接続が切断された）
                        print('break')
                    buffer += data
                    if buffer.endswith(b'END'):
                        buffer = buffer[:-3]  # 'END'マーカーを削除
                        break
                print('www')
                return buffer
            print('lll')

            # サーバーから完全なメッセージを受信
            try:
                print('rrr')
                complete_data = receive_complete_message(sock)
                # データをデコード
                print('mmm')
                message = complete_data.decode('utf-8')
                print('kkk')
                print('Server response: （生成された都道府県はこちらです）' + message)
            except UnicodeDecodeError as e:
                print('Unicode Decode Error:', e)
            except Exception as e:
                print('An error occurred:', e)
            print('yyy')
                    #data = sock.recv(1024)
                    #data = data.decode('utf-8')

            # データがあればそれを表示し、なければループを終了します。
            # if data:
            #     print('Server response: ' + data)
            # else:
            #     break

    # 2秒間サーバからの応答がなければ、タイムアウトエラーとなり、エラーメッセージを表示します。
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')


# すべての操作が完了したら、最後にソケットを閉じて通信を終了します。
finally:
    print('closing socket')
    sock.close()
