# =====Imports=====

import os
from colorama import Fore, Style
import readline # noqa
import accounts_manager
import login_manager
import passwords_manager

# =====Variables=====

cryptosafe_title = """
   ____                  _          ____         __
  / ___|_ __ _   _ _ __ | |_ ___   / ___|  __ _ / _| ___
 | |   | '__| | | | '_ \| __/ _ \  \___ \ / _` | |_ / _ \\
 | |___| |  | |_| | |_) | || (_) |  ___) | (_| |  _|  __/
  \____|_|   \__, | .__/ \__\___/  |____/ \__,_|_|  \___|
  ===========|___/|_|====================================
""" # noqa

login_account = None
login_account_name = None

# =====Functions=====


def main():
    global login_account
    global login_account_name
    input_command = str(input(Fore.WHITE + Style.NORMAL + ': '))

    if input_command.split() == []:
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            'No command typed.\n'
        )
        main()

    elif input_command == 'help' or input_command[0:5] == 'help ':
        if len(input_command.split()) >= 2:
            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'help' command takes 0 argument but ",
                    f'{len(input_command.split()) - 1} was given.\n'
                ])
            )
            main()
        else:
            print()
            print('COMMANDS                     DESCRIPTIONS\n')
            print('exit                         exit the software')
            print('help                         display commands')
            print('clear                        remove outputs\n')
            print('-------------------------------------------\n')
            print('ACCOUNT COMMANDS             DESCRIPTIONS\n')
            print(
                'show accounts                ' +
                'display existing accounts'
            )
            print(
                'create account               ' +
                'execute the account creation procedure'
            )
            print(
                'modify account pwd [account] ' +
                'execute the account password modification procedure'
            )
            print(
                'remove account [account]     ' +
                'execute the account removing procedure'
            )
            print(
                'login [account]              ' +
                'execute the login procedure'
            )
            print(
                'logout                       ' +
                'logout yourself\n'
            )
            print('-------------------------------------------\n')
            print('PASSWORDS COMMANDS           DESCRIPTIONS\n')
            print(
                'show registered passwords    ' +
                "display all passwords's name without displaying passwords."
            )
            print(
                'show passwords               ' +
                Fore.YELLOW +
                "display passwords. this command will display all of " +
                "your passwords without any protection" +
                Fore.WHITE
            )
            print(
                'create password              ' +
                'execute the password creation procedure'
            )
            print(
                'modify password [password]   ' +
                'execute the password modification procedure'
            )
            print(
                'remove password [password]   ' +
                'execute the password removing procedure\n'
            )
            main()

    elif input_command == 'exit' or input_command[0:5] == 'exit ':
        if len(input_command.split()) >= 2:
            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'exit' command takes 0 argument but ",
                    f'{len(input_command.split()) - 1} was given.\n'
                ])
            )
            main()
        else:
            exit()

    elif input_command == 'clear' or input_command[0:6] == 'clear ':
        if len(input_command.split()) >= 2:
            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'clear' command takes 0 argument but ",
                    f'{len(input_command.split()) - 1} was given.\n'
                ])
            )
            main()
        else:
            os.system('clear')
            print(Fore.YELLOW + Style.BRIGHT + cryptosafe_title)
            main()

    elif (input_command == 'show accounts' or
          input_command[0:14] == 'show accounts '):

        if len(input_command.split()) >= 3:
            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'show accounts' command takes 0 argument but ",
                    f'{len(input_command.split()) - 2} was given.\n'
                ])
            )
            main()
        else:
            accounts_manager.show_accounts()
            main()

    elif (input_command == 'create account' or
          input_command[0:15] == 'create account '):

        if len(input_command.split()) >= 3:
            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'create account' command takes 0 argument but ",
                    f'{len(input_command.split()) - 2} was given.\n'
                ])
            )
            main()

        else:
            if login_account:
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    '\n[!] ' +
                    Fore.WHITE +
                    Style.NORMAL +
                    "You have to logout yourself to create an account.\n"
                )
                main()
            else:
                accounts_manager.create_account()
                main()

    elif (input_command == 'modify account pwd' or
          input_command[0:19] == 'modify account pwd '):

        if len(input_command.split()) >= 5 or len(input_command.split()) <= 3:

            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'modify account pwd' command takes 1 argument but ",
                    f'{len(input_command.split()) - 3} was given.\n'
                ])
            )
            main()

        else:
            if login_account:
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    '\n[!] ' +
                    Fore.WHITE +
                    Style.NORMAL +
                    "".join([
                        "You have to logout yourself ",
                        "to modify an account password.\n"
                    ])
                )
                main()
            else:
                accounts_manager.modify_pwd_account(input_command.split()[3])
                main()

    elif (input_command == 'remove account' or
          input_command[0:15] == 'remove account '):

        if len(input_command.split()) >= 4 or len(input_command.split()) <= 2:

            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'remove account' command takes 1 argument but ",
                    f'{len(input_command.split()) - 2} was given.\n'
                ])
            )
            main()

        else:
            if login_account:
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    '\n[!] ' +
                    Fore.WHITE +
                    Style.NORMAL +
                    "You have to logout yourself to remove an account.\n"
                )
                main()
            else:
                accounts_manager.remove_account(input_command.split()[2])
                main()

    elif (input_command == 'login' or
          input_command[0:6] == 'login '):

        if len(input_command.split()) >= 3 or len(input_command.split()) <= 1:

            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'login' command takes 1 argument but ",
                    f'{len(input_command.split()) - 1} was given.\n'
                ])
            )
            main()

        else:

            if login_account:
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    '\n[!] ' +
                    Fore.WHITE +
                    Style.NORMAL +
                    f"You're already logged as '{login_account_name}'\n"
                )
                main()

            else:

                login_return = login_manager.login(input_command.split()[1])
                if login_return:
                    login_account = True
                    login_account_name = input_command.split()[1]

                main()

    elif (input_command == 'logout' or
          input_command[0:7] == 'logout '):

        if len(input_command.split()) >= 2:

            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'logout' command takes 0 argument but ",
                    f'{len(input_command.split()) - 1} was given.\n'
                ])
            )
            main()

        else:
            if login_account:
                login_account = None
                login_account_name = None
                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    '\n[+] ' +
                    Fore.WHITE +
                    Style.NORMAL +
                    "You have been logged out.\n"
                )
                main()

            else:
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    '\n[!] ' +
                    Fore.WHITE +
                    Style.NORMAL +
                    "You are not login.\n"
                )
                main()

    elif (input_command == 'show registered passwords' or
          input_command[0:26] == 'show registered passwords '):

        if len(input_command.split()) >= 4:

            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'show registered passwords' ",
                    "command takes 0 argument but ",
                    f'{len(input_command.split()) - 3} was given.\n'
                ])
            )
            main()

        else:
            if login_account:
                passwords_manager.show_registered_passwords(login_account_name)
                main()

            else:
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    "\n[!] " +
                    Fore.WHITE +
                    Style.NORMAL +
                    "You have to login.\n"
                )
                main()

    elif (input_command == 'show passwords' or
          input_command[0:15] == 'show passwords '):

        if len(input_command.split()) >= 3:

            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'show passwords' ",
                    "command takes 0 argument but ",
                    f'{len(input_command.split()) - 2} was given.\n'
                ])
            )
            main()

        else:
            if login_account:
                passwords_manager.show_passwords(login_account_name)
                main()

            else:
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    "\n[!] " +
                    Fore.WHITE +
                    Style.NORMAL +
                    "You have to login.\n"
                )
                main()

    elif (input_command == 'create password' or
          input_command[0:16] == 'create password '):

        if len(input_command.split()) >= 3:

            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'create password' ",
                    "command takes 0 argument but ",
                    f'{len(input_command.split()) - 2} was given.\n'
                ])
            )
            main()

        else:

            if login_account:
                passwords_manager.create_password(login_account_name)
                main()

            else:
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    "\n[!] " +
                    Fore.WHITE +
                    Style.NORMAL +
                    "You have to login.\n"
                )
                main()

    elif (input_command == 'modify password' or
          input_command[0:16] == 'modify password '):

        if len(input_command.split()) >= 4 or len(input_command.split()) <= 2:

            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'create password' ",
                    "command takes 1 argument but ",
                    f'{len(input_command.split()) - 2} was given.\n'
                ])
            )
            main()

        else:

            if login_account:
                passwords_manager.modify_password(
                    login_account_name,
                    input_command.split()[2]
                )
                main()

            else:
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    "\n[!] " +
                    Fore.WHITE +
                    Style.NORMAL +
                    "You have to login.\n"
                )
                main()

    elif (input_command == 'remove password' or
          input_command[0:16] == 'remove password '):

        if len(input_command.split()) >= 4 or len(input_command.split()) <= 2:

            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[!] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'remove password' ",
                    "command takes 1 argument but ",
                    f'{len(input_command.split()) - 2} was given.\n'
                ])
            )
            main()

        else:

            if login_account:
                passwords_manager.remove_password(
                    login_account_name,
                    input_command.split()[2]
                )
                main()

            else:
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    "\n[!] " +
                    Fore.WHITE +
                    Style.NORMAL +
                    "You have to login.\n"
                )
                main()

    else:
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[!] ' +
            Fore.WHITE +
            Style.NORMAL +
            "".join([
                f"'{input_command.split()[0]}' ",
                "command doesn't exist. Type 'help' to see commands.\n"
            ])
        )
        main()

# =====Program Starting=====


os.system('clear')
print(Fore.YELLOW + Style.BRIGHT + cryptosafe_title)
print(
    Fore.BLUE +
    Style.BRIGHT +
    '[i] ' +
    Fore.WHITE +
    Style.NORMAL +
    "Type 'help' to see commands.\n"
)
main()
