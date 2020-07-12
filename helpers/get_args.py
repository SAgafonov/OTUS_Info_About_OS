import argparse


def get_args():
    """
    Reads script arguments and returns it.
    :return: tuple: path to logs, path to report
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--all_info", required=False, action="store_true", help="Represents: list of files in a "
                                                                                "current directory; "
                                                                                "core version; "
                                                                                "OS version; "
                                                                                "list of all processes")
    parser.add_argument("--proc_info", required=False, help="Represents list of all processes or info "
                                                            "about provided process. "
                                                            "Name of a searching process should be provided."
                                                            "'all' is to show all processes")
    parser.add_argument("--core_version", required=False, action="store_true", help="Represents core version")
    parser.add_argument("--os_version", required=False, action="store_true", help="Represents OS version")
    parser.add_argument("--cur_dir_info", required=False, action="store_true", help="Represents list of files in a "
                                                                                    "current directory")
    parser.add_argument("--dir_info", required=False, nargs='?', help="Represents list of files in a "
                                                                      "provided directory.")
    args = parser.parse_args()
    return args
