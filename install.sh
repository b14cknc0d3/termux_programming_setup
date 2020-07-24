echo "[!] updating ................................................"
sleep 0.3
pkg update

pkg upgrade
echo "[+] done....................................................!"

echo "[*] installing required package ............................!"
pkg install git curl  python
pip3 install termcolor

git clone https://github.com/b14cknc0d3/termux_programming_setup ~/tps

cd ~/tps
echo "[!] cd tps "
echo "[!] run -> python termux_programming_setup.py"



