import pexpect

# https://pexpect.readthedocs.io/en/stable/api/pxssh.html

from pexpect import pxssh
import getpass
import sys
hostname = sys.argv[1]
password = sys.argv[2]
username = sys.argv[3]


s = pxssh.pxssh()

s.login(hostname, username, password)
s.sendline('uptime')
s.prompt()
print(s.before)
s.sendline('ls')
s.prompt()
print(s.before)
s.sendline('cd ocean')
s.prompt()
print(s.before)
s.sendline('ls')
s.prompt()
print(s.before)
s.logout()