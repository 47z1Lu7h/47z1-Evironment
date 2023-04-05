#!/usr/bin/python
import os, time, signal, sys
from sys import stdout

def signal_handler(sig, frame):
    red()
    print("\n\t [!] Ctrl+C -> Ext1t1n6...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)

def black():
    BLACK = '\033[30m'
    stdout.write(BLACK)
def red():
    RED = '\033[1;31m'
    stdout.write(RED)
def green():
    GREEN = '\033[0;32m'
    stdout.write(GREEN)
def yellow():
    YELLOW = '\033[1;33m'
    stdout.write(YELLOW)
def blue():
    BLUE =  '\033[1;34m'
    stdout.write(BLUE)
def mag():
    MAGENTA = '\033[35m'
    stdout.write(MAGENTA)
def cyan():
    CYAN = '\033[1;36m'
    stdout.write(CYAN)
def white():
    WHITE =  '\033[1;37m'
    stdout.write(WHITE)
def under():
    UNDERLINE = '\033[4m'
    stdout.write(UNDERLINE)
def reset():
    RESET = '\033[0m'
    stdout.write(RESET)

banner = '''\n
 @@   @@   @@@@@@@@  @@@@@@@@  @@@  @@@      @@@  @@@  @@@@@@@@   @@@  @@@                       
 @@  !@!        @@!       @@!  @@!  @@!      @@!  @@@       @@!   @@!  @@@    !@!                
 !!!!!@!     !!!       !!!     !!!  !!!      !@!  !!!    !!!      @!!@!!!@    !:!  !:!           
     :::    ::        :: ::::  :::  :::::::  ::::: ::   ::        :::   :::   :::  :::  :::  ..  
@@@@@@@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@  
!@!       !@!  @!@  !@!  !@!  @!@  !@!  @!@  !@!!@!@!  !@! !@! !@!  !@!       !@!!@!@!    !@!    
!!!!!:    !@!  !!!  !!!  !!@!@!    !@!  !!!  !@!  !!!  !@!   ! !@!  !!!!!:    !@!  !!!    !!!    
:: ::::    ::::.     ::  ::   :::  ::::: ::   ::   ::  :::     ::   :: ::::   ::   ::     ::     
+ + + + ++ + + + + ++ + + ++ + + ++ + + + ++ + + + + + ++ ++ + + ++ + + + ~~> by 47z!Lu7h :)\n'''

def menu():
    blue()
    print('1 - Base Package "bspmw + zsh + polybar + rofi, etc ..."')
    print('2 - Nvim de nvchad')
    print('3 - google-chrome, Discord, Telegram ...')
    print('4 - KDE Rounded Corners + menu11')
    print('5 - VSCode Dark-Theme')
    print('6 - Htb-Xplorer tool')
    mag()
    print("0 - Exit")
    blue()

def main():
    mag()
    print("\t\n[+] Upgrading System... \n")
    blue()
    os.system("sudo apt update; sleep 2; sudo parrot-upgrade -y; sleep 2; sudo apt upgrade -y")
    time.sleep(2)
    mag()
    print("\t\n[+] Isntaling Packages & Dependecies... \n")
    blue()
    os.system("sudo apt install qttools5-dev libqt5x11extras5-dev libkf5configwidgets-dev libkf5globalaccel-dev libkf5notifications-dev kwin-dev  libcairo2-dev libqt5positioning5 libqt5location5 qtlocation5-dev qtpositioning5-dev qml-module-qtlocation qml-module-qtpositioning libxcb1-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-image0-dev libqt5x11extras5-dev libkf5configwidgets-dev libkf5crash-dev libkf5globalaccel-dev libkf5kio-dev libkf5notifications-dev kinit-dev kwin-dev libnotify-bin libxcb-randr0-dev libxcb-util0-dev libxcb-xkb-dev pkg-config xcb-proto libxcb-xrm-dev libasound2-dev libmpdclient-dev libiw-dev libpulse-dev libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libxcb-glx0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libpcre3-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev build-essential pkg-config python3-sphinx python3-packaging libuv1-dev libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev zsh zsh-autosuggestions polybar cmake cmake-data extra-cmake-modules git g++ gettext kitty bspwm rofi picom sxhkd feh dash bat neofetch git wget curl xclip net-tools openvpn html2text rlwrap gpick meson trash-cli xbacklight brightnessctl qt5ct qttools5-dev -y")
    time.sleep(2)
    os.system("wget https://github.com/lsd-rs/lsd/releases/download/0.23.1/lsd_0.23.1_amd64.deb -O lsd.deb; sleep 2; sudo dpkg -i lsd.deb && rm lsd.deb")
    time.sleep(2)
    red()
    print("\t\t\n[!] Bspwm instal3d!!!\n\n")
    time.sleep(2)

	    # ~ Cloning zsh plugins
    mag()
    print("\t\n[+] cloning zsh plugins \n")
    blue()
    time.sleep(2)
    os.system("sudo git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /usr/share/zsh/powerlevel10k")
    os.system("sudo git clone https://github.com/zsh-users/zsh-syntax-highlighting.git /usr/share/zsh/plugins/zsh-syntax-highlightiqng")
    os.system("sudo git clone --depth=1 -- https://github.com/marlonrichert/zsh-autocomplete.git /usr/share/zsh/plugins/zsh-autocomplete")
    os.system("sudo wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/plugins/sudo/sudo.plugin.zsh -P /usr/share/zsh/plugins/")
    time.sleep(2)

	    # ~ Make necesary folders in ~/.config & copy files
    mag()
    print("\t\n[+] Making necessary folders in ~/.config \n")
    blue()
    os.system("sudo rm -rf ~/.config/bspwm ~/.config/sxhkd/ ~/.config/picom ~/.config/polybar ~/.config/rofi ")
    os.system("cp -r config/* ~/.config/")
    os.system("chmod +x ~/.config/bspwm/bspwmrc ~/.config/polybar/pl45M4-p@ly.sh ~/.config/polybar/b5PWm-p@ly.sh ~/.config/polybar/bin/* ~/.config/bspwm/scripts/*")
    os.system("cp misc/.Xresources ~/.Xresources; cp misc/.p10k.zsh ~/.p10k.zsh; sudo cp misc/root.p10k.zsh /root/.p10k.zsh; cp misc/.zshrc ~/.zshrc; sudo ln -s -f $HOME/.zshrc /root;")
    os.system("sudo cp -r misc/usrShare/* /usr/share/; sudo cp -r misc/fonts/* /usr/share/fonts; sleep 2; fc-cache -v; sudo sed -i 's/bash/zsh/g' /etc/passwd; sleep 2; sudo cp -r config/bspwm/p1C5 /usr/share/wallpapers/")

	# Visual Studio Code
def visual():
    mag()
    print("\n[+] Installing Visual Studio Code... \n")
    blue()
    os.system("sudo apt update && sudo apt install software-properties-common apt-transport-https -y")
    time.sleep(2)
    os.system("wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")
    time.sleep(2)
    os.system("sudo add-apt-repository 'deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main'")
    os.system("sudo apt --fix-broken install -y && sudo apt install code")
    time.sleep(2)
    os.system("mkdir -p ~/.config/Code/User; sleep 1; cp  misc/code/user/settings.json ~/.config/Code/User; sleep 1; rm -rf ms_vscode_key_*; rm -rf microsoft.asc")

	# google chrome & discord & telegram..
def various():
    mag()
    print("\n\t[+]  Installing Discord & Telegram.. \n")
    blue()
    os.system("wget 'https://discord.com/api/download?platform=linux&format=deb' -O discord.deb")
    os.system("sudo apt --fix-broken install -y && sudo dpkg -i discord.deb && rm -rf discord.deb")
    time.sleep(2)
    os.system("sudo apt --fix-broken install -y && sudo apt install telegram-desktop")
    time.sleep(2)
    print("\n\t[+]  Installing google chrome \n")
    blue()
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("sudo apt install ./google-chrome-stable_current_amd64.deb -y; rm google-chrome-stable_current_amd64.deb; sudo apt install google-chrome-stable -y")
    mag()

	# NVIM-NVchad
def nvim():
    mag()
    print("\n\t[+] Installing Nvim de NVCHAD \n")
    blue()
    os.system("sudo apt purge neovim\* -y; wget https://github.com/neovim/neovim/releases/download/v0.8.1/nvim-linux64.deb; sudo apt install ./nvim-linux64.deb -y && rm nvim-linux64.deb")
    os.system("rm -rf ~/.config/nvim; rm -rf ~/.local/share/nvim; rm -rf ~/.cache/nvim; sudo rm -rf ~/.config/nvim; sudo rm -rf ~/.local/share/nvim; sudo rm -rf ~/.cache/nvim")
    time.sleep(2)
    os.system("git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim;")


	# KDE Rounded Corners
def roundC():
    mag()
    print("\n\t[+] Installing KDE-Rounded-Corners \n")
    blue()
    os.system("mkdir ~/d35kT@p/r3p0s; cd ~/d35kT@p/r3p0s")
    os.system("git clone https://github.com/matinlotfali/KDE-Rounded-Corners")
    time.sleep(2)
    os.system("cd KDE-Rounded-Corners; mkdir build; cd build; cmake ..; sleep 2; make; sudo make install")
    time.sleep(2)
    os.system("kwin --replace & disown")
    time.sleep(2)
    os.system("sudo apt-get install --reinstall plasma-widgets-addons -y && git clone https://github.com/prateekmedia/Menu11.git ~/.local/share/plasma/plasmoids/menu11; kquitapp5 plasmashell || killall plasmashell && kstart5 plasmashell;")

	# Nice t@@L! ;D
def htbXplorer():
    red()
    print("\n\t[+] Cloning htbXplorer from github \n")
    mag()
    os.system("sudo mkdir /opt/h4Ck/htbXplorer-Plus")
    os.system("sudo git clone https://github.com/4tz1Lu7h/htbXplorer-Plus.git /opt/h4Ck/htbXplorer-Plus")
    os.system("sudo chmod +x /opt/h4Ck/htbXplorer-Plus/htbXplorer")

if __name__ == '__main__':

    id = os.getuid()
    if id == 0:
        red()
        print("\n\t\t[!] -> You do not need to be ROOT to execute the tool!\n")

    else:
        while True:
            # show banner & menu
            red()
            print(banner)
            time.sleep(0.3)
            blue()
            menu()

            # get user imput & launch
            opcionMenu = input("\nChosse what you want to install >> \n")
            if opcionMenu == "1":
                yellow()
                print("\n\n\t\tInstalling Base package\n")
                main()

            elif opcionMenu == "2":
                yellow()
                print("\n\t\tInstalling Nvim-NvChad \n")
                nvim()

            elif opcionMenu == "3":
                mag()
                print("\n\t\tInstalling Discord, Chrome, Telegram, etc.. \n")
                various()

            elif opcionMenu == "4":
                yellow()
                print("\n\t\tInstalling KDE Rounded Corners\n")
                roundC()

            elif opcionMenu == "5":
                yellow()
                print("\n\tInstalling Vs-COde\n")
                visual()

            elif opcionMenu == "6":
                red()
                print("\n\t\t Nice tool! ;) ;)\n")
                htbXplorer()

            elif opcionMenu == "0":
                time.sleep(0.3)
                mag()
                print("\n\tBye!\n\n")
                break
            else:
                red()
                print("\n[!] You did'nt press any valid key ...")
                white()
                input("\t\t\n Press any key to continue")
