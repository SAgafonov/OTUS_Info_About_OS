# OTUS_Info_About_OS
Get info about system.
The following information may be represented as a result:
- information about specific process;
- information about all processes;
- information about core;
- information about OS;
- list of FILEs in a directory;

## Run
To see all the available information (list of FILEs in a current directory will be provided)
```bash
python3 get_sys_info.py --all_information
```

To see some specific information
```bash
python3 get_sys_info.py [OPTION]

Available OPTIONS
    --proc_info=<VALUE>   Represents list of all processes or info about provided process. 
                          Name of a searching process should be provided.
                          Use 'all' to show all processes
    --core_version        Represents core version
    --os_version          Represents OS version
    --cur_dir_info        Represents list of files in a current directory
    --dir_info=<VALUE>    Represents list of files in a provided directory.
```

Example of usage:
```bash
python3 get_sys_info.py --core_version --os_version --dir_info=/home
```
