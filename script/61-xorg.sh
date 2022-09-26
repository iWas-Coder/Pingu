echo "[*] Configuring Xorg..."
sleep 2
cd $MAIN_PWD
sudo cp ./config/xorg/xinitrc /etc/X11/xinit/xinitrc
sudo cp ./config/xorg/xprofile ~/.xprofile
sleep 2
echo "[+] Xorg Configured!"

sleep 2
