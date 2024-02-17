"""
From Genius_um. Under the name of MazeGroup (https://mazegroup.org/)
2024
"""

import os
from colorama import Fore, Back
import colorama
import time
import sys

colorama.init()

script_path = os.path.dirname(os.path.abspath(__file__))

remid_path = script_path + r"\remid.pth"

if not os.path.exists(remid_path):
    open(remid_path, "w").close()

class remid():
    def __init__(self, remid_path:str):
        """
        Remid Path Building :
        path/to/my/file.exe:program_name;path/to/my/file2.exe:program_name2
        """
        self.paths = open(remid_path).read().strip().split(";")

    def terminal(self):
        os.system("cls")
        print(Fore.YELLOW + "| " + Fore.LIGHTYELLOW_EX + "REMID Terminal"+ Fore.RESET)
        while True:
            print(Fore.GREEN + "| " + Fore.LIGHTGREEN_EX, end="")
            command = str(input())
            if command.strip():
                prompt = command.strip().split()
                program_name = prompt[0]
                args = []
                if len(prompt) >= 2:
                    args = prompt[1:]
                if program_name.lower() in ["rel", "reload"]:
                    self.paths = open(remid_path).read().strip().split(";")
                    print(Fore.YELLOW + "| " + Fore.LIGHTYELLOW_EX + "Reloaded"+ Fore.RESET)
                elif program_name.lower() in ["quit", "exit"]:
                    print(Fore.YELLOW + "| " + Fore.LIGHTYELLOW_EX + "Bye"+ Fore.RESET)
                    time.sleep(1)
                    sys.exit()
                elif program_name.lower() in ["li", "list"]:
                    print(Fore.YELLOW + "| " + Fore.BLUE + "Path list :" + Fore.RESET)
                    for path in self.paths:
                        path = path.split("|")
                        print(Fore.YELLOW + "|     " + Fore.BLUE + path[1] + " : " + Fore.GREEN + path[0])
                    print(Fore.YELLOW + "| " + Fore.BLUE + f"{len(self.paths)} path(s) registered.")
                elif program_name.lower() in ["cls", "clear"]:
                    os.system("cls")
                elif program_name.lower() in ["rs", "restart", "rb"]:
                    os.system("remid")
                else:
                    program_path = ""
                    founded = False
                    for path in self.paths:
                        path = path.split("|")
                        if len(path) >= 2:
                            if path[1].lower() == program_name.lower():
                                program_path = path[0]
                                founded = True
                    if founded:
                        blank = " "
                        final_command = f"py \"{program_path}\" {blank.join(args)}"
                        print(Fore.RESET, end="")
                        os.system(final_command)
                    else:
                        print(Fore.RED + "| " + Fore.LIGHTRED_EX + f"Error : Can find the program " + Back.LIGHTRED_EX + Fore.BLACK + "'" + program_name + "'" + Back.RESET + Fore.LIGHTRED_EX + " in the paths list." + Fore.RESET)

remid(remid_path).terminal()