from . import _open_file_module


def receive_hello():
    _open_file_module.open_file()
    print("接收消息hello")
    _open_file_module.close_file()
