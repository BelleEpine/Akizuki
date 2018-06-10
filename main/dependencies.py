import os
import subprocess

def install(package):
    os.system("pip install " + package)
    

def subprocess_install(package):
    subprocess.call(["pip", "install", package])


def local_os_install(package):
    os.system("pip install " + package)
    
    
if __name__ == "__main__":
    install("discord.py==0.16.12")

    #subprocess_install("discord.py==0.16.12")

    #local_os_install("PATH HERE")
	
	#local_os_install("discord.py-0.16.12.tar.gz")
	
    # backup methods ^^
    
