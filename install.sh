#!/usr/bin/env sh

set -e

LIB_TARGET="/usr/local/lib/los-torreros/"
BIN_TARGET="/usr/local/bin/"
APPLICATION_DIR="/usr/share/applications/"

if [ ! -d "$LIB_TARGET" ]; then
  mkdir $LIB_TARGET
fi

cp los-torreros.py $LIB_TARGET
cp los-torreros $BIN_TARGET
cp los-torreros.desktop $APPLICATION_DIR
