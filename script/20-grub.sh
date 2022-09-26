echo "[*] Creating GRUB Custom Configuration file..."
sudo cp ./config/grub/grub /etc/default/grub
sleep 1
echo "[+] File written to: /etc/default/grub"
sleep 2

echo "[*] Setting GRUB Custom theme..."
sudo cp -r ./config/grub/CyberRe /boot/grub/themes/CyberRe
sleep 1
echo -e "[+] Theme copied correctly!\n"
sleep 2

echo "[*] Showing disks and partitions..."
echo "-----------------------------------"
lsblk -np --output NAME,MOUNTPOINT
echo "-----------------------------------"

read -p "[?] Encrypted ROOT partition path (with /dev/...): " ROOT_PARTITION
read -p "[?] Decrypted ROOT partition name (e.g. cryptroot): " ROOT_NAME
read -p "[?] Encrypted HOME partition path (with /dev/...): " HOME_PARTITION
read -p "[?] Decrypted HOME partition name (e.g. crypthome): " HOME_NAME

banner

ROOT_UUID=$(sudo blkid $ROOT_PARTITION | grep -oP '(?<= UUID=").*?(?=")')
echo "[+] $ROOT_PARTITION -> UUID: $ROOT_UUID"
HOME_UUID=$(sudo blkid $HOME_PARTITION | grep -oP '(?<= UUID=").*?(?=")')
echo "[+] $HOME_PARTITION -> UUID: $HOME_UUID"

sleep 2
  
sudo sed -i "s/<ROOT_NAME>/$ROOT_NAME/g" /etc/default/grub
sudo sed -i "s/<ROOT_UUID>/$ROOT_UUID/" /etc/default/grub
sudo sed -i "s/<HOME_NAME>/$HOME_NAME/" /etc/default/grub
sudo sed -i "s/<HOME_UUID>/$HOME_UUID/" /etc/default/grub

sleep 2

echo "[*] Generating GRUB Configuration..."
sudo grub-mkconfig -o /boot/grub/grub.cfg

sleep 2

echo "[+] GRUB Configured!"

banner
