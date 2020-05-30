
def usage(type='short'):
    if type == 'short':
        _usage_short()
    elif type == 'long':
        _usage_long()
    elif type == 'retrieve':
        _usage_retrieve()
    else:
        _usage_short()


def _usage_short():
    print(
        "usage: sql-reporter [--help] [-c <path>] <command> [<args>]"
    )


def _usage_long():
    _usage_short()
    print(
        "\n"
        "These are sql-reporter commands used in various usage:\n"
        "\n"
        "all        Execute all commands (retrieve, compress)\n"
        "retrieve   Get results of queries from gateway and make xlsx files\n"
        "compress   Compress all directories to zip format under tmp directory\n"
        "help       Show detail of usage\n"
    )


def _usage_retrieve():
    _usage_short()
    print(
        "\n"
        "retrieve command:\n"
        "usage: sql-reporter retrieve (all, [sql file name])\n"
    )
