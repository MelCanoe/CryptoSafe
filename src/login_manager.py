# =====Imports=====

import os
from colorama import Fore, Style
import getpass
import readline # noqa
import hashlib

# =====Variables=====

# =====Functions=====


def login(account_name):
    if not os.path.isdir(f'data/accounts/{account_name}'):
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            f"'{account_name}' account doesn't exist.\n"
        )
        return

    print(
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        "Please type the master password of the account."
    )
    master_password = getpass.getpass(Fore.BLUE + 'Master Password : ')

    encrypt_1_sha256 = hashlib.sha256()
    encrypt_1_sha256.update(master_password.encode())
    password_1_sha256 = encrypt_1_sha256.hexdigest()

    encrypt_2_sha256 = hashlib.sha256()
    encrypt_2_sha256.update(password_1_sha256.encode())
    password_2_sha256 = encrypt_2_sha256.hexdigest()

    with open(
        f'data/accounts/{account_name}/safe/master_pwd.key',
        'r'
    ) as master_pwd_file:
        real_master_password = master_pwd_file.readline()
        master_pwd_file.close()

    if real_master_password != password_2_sha256:
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            "Incorrect master password.\n"
        )
        return

    print(
        Fore.GREEN +
        Style.BRIGHT +
        '\n[+] ' +
        Fore.WHITE +
        Style.NORMAL +
        f"You're now logged as '{account_name}'.\n"
    )

    return True
