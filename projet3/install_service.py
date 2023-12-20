# install_service.py

import subprocess

def install_apache():
    try:
        subprocess.run(['sudo', 'apt-get', 'update'])
        subprocess.run(['sudo', 'apt-get', 'install', 'apache2'])
        print("Apache installed successfully.")
    except Exception as e:
        print(f"Error installing Apache: {e}")

def install_ssh():
    try:
        subprocess.run(['sudo', 'apt-get', 'install', 'openssh-server'])
        print("SSH installed successfully.")
    except Exception as e:
        print(f"Error installing SSH: {e}")

if __name__ == "__main__":
    install_apache()
    install_ssh()
