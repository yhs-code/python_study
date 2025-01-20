from . import _open_file_module


def send_hello():
    _open_file_module.open_file()
    print("发送消息hello")
    _open_file_module.close_file()
