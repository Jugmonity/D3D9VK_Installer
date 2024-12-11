import os
import shutil

def Main():
    if(os.path.exists("C:\\Program Files\\D3D9VK")):
        print("This Path is Exists and D3D9_VK Will be Downloaded in You're Folder")
        d3d9vk_folder = input("Please Write You're Folder To Copy D3D9_VK: ")
        shutil.copy("{}".format(os.getcwd() + "\\d3d9.dll", d3d9vk_folder))
        shutil.copy("{}".format(os.getcwd() + "\\d3d9vk.dll"), d3d9vk_folder)
        print("Copied Successfully!!! Created By Jugmonity")
    else:
        print("Not Founded D3D9_VK Folder... Before Use Please Download D3D9VK... Thanks!!!")
        os._exit(122)
    os._exit(345)

if __name__ == "__main__":
    Main()