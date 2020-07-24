import sys
import os
from termcolor import colored


def myanmar_flags():
    with open("small_mm_flags.txt", "rb") as f:
        banner = f.read()
        print(banner.decode("utf-8"))



def dependencies_install():
    try:

        print(colored("[*]updating termux", "yellow"))
        os.system("pkg update -y && upgrade -y ")
        print(colored("[*]Updated", "green"))
        os.system(
            "pkg install git python python2 vim neovim tmux zsh curl wget  ruby nodejs")
        print(colored("[+]finished installing some packages!", "green"))
        print(colored("[!] installing oh-my-zsh", "yellow"))
        try:
            os.system("""
                      curl -fsSL https://git.io/termux  | bash -s  -- -t -z -n -p
                  """)
        except:
            pass

        print(colored("installing amax_vimrc"))
        try:

            os.system("git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime")
            os.system("sh ~/.vim_runtime/install_awesome_vimrc.sh")
            print(colored("[!] done!","green"))
            print(colored("""\
                          [1] vim/neovim can config @ [ ~/.vim_runtime/vimrc/ ]
                          [2] you can install plugin for your fav progammig find on github search .
                          [3] you can clone fav* plugin at [~/.vim_runtime/my_plugins] folder
                          [4] then exit vim/nvim and open again
                          [5] still need help? post in [facebook group] or dm @me
                          [6] bye bye!

                          """),"yellow")
            os.system("sleep 10")
            print(colored("myanmar <3 termux ,nvim ,tmux ,zsh xD"))
            myanmar_flags()
            os.system("clear")
        except:
            pass


    except KeyboardInterrupt:
        print(colored("You Pressed C+c", "red"))
        sys.exit()
    except BaseException:
        pass


if __name__ == "__main__":
            myanmar_flags()

            os.system("sleep 1.0 && clear")
            print(colored("[*] You are about to setup programming env for Termux!","green"))
            os.system("sleep 1.0")


            dependencies_install()
