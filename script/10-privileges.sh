echo "[!] Checking current user..."
sleep 2
if [ "$EUID" -eq 0 ]; then
  echo "[-] Please do not run as ROOT."
  tput cnorm; exit 1
fi
echo "[+] Hello, $USER :D"
sleep 2
echo "[!] Checking if current session has sudo privileges..."
sleep 2
sudo pwd > /dev/null 2>&1
echo -e "[+] Sudo privileges obtained! Thank you <3\n"
sleep 2

banner
