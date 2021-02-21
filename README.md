# SimplePasswordManager v1.0
![dash](https://user-images.githubusercontent.com/78107602/108627869-af8e3a80-747d-11eb-9acd-af6a06d69124.PNG)

A Command-Line Password Manager created in Python. Uses SQLite Database for storing passwords on a local system, Uses AES256-CBC encryption for securing the database.

FEATURES:
- Secured with AES256-CBC Encryption
- Create totally randomized passwords (Mix of letters,Digits & Special characters) according to specified length            
 Example : ai4R>,DP<W9Da:9?Q3h;yR7ZI
- Easy Search, Create, Remove, Update, Delete CRUD operations.
- Hardcoded Master Password
- Auto quit after inactivity for 3 minutes 
- Automatically copy password to clipboard after selecting a credential
- Accidental shutdowns will automatically encrypt the database.

REQUIRED LIBRARIES: (Please install the following libraries before running the script/exe)
- Sqlite3
- tabulate
- string
- secrets
- pyperclip
- os
- pyAesCrypt
- base64
- time
- subprocess
- getpass


The Master password can be changed at line no 24 of SimplePassMngr.py
 24. coded_str = "Your Master Password Goes here" 
You can use pyinstaller to convert script to an Executable (.exe). 
Remember MasterPassword(Single password to get access to database) can be easily found in script, so it is highly recommended to use an executable for daily use.

--------------------------------------------------------
Licensed under the 
 MIT License ,Copyright (c) 2021 Amit Padmakar Kadam
-------------------------------------------------------
