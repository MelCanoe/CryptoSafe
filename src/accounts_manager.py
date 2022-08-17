# =====Imports=====

import subprocess
import os
from colorama import Fore, Style
import getpass
import readline # noqa
import sys
import hashlib

# =====Variables=====

# =====Functions=====


def show_accounts():

    unfiltered_accounts = os.listdir('data/accounts')
    dash_complement = ''
    max_account_len = 0
    accounts = []
    for account in unfiltered_accounts:
        if (os.path.isdir(f'data/accounts/{account}')):
            if account != "others":
                accounts.append(account)

    for account in accounts:
        if len(account) > max_account_len:
            max_account_len = len(account)

    if max_account_len < len('ACCOUNTS'):
        max_account_len = len('ACCOUNTS')

    for dash in range(max_account_len):
        dash_complement = dash_complement + '-'

    account_spaces_complement = ''
    if max_account_len - len('ACCOUNTS') >= 1:
        for space in range(max_account_len - len('ACCOUNTS')):
            account_spaces_complement = account_spaces_complement + ' '

    print(f'\n+-{dash_complement}-+')
    print(f'| ACCOUNTS{account_spaces_complement} |')
    print(f'+-{dash_complement}-+')
    if len(accounts) != 0:
        for account in accounts:
            spaces_complement = ''
            if max_account_len - len(account) >= 1:
                for space in range(max_account_len - len(account)):
                    spaces_complement = spaces_complement + ' '
            print(f'| {account}{spaces_complement} |')
    else:
        print('|          |')
    print(f'+-{dash_complement}-+\n')


def create_account():

    print(
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        "Please type the new account's name."
    )
    new_account_name = str(input(
        Fore.BLUE +
        Style.NORMAL +
        'Account Name : ')
    )
    if os.path.isdir(f'data/accounts/{new_account_name}'):
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            "This account already exist.\n"
        )
        return
    print(
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        "Please type the new account's master password."
    )
    new_account_password = str(getpass.getpass(
        Fore.BLUE +
        Style.NORMAL +
        'New Master Password : ')
    )
    print(
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        "Please confirm the new account's master password."
    )
    new_account_password_confirm = str(getpass.getpass(
        Fore.BLUE +
        Style.NORMAL +
        'Confirm Password : ')
    )
    if new_account_password != new_account_password_confirm:
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            "The confirmation password isn't the same as the password.\n"
        )
        return

    print()

    sys.stdout.write(
        Fore.WHITE +
        'Creating account [' +
        Fore.BLUE +
        '                ' +
        Fore.WHITE +
        ']...'
    )

    os.mkdir(f'data/accounts/{new_account_name}')

    for i in range(20):
        sys.stdout.write('\b')

    sys.stdout.write(
        Fore.BLUE +
        '####            ' +
        Fore.WHITE +
        ']...'
    )

    os.mkdir(f'data/accounts/{new_account_name}/safe')

    for i in range(20):
        sys.stdout.write('\b')

    sys.stdout.write(
        Fore.BLUE +
        '########        ' +
        Fore.WHITE +
        ']...'
    )

    encrypt_1_sha256 = hashlib.sha256()
    encrypt_1_sha256.update(new_account_password.encode())
    password_encrypt_1 = encrypt_1_sha256.hexdigest()

    encrypt_2_sha256 = hashlib.sha256()
    encrypt_2_sha256.update(password_encrypt_1.encode())
    password_encrypt_2 = encrypt_2_sha256.hexdigest()

    for i in range(20):
        sys.stdout.write('\b')

    sys.stdout.write(
        Fore.BLUE +
        '############    ' +
        Fore.WHITE +
        ']...'
    )

    with open(
        f'data/accounts/{new_account_name}/safe/master_pwd.key',
        'w+'
    ) as master_password_file:
        master_password_file.write(password_encrypt_2)
        master_password_file.close()

    for i in range(20):
        sys.stdout.write('\b')

    sys.stdout.write(
        Fore.BLUE +
        '################' +
        Fore.WHITE +
        ']...'
    )

    print()

    print(
        Fore.GREEN +
        Style.BRIGHT +
        '[+] ' +
        Fore.WHITE +
        Style.NORMAL +
        f"'{new_account_name}' account created.\n"
    )


def modify_pwd_account(account_name):

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
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        "Please type the new master password of the account."
    )
    new_master_password = getpass.getpass(Fore.BLUE + 'New Master Password : ')
    print(
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        "Please retype the new master password of the account."
    )
    new_master_confirm = getpass.getpass(Fore.BLUE + 'Confirm Password : ')

    if new_master_password != new_master_confirm:
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            "The confirmation password isn't the same as the password.\n"
        )
        return

    encrypt_1_sha256 = hashlib.sha256()
    encrypt_1_sha256.update(new_master_password.encode())
    password_1_sha256 = encrypt_1_sha256.hexdigest()

    encrypt_2_sha256 = hashlib.sha256()
    encrypt_2_sha256.update(password_1_sha256.encode())
    password_2_sha256 = encrypt_2_sha256.hexdigest()

    with open(
        f'data/accounts/{account_name}/safe/master_pwd.key',
        'w+'
    ) as new_master_password_file:
        new_master_password_file.write(password_2_sha256)

    print(
        Fore.GREEN +
        Style.BRIGHT +
        '\n[+] ' +
        Fore.WHITE +
        Style.NORMAL +
        f"'{account_name}' account's master password changed.\n"
    )


def remove_account(account_name):

    if not os.path.isdir(f'data/accounts/{account_name}'):
        print(
            Fore.RED +
            Style.BRIGHT +
            '[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            f"'{account_name}' account doesn't exist."
        )
        return

    print(
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        f"Removing '{account_name}' account..."
    )
    subprocess.check_output(['rm', '-rf', f'data/accounts/{account_name}'])
    print(
        Fore.GREEN +
        Style.BRIGHT +
        '[+] ' +
        Fore.WHITE +
        Style.NORMAL +
        f"'{account_name}' account removed.\n"
    )

