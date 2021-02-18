from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.util import readfile
from cloudmesh.common.util import writefile
from cloudmesh.common.util import path_expand
from pathlib import Path


class MarkdownCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_markdown(self, args, arguments):
        """
        ::

          Usage:
                markdown numbers [-i] FILE
                markdown meta [-i] FILE

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -i     in place replacements. Overwrites the existing file
        """

        def remove_number(line):
            line = line.strip()
            pos = 0
            for pos in range(0, len(line)):
                if line[pos].isdigit() or line[pos] == ".":
                    pass
                else: break
            line = line[pos:].strip()
            return line


        if arguments.numbers:
            arguments.FILE = Path(arguments.FILE).resolve()

            lines = readfile(arguments.FILE).splitlines()
            result = []

            s, ss, sss, ssss= 0, 0, 0, 0

            for line in lines:
                if line.startswith("## "):
                    s = s + 1
                    ss, sss, ssss = 0, 0, 0
                    line = line.replace("## ", "")
                    line = remove_number(line)
                    result.append(f"## {s}. {line}")
                elif line.startswith("### "):
                    ss = ss + 1
                    sss, ssss= 0, 0
                    line = line.replace("### ", "")
                    line = remove_number(line)
                    result.append(f"### {s}.{ss} {line}")

                elif line.startswith("#### "):
                    sss = sss + 1
                    ssss = 0
                    line = line.replace("#### ", "")
                    line = remove_number(line)
                    result.append(f"#### {s}.{ss}.{sss} {line}")

                elif line.startswith("##### "):
                    ssss = ssss + 1
                    line = line.replace("##### ", "")
                    line = remove_number(line)
                    result.append(f"##### {s}.{ss}.{sss} {line}")
                else:
                    result.append(line)

                print ("\n".join(result))

        elif arguments.list:
            print(f"generate metadata for {arguments.FILE} ...")

        return ""
