import paramiko
from paramiko import SSHClient
from scp import SCPClient
import sys
import time
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




# Define progress callback that prints the current percentage completed for the file
def progress(filename, size, sent):
    sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )


def upload_to_remote(client: SSHClient, path_to_file, destination):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()

    ssh_client.connect(hostname, username=username,password=password)

    scp = SCPClient(client.get_transport(),progress=progress)
    scp.put(path_to_file, recursive=True,remote_path=destination)

    try:
        stdin, stdout, stderr = ssh_client.exec_command('nohup python test.py > testupload.log &')
        scp.close()
    except Exception as e:
        print(e)

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

    # upload_to_remote(client=ssh_client, path_to_file='/Users/helium/ncsa/scripts/python-ssh/make_text_file.py', destination='/jet/home/pdg/ocean')
    run_python_script()