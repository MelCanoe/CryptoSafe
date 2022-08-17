# =====Imports=====

import os
import hashlib
from colorama import Fore, Style
import getpass
import cryptocode
import sys
import readline # noqa

# =====Variables=====

# ====Functions=====


def show_registered_passwords(account_name):

    passwords_name = os.listdir(f'data/accounts/{account_name}')
    dash_complement = ''
    max_password_len = 0
    for password_name in passwords_name:
        if os.path.isfile(f'data/accounts/{account_name}/{password_name}'):
            if len(password_name[0:-8]) > max_password_len:
                max_password_len = len(password_name[0:-8])

    if max_password_len < len('PASSWORDS'):
        max_password_len = len('PASSWORDS')

    for dash in range(max_password_len):
        dash_complement = dash_complement + '-'

    password_spaces_complement = ''
    if max_password_len - len('PASSWORDS') >= 1:
        for space in range(max_password_len - len('PASSWORDS')):
            password_spaces_complement = password_spaces_complement + ' '

    passwords_name_len = 0
    for password_name in passwords_name:
        if os.path.isfile(f'data/accounts/{account_name}/{password_name}'):
            passwords_name_len += 1

    print(f'\n+-{dash_complement}-+')
    print(f'| PASSWORDS{password_spaces_complement} |')
    print(f'+-{dash_complement}-+')
    if passwords_name_len != 0:
        for password_name in passwords_name:
            if os.path.isfile(f'data/accounts/{account_name}/{password_name}'):
                spaces_complement = ''
                if max_password_len - len(password_name[0:-8]) >= 1:
                    for space in range(
                        max_password_len -
                        len(password_name[0:-8])
                    ):
                        spaces_complement = spaces_complement + ' '
                print(f'| {password_name[0:-8]}{spaces_complement} |')
    else:
        print('|           |')
    print(f'+-{dash_complement}-+\n')


def show_passwords(account_name):

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

    passwords_name = os.listdir(f'data/accounts/{account_name}')
    password_dash_complement = ''
    pwd_dash_complement = ''
    max_password_len = 0
    max_pwd_len = 0
    for password_name in passwords_name:
        if os.path.isfile(f'data/accounts/{account_name}/{password_name}'):
            with open(
                f'data/accounts/{account_name}/{password_name}',
                'r'
            ) as password_file:
                encrypted_password = password_file.readline()
                if encrypted_password[-1] == '\n':
                    encrypted_password = encrypted_password[0:-1]
                decrypted_password = cryptocode.decrypt(
                    encrypted_password,
                    master_password
                )
            if len(str(decrypted_password)) > max_pwd_len:
                max_pwd_len = len(str(decrypted_password))
            if len(password_name[0:-8]) > max_password_len:
                max_password_len = len(password_name[0:-8])

    if max_password_len < len('NAMES'):
        max_password_len = len('NAMES')

    if max_pwd_len < len('PASSWORDS'):
        max_pwd_len = len('PASSWORDS')

    for dash in range(max_password_len):
        password_dash_complement = password_dash_complement + '-'

    for dash in range(max_pwd_len):
        pwd_dash_complement = pwd_dash_complement + '-'

    password_spaces_complement = ''
    if max_password_len - len('NAMES') >= 1:
        for space in range(max_password_len - len('NAMES')):
            password_spaces_complement = password_spaces_complement + ' '

    pwd_spaces_complement = ''
    if max_pwd_len - len('PASSWORDS') >= 1:
        for space in range(max_pwd_len - len('PASSWORDS')):
            pwd_spaces_complement = pwd_spaces_complement + ' '

    passwords_name_len = 0
    for password_name in passwords_name:
        if os.path.isfile(f'data/accounts/{account_name}/{password_name}'):
            passwords_name_len += 1

    print(
        Fore.WHITE +
        f'\n+-{password_dash_complement}-+' +
        f'-{pwd_dash_complement}-+'
    )
    print(
        f'| NAMES{password_spaces_complement} |' +
        f' PASSWORDS{pwd_spaces_complement} |'
    )
    print(
        f'+-{password_dash_complement}-+' +
        f'-{pwd_dash_complement}-+'
    )
    if passwords_name_len != 0:
        for password_name in passwords_name:
            if os.path.isfile(f'data/accounts/{account_name}/{password_name}'):
                pass_spaces_complement = ''
                pwd2_spaces_complement = ''
                with open(
                    f'data/accounts/{account_name}/{password_name}',
                    'r'
                ) as password_file:
                    encrypted_password = password_file.readline()
                    if encrypted_password[-1] == '\n':
                        encrypted_password = encrypted_password[0:-1]
                if max_password_len - len(password_name[0:-8]) >= 1:
                    for space in range(
                        max_password_len -
                        len(password_name[0:-8])
                    ):
                        pass_spaces_complement = pass_spaces_complement + ' '
                decrypted_password = cryptocode.decrypt(
                    encrypted_password,
                    master_password
                )
                if max_pwd_len - len(decrypted_password) >= 1:
                    for space in range(
                        max_pwd_len -
                        len(decrypted_password)
                    ):
                        pwd2_spaces_complement = pwd2_spaces_complement + ' '
                print(
                    "".join([
                        f'| {password_name[0:-8]}{pass_spaces_complement} | ',
                        f'{Fore.YELLOW + decrypted_password}',
                        f'{Fore.WHITE + pwd2_spaces_complement} |'
                    ])
                )

    else:
        print('|       |           |')
    print(
        f'+-{password_dash_complement}-+' +
        f'-{pwd_dash_complement}-+'
    )
    print()


def create_password(account_name):

    print(
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        "Please type the new password's name."
    )
    new_password_name = str(input(
        Fore.BLUE +
        Style.NORMAL +
        'Password Name : ')
    )
    if os.path.isfile(
        f'data/accounts/{account_name}/{new_password_name}_pwd.key'
    ):
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            "This password already exist.\n"
        )
        return
    print(
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        "Please type the new password name's password."
    )
    new_password_pwd = str(getpass.getpass(
        Fore.BLUE +
        Style.NORMAL +
        'New Password : ')
    )
    print(
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        "Please confirm the new password name's password."
    )
    new_password_pwd_confirm = str(getpass.getpass(
        Fore.BLUE +
        Style.NORMAL +
        'Confirm Password : ')
    )
    if new_password_pwd != new_password_pwd_confirm:
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            "The confirmation password isn't the same as the password.\n"
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

    print()

    sys.stdout.write(
        Fore.WHITE +
        'Creating password [' +
        Fore.BLUE +
        '                ' +
        Fore.WHITE +
        ']...'
    )

    password_file = open(
        f'data/accounts/{account_name}/{new_password_name}_pwd.key',
        'w+'
    )

    for i in range(20):
        sys.stdout.write('\b')

    sys.stdout.write(
        Fore.BLUE +
        '####            ' +
        Fore.WHITE +
        ']...'
    )

    encrypted_password = cryptocode.encrypt(
        new_password_pwd,
        master_password
    )

    for i in range(20):
        sys.stdout.write('\b')

    sys.stdout.write(
        Fore.BLUE +
        '########        ' +
        Fore.WHITE +
        ']...'
    )

    password_file.write(encrypted_password)

    for i in range(20):
        sys.stdout.write('\b')

    sys.stdout.write(
        Fore.BLUE +
        '############    ' +
        Fore.WHITE +
        ']...'
    )

    password_file.close()

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
        f"'{new_password_name}' password created.\n"
    )


def modify_password(account_name, password_name):

    if not os.path.isfile(
        f'data/accounts/{account_name}/{password_name}_pwd.key'
    ):
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            f"'{password_name}' password doesn't exist.\n"
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
        f"Please type the new password of the '{password_name}' password."
    )
    new_password = getpass.getpass(Fore.BLUE + 'New Password : ')
    print(
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        f"Please retype the new password of the '{password_name}' password."
    )
    new_password_confirm = getpass.getpass(Fore.BLUE + 'Confirm Password : ')

    if new_password != new_password_confirm:
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            "The confirmation password isn't the same as the password.\n"
        )
        return

    new_encrypted_password = cryptocode.encrypt(
        new_password,
        master_password
    )

    with open(
        f'data/accounts/{account_name}/{password_name}_pwd.key',
        'w+'
    ) as new_password_file:
        new_password_file.write(new_encrypted_password)

    print(
        Fore.GREEN +
        Style.BRIGHT +
        '\n[+] ' +
        Fore.WHITE +
        Style.NORMAL +
        f"'{password_name}' password changed.\n"
    )


def remove_password(account_name, password_name):

    if not os.path.isfile(
        f'data/accounts/{account_name}/{password_name}_pwd.key'
    ):
        print(
            Fore.RED +
            Style.BRIGHT +
            '[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            f"'{password_name}' password doesn't exist."
        )
        return

    print(
        Fore.BLUE +
        Style.BRIGHT +
        '\n[i] ' +
        Fore.WHITE +
        Style.NORMAL +
        f"Removing '{password_name}' password..."
    )
    os.remove(
        f'data/accounts/{account_name}/{password_name}_pwd.key'
    )
    print(
        Fore.GREEN +
        Style.BRIGHT +
        '[+] ' +
        Fore.WHITE +
        Style.NORMAL +
        f"'{password_name}' password removed.\n"
    )
