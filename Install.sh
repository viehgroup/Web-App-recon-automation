#!/usr/bin/sh 

echo "Run this script with root previleges only !!"

apt update && apt upgrade -y

apt install golang  -y 

go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

go install github.com/tomnomnom/assetfinder@latest

go install github.com/projectdiscovery/httpx/cmd/httpx@latest

go install github.com/tomnomnom/waybackurls@latest

go install github.com/lc/gau/v2/cmd/gau@latest

go install github.com/ffuf/ffuf@latest

cp /root/go/bin/* /usr/bin/

echo "You Are Ready to GO"
