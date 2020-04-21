sudo apt upgrade
sudo apt update
sudo apt install streamlink unzip-y --fix-missing
wget -c https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip --no-check-certicicate
unzip ngrok-stable-linux-amd64.zip
./ngrok authtoken 4rYuvATyw19Cmk3yuxJDe_4SssNTEb27EE1U4es17pJ
sudo service apache2 start

