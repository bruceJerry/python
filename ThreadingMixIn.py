import threading
import socketserver
import os
import time


class TcpServerRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(100)
            if data:
                if data == b"bye":
                    break
                data_str = bytes.decode(data)
                response = "%s" % data_str
                print("send response [pid:data] = [%s]" % response)
                self.request.send(data)

    def setup(self):  # 连接创建的时候调用一次
        print("tcp client connected, ip = [%s], port = [%d]" % self.client_address)

    def finish(self):
        print("finish------------")
        self.request.close()


class MyServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    pass


def main():
    server = MyServer(("0", 5000), TcpServerRequestHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print("tcp server is running")
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt as e:
            print("用户停止")
            break

    server.socket.shutdown(1)
    server.socket.close()
    print("main exit")


if __name__ == '__main__':
    main()

