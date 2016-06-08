import subprocess

def checksum(binary):
    p = subprocess.Popen(["sha1sum", binary.get_file()], stdout=subprocess.PIPE)
    output, err = p.communicate()
    return "\nSHA1 Sum:\t%s" % output.split(" ")[0]