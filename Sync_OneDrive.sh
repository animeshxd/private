sudo apt update -y
sudo apt install libcurl4-openssl-dev -y --fix-missing
sudo apt install libsqlite3-dev -y --fix-missing
sudo snap install --classic dmd && sudo snap install --classic dub
git clone https://github.com/skilion/onedrive.git
cd onedrive
make
sudo make install
make DC=ldmd2
mkdir -p ~/.config/onedrive
cp ./config ~/.config/onedrive/config
nano ~/.config/onedrive/config
onedrive
