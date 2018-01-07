# stellar-paper-wallet
CLI tool for making fancy printable stellar paper wallets to hold your lumens (XLM).

## Getting started

You would need to install [Pillow](http://pillow.readthedocs.io/en/3.0.x/installation.html), not PIL.

`python spw.py d1` creates a png of random keypair with design 1
`python spw.py d2` creates a png of random keypair with design 2
`python spw.py d3` creates a png of random keypair with design 3

`python spw.py --design --privatekey` creates a png of public/private keypair with design
