import os
import sys

def check_reboot():
    # """Returna True if the computer has a panding reboot"""
    return os.path.exists(os.path.join("Users", "Mcc", "Desktop", "module"))

def main():
    if check_reboot():
        print("panding Reboot ")
        sys.exit(1)
    
    print("Everything ok")

    sys.exit(0)




if __name__ == "__main__":
    main()