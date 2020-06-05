#dict

print(" \033[1;35mNumber seven\033[0m ".center(40,"*"))
from PIL import Image
import sys
from matplotlib import pyplot as plt
import numpy as np
print(sys.path)
print("AI的起起伏伏")
img = Image.open(U"图片\\ai0.png")
img_data = np.array(img)
plt.imshow(img_data[:,:,0])

print(img_data.shape)
plt.show()

# import getpass
# a = {"name":"WangWu","sex":"男","age":30}
# print(len(a))
# # name = input("What is your name?")
# name = getpass.getuser()
# age = getpass.getpass("密码：")
# print(name,age)
#
# if name == "Administrator" and age == str(a["age"]):
#     print("Welcome to LieWei")
# elif name == "Administrator":
#     print("age error")
# else:
#     print("sorry")


