import paramiko
from paramiko import SSHClient
from scp import SCPClient
import sys
import time
hostname = sys.argv[1]
password = sys.argv[2]
username = sys.argv[3]

## https://stackoverflow.com/questions/6203653/how-do-you-execute-multiple-commands-in-a-single-session-in-paramiko-python

## https://stackoverflow.com/questions/17560498/running-process-of-remote-ssh-server-in-the-background-using-python-paramiko


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




# Define progress callback that prints the current percentage completed for the file
def progress(filename, size, sent):
    sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )


def upload_to_remote(client: SSHClient, path_to_file, destination):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()

    ssh_client.connect(hostname, username=username,password=password)

    scp = SCPClient(client.get_transport(),progress=progress)
    scp.put(path_to_file, recursive=True,remote_path=destination)
    scp.close()

def copy_python_script_and_run(client: SSHClient, path_to_script, destination):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()

    ssh_client.connect(hostname, username=username, password=password)

    scp = SCPClient(ssh_client.get_transport(), progress=progress)
    scp.put(path_to_script, recursive=True, remote_path=destination)

    try:
        stdin, stdout, stderr = ssh_client.exec_command('python test.py', get_pty=True)
        time.sleep(50)
        scp.close()
    except Exception as e:
        print(e)


def run_python_script():
    print(sys.argv)
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()

    ssh_client.connect(hostname, username=username, password=password)

    stdin, stdout, stderr = ssh_client.exec_command('cd ocean \n python /jet/home/pdg/ocean/make_text_file.py')
    print(stdout.read().decode("utf8"))
    ssh_client.close()
    print('done')

def run_nohup():
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()

    ssh_client.connect(hostname, username=username, password=password)

    channel = ssh_client.get_transport().open_session()
    pty = channel.get_pty()
    shell = ssh_client.invoke_shell()
    try:
        shell.send("cd ocean \n nohup python test1.py > test1.log &\n")
    except Exception as e:
        print(e)

    print('after')



def nohup1():
    client = paramiko.SSHClient()
    client.connect(hostname, username=username, password=password, timeout=5)
    transport = client.get_transport()
    channel = transport.open_session()
    channel.exec_command('cd ocean \n python test.py > testlog1.log &')

def nohup2():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password =password)
    channel = ssh.get_transport().open_session()
    pty = channel.get_pty()
    shell = ssh.invoke_shell()
    shell.send("cd /ocean \n nohup python test2.py > test2.log &\n")

def main():
    print(sys.argv)
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()

    ssh_client.connect(hostname, username=username,password=password)

    stdin, stdout, stderr = ssh_client.exec_command('ls \n cd ocean \n ls')
    print(stdout.read().decode("utf8"))
    result = execute_commands(client=ssh_client, commands=['ls', 'cd ocean', 'ls'])
    stdin, stdout, stderr = ssh_client.exec_command('cd ocean \n ls')
    print(stdout.read().decode("utf8"))
    ssh_client.close()
    print('done')

if __name__ == '__main__':
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()

    # copy_python_script_and_run(client=ssh_client, path_to_script='/Users/helium/ncsa/scripts/python-ssh/test.py', destination='/jet/home/pdg/ocean')

    ssh_client.connect(hostname, username=username,password=password)

    upload_to_remote(client=ssh_client, path_to_file='/Users/helium/ncsa/scripts/python-ssh/test1.py', destination='/jet/home/pdg/ocean')
    upload_to_remote(client=ssh_client, path_to_file='/Users/helium/ncsa/scripts/python-ssh/test2.py', destination='/jet/home/pdg/ocean')
    upload_to_remote(client=ssh_client, path_to_file='/Users/helium/ncsa/scripts/python-ssh/test3.py', destination='/jet/home/pdg/ocean')

    try:
        run_nohup()
    except Exception as e:
        print(e)


    # run_nohup()
    #
    # try:
    #     nohup1()
    # except Exception as e:
    #     print(e)
    #
    # try:
    #     nohup2()
    # except Exception as e:
    #     print(e)
    #
    # print('done')
    # # upload_to_remote(client=ssh_client, path_to_file='/Users/helium/ncsa/scripts/python-ssh/test.py', destination='/jet/home/pdg/ocean')
    # run_nohup()
    # # run_python_script()