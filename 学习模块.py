import os
import hashlib
file_path = input("你需要的目录\n")#获取你需要的目录

current = os.listdir(file_path)#存储目录下的所有文件名
my_list = []
my_list2 = []
for current_file_name in current:
    current_path = os.path.join(file_path,current_file_name)
    if current_file_name[0] == ".":
        continue
    elif not os.path.isfile(current_path):
        continue
    with open(current_path,"rb") as f:
        bytes = f.read()
        readable_hash = hashlib.md5(bytes).hexdigest()
        if readable_hash not in my_list2:
            my_list2.append(readable_hash)
            my_list.append(current_path)
    f.close()
print(my_list)
print(len(my_list))




