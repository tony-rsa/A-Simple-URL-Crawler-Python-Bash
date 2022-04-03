from enum import Enum


class hlpmsg(Enum):
    h="HELP\n\tUsage\n\tCommands\n\t\tDescription\n\n\tExamples\n"


help_dict = {
    "-h" : hlpmsg.h,
    "--help": hlpmsg.h
}

def get_help(cmmd, argin):
    iscmmd = cmmd in list(help_dict.keys())
    isargin = argin in list(help_dict.keys())
    keycmd = argin if isargin else cmmd if iscmmd else "-h"
    return help_dict[keycmd]
