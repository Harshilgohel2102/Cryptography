## DES Module

### Description
Implements DES encryption and decryption using `pyDes` library.

### Warning
DES is outdated and insecure. Use AES for production systems.

### Install Dependency
```bash
pip install pyDes
```

### Run
```bash
python des.py
```

## Triple DES (3DES) - Upgraded Version

### Features
- Uses CBC Mode
- Random IV for security
- Base64 encoding for safe transmission

### Install Dependency
```bash
pip install pycryptodome
```

### Run
```bash
python des3.py
```

### Note
3DES is more secure than DES but still not recommended for modern systems.
Prefer AES for production use.