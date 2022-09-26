echo "[*] Configuring Ranger..."
sleep 2
cd $MAIN_PWD
cp -r ./config/ranger ~/.config/ranger
git clone "https://github.com/alexanderjeurissen/ranger_devicons" ~/.config/ranger/plugins
sudo ln -s ~/.config/ranger /root/.config/ranger
sleep 2
echo "[+] Ranger Configured!"

banner