#! python3

PASSWORDS = {'email': 'FZ@2213414bc%$sdf',
             'blog': 'fjs&12ACjef@123',
             'luggage': '12345',
             '嗆人': '你這個XXX怎麼可以XXXXX然後又像是XXX一樣XXX',
             'fju統編': '35701598'}

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account]')
    sys.exit()

account = sys.argv[1]

import pyperclip
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

