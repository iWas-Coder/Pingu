cd $USER_HOME

echo "[*] Compiling and Installing Bento4 Tools..."
sleep 2

cd ~/content
git clone "https://github.com/axiomatic-systems/Bento4"
cd Bento4
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
sudo make install
cd ../..
rm -rf Bento4

sleep 2
banner