cd $USER_HOME

echo "[*] Compiling and Installing Logiops..."
sleep 2

cd ~/content
git clone "https://github.com/PixlOne/logiops"
cd logiops
mkdir build
cd build
cmake ..
make
sudo make install
systemctl enable --now logid
cd ../..
rm -rf logiops
# === END(5) === #

sleep 2
banner