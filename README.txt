Assignment 4: Cryptanalysis
===========================
a4p1.py        - hacks the Caesar, transposition and affine ciphers in ciphers.txt
decrypted.txt  - output of a4p1.py, the twelve plaintexts in order
a4p2.py        - nomenclator cipher (substitution cipher plus a codebook)
a4p3.py        - completes simpleSubHacker.py's partial decipherment using regex dictionary matching
a1p1.py        - Caesar cipher from Assignment 1, used by a4p1.py
a2p3.py        - columnar transposition decryption from Assignment 2, used by a4p1.py

PREREQUISITES
-------------
Python 3.13.6 (Standard Library only)

USAGE
-----
Run any script from the root directory, for example:
python3 a4p1.py

Each script runs its own assertions and prints nothing if they all pass.
a4p1.py also writes decrypted.txt.
To call the functions directly, load a script interactively:
python3 -i a4p2.py
>>> decryptMessage('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Lj jia 1 py Lmfacjl', {'university': ['1']})
'At the university of Alberta'
