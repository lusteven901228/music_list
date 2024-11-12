# import
from subprocess import Popen, PIPE
from datetime import datetime
import os
# main function
def main():
    # header generate
    header = datetime.strftime(datetime.now(), "# Music List\n###### updated on %Y/%m/%d %H:%M\n")

    # Get __file__ directory
    dir_pth = os.path.dirname(__file__)

    # tree
    output = Popen(["tree", dir_pth, "-P", "*.flac", "--noreport"], stdout=PIPE).communicate()[0].decode("utf-8")
    # print(output.decode("utf-8"))
    output = "\n"+output[output.find('\n')+1:]
    output = output.replace('    ','  ').replace("│   ", "  ").replace("├──", "-").replace("└──", "-").replace("*", r"\*")
    with open("music_list.md", 'w') as f:
        f.write(header)
        f.write(output)
    return 0


# run
if __name__ == "__main__":
    print(main())