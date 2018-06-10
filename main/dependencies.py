import os

def install(package):

    os.system("pip install " + package)




if __name__ == "__main__":
    install("discord.py")
