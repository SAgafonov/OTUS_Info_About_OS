import os
import platform
import subprocess


def get_os_version() -> str:
    """
    Return info about OS
    :return: str
    """
    return f"{os.name} {platform.system()} {platform.release()}"


def get_core_version() -> str:
    """
    Return info about core
    :return: str
    """
    uname = platform.uname()
    return f"{uname.system} {uname.release} {uname.version} {uname.machine} {uname.processor}"


def get_dir_info(path=".") -> dict:
    """
    Represent files in a provided directory.
    Current directory by default
    :param path: str: path to a dir
    :return: dict: list of files and dirs
    """
    dirs = []
    files = []
    with os.scandir(path=path) as item:
        for entry in item:
            if entry.is_file():
                files.append(entry.name)
            else:
                dirs.append(entry.name)
    res = {"dirs": dirs, "files": files}
    return res


def get_proc_info(proc_name: str = None) -> str:
    """
    Return info either about all processes or provided process
    :param proc_name: str
    :return: str
    """
    proc1 = subprocess.Popen(["ps", "-aux"], stdout=subprocess.PIPE)
    if proc_name:
        proc2 = subprocess.Popen(["grep", proc_name], stdin=proc1.stdout, stdout=subprocess.PIPE)
        proc1.stdout.close()
        res = proc2.communicate()
    else:
        res = proc1.communicate()
    return res[0].decode()
