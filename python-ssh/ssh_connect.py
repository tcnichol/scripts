import paramiko
from paramiko import SSHClient
import sys
hostname = sys.argv[1]
password = sys.argv[2]
username = sys.argv[3]

## https://stackoverflow.com/questions/6203653/how-do-you-execute-multiple-commands-in-a-single-session-in-paramiko-python


def execute_commands(client, commands: [str]):
    """
    Execute multiple commands in succession.

    :param commands: List of unix commands as strings.
    :type commands: List[str]
    """
    responses = []

    for cmd in commands:
        stdin, stdout, stderr = client.exec_command(cmd)
        stdout.channel.recv_exit_status()
        response = stdout.readlines()
        responses.append(response)
        for line in response:
            print(f"INPUT: {cmd} | OUTPUT: {line}")
    return responses

def main():
    print(sys.argv)
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()

    ssh_client.connect(hostname, username=username,password=password)

    stdin, stdout, stderr = ssh_client.exec_command('ls \n cd ocean \n ls')
    print(stdout.read().decode("utf8"))
    stdin, stdout, stderr = ssh_client.exec_command('cd ocean \n ls')
    print(stdout.read().decode("utf8"))
    ssh_client.close()
    print('done')

if __name__ == '__main__':
    main()