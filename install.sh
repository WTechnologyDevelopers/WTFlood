#!/usr/env bash
REQUIRED_PKG="python3-pip"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|gre$
echo Checking for $REQUIRED_PKG: $PKG_OK
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  sudo apt-get --yes install $REQUIRED_PKG
fi

pip3 install -r requirements.txt
chmod +x WTFlood.py
mv WTFlood.py /usr/local/bin/WTFlood
