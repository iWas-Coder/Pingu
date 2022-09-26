echo "[*] Configuring Rofi..."
sleep 2
cd $MAIN_PWD
cp -r ./config/rofi ~/.config/rofi
sudo mv ~/.config/rofi/onedark.rasi /usr/share/rofi/themes
sleep 2
echo "[+] Rofi Configured!"
