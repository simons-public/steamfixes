#!/bin/sh

PATH=$PATH:.

function print(){
    echo $(tput setaf 2)$@$(tput sgr0)
}

if [ ! -f loader.so ]; then
    print Compile loader.so with \'make\' first
    exit 0
fi

print Testing without SteamAppId in env
LD_PRELOAD=${PWD}/loader.so sh -c 'whoami'
print End test

print Testing with SteamAppId in env
SteamAppId=555 LD_PRELOAD=${PWD}/loader.so sh -c 'whoami'
print End test
