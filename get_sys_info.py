from helpers.get_args import get_args
from helpers import get_data

if __name__ == "__main__":
    cmd_data = vars(get_args())
    if cmd_data["all_info"]:
        print("=" * 40, " System info ", "=" * 40)
        print("OS:", get_data.get_os_version(), end="\n\n")
        print("Core:", get_data.get_core_version(), end="\n\n")
        print("Information about the FILEs in '.':\n", get_data.get_dir_info(), sep="", end="\n\n")
        print("Information about all processes:\n", get_data.get_proc_info(), sep="")
        exit(0)
    if cmd_data["proc_info"] == "all":
        print("Information about all processes:\n", get_data.get_proc_info(), sep="")
    elif cmd_data["proc_info"] is not None:
        print("Information about process {}:\n".format(cmd_data["proc_info"]),
              get_data.get_proc_info(cmd_data["proc_info"]), sep="")
    if cmd_data["core_version"]:
        print("Core:", get_data.get_core_version(), end="\n\n")
    if cmd_data["os_version"]:
        print("OS:", get_data.get_os_version(), end="\n\n")
    if cmd_data["cur_dir_info"]:
        print("Information about the FILEs in . :\n", get_data.get_dir_info(), sep="", end="\n\n")
    if cmd_data["dir_info"]:
        print("Information about the FILEs in .:\n", get_data.get_dir_info(cmd_data["dir_info"]), sep="", end="\n")
