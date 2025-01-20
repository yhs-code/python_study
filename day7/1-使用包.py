import project_package

project_package.send_message.send_hello()
print("-" * 100)
project_package.receive_message.receive_hello()
# 虽然_open_file_module会被间接导入，但是由于是私有模块，所以不建议使用
# project_package._open_file_module.open_file()
