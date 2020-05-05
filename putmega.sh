sudo apt update -y
curl -o mega.deb https://mega.nz/linux/MEGAsync/xUbuntu_18.04/amd64/megacmd_1.2.0-10.1_amd64.deb
sudo dpkg --install mega.deb
sudo apt install --assume-yes --fix-broken
mega-cmd
echo "use 'mega-put' to upload & use 'mega-login email password' to login"
