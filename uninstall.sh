#!/usr/bin/env sh

set -e

LIB_TARGET="/usr/local/lib/los-torreros/"
BIN_TARGET="/usr/local/bin/"
APPLICATION_DIR="/usr/share/applications/"

rm $LIB_TARGET/los-torreros.py
rm $LIB_TARGET/icon.svg
rmdir $LIB_TARGET
rm $BIN_TARGET/los-torreros
rm $APPLICATION_DIR/los-torreros.desktop

