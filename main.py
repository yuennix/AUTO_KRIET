import subprocess
import sys
import os

if __name__ == "__main__":
    # Clear visible screen and clear the terminal scrollback buffer
    # This works in both Termux (Android) and regular Linux terminals
    # \033[H moves cursor to top-left, \033[2J clears screen, \033[3J clears scrollback
    sys.stdout.write('\033[H\033[2J\033[3J')
    sys.stdout.flush()
    
    # Also use os.system as fallback for older terminals
    os.system("clear 2>/dev/null || printf '\\033[H\\033[2J\\033[3J'")
    

    # Launch the real script
    subprocess.run([sys.executable, "weynnew.py"])
