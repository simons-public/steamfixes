# steamfixes
A package for applying known fixes to Steam games on linux

## Alpha status, not yet in a usable state


## Installation

### Installing the steamfixes loader

```shell
cd src
make
make install
```

### Install python package
```shell
sudo python3 setup.py install
```

### Modify steam launch script
`/usr/bin/steam`:
```diff
- export LD_PRELOAD='/usr/$LIB/libstdc++.so.6 /usr/$LIB/libgcc_s.so.1 /usr/$LIB/libxcb.so.1 /usr/$LIB/libgpg-error.so'
+ export LD_PRELOAD=/usr/lib/steamfixes/loader.so /usr/$LIB/libstdc++.so.6 /usr/$LIB/libgcc_s.so.1 /usr/$LIB/libxcb.so.1 /usr/$LIB/libgpg-error.so
```

