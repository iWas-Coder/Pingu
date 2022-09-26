echo "[*] Configuring ZSH..."
sleep 2
cd $MAIN_PWD
sudo cp ./config/zsh/zshrc ~/.zshrc
sudo ln -sf ~/.zshrc /root/.zshrc

sudo mkdir /usr/share/custom-zsh
sudo git clone "https://github.com/romkatv/powerlevel10k" /usr/share/custom-zsh/powerlevel10k
sudo cp ./config/zsh/p10k.zsh /usr/share/custom-zsh/.p10k.zsh
sudo git clone "https://github.com/zsh-users/zsh-syntax-highlighting" /usr/share/custom-zsh/zsh-syntax-highlighting
sudo git clone "https://github.com/zsh-users/zsh-autosuggestions" /usr/share/custom-zsh/zsh-autosuggestions
sudo mkdir /usr/share/custom-zsh/zsh-sudo
cd /usr/share/custom-zsh/zsh-sudo
sudo wget "https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/plugins/sudo/sudo.plugin.zsh"
sleep 2
echo "[+] ZSH Configured!"

sleep 2
banner
