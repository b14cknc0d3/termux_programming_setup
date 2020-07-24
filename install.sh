echo "[!] updating ..."
pkg update

pkg upgrade
echo "[+] done!"

echo "[*] installing required package "
pkg install git curl python3 python

git clone https://github.com/b14cknc0d3/termux_programming_setup ~/tps

cd ~/tps/termux_programming_setup

echo "[!] run -> python3 termux_programming_setup.py"



