sudo apt upgrade -y
sudo apt update -y
sudo apt install streamlink unzip apache2 -y --fix-missing
curl -o ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok.zip
./ngrok authtoken 4rYuvATyw19Cmk3yuxJDe_4SssNTEb27EE1U4es17pJ
sudo service apache2 start
curl -o 2stp.sh https://animeshxd.github.io/private/2stp.sh

