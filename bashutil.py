import subprocess

def Start(command, timeout=None):
    """
    Run a Bash command.

    Args:
        command (str): The Bash command to execute.
        timeout (int): Maximum time to wait for the command to complete (in seconds). Set to None for no timeout.

    Example:
        Start("ls -l", timeout=10)
    """
    try:
        subprocess.run(command, shell=True, timeout=timeout, check=True)
    except subprocess.CalledProcessError as e:
        raise e
