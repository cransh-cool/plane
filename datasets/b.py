import os

# 设置文件的相对路径
file_path = 'plane/trainval.txt'

# 检查文件是否存在
if os.path.exists(file_path):
    print("文件存在。")
else:
    print("文件不存在。")
