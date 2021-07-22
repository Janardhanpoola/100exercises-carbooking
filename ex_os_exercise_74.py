import os

path='C:/Users/jpoola/3D Objects/'

dir='Leetcode'

new_dir_path=os.path.join(path,dir)

os.mkdir(new_dir_path)


dirs=os.listdir(path)

print(dirs)