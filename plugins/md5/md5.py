import subprocess

def checksum(binary):
    p = subprocess.Popen(["md5sum", binary.get_file()], stdout=subprocess.PIPE)
    output, err = p.communicate()
    return '\nMD5 Sum:\t%s' % output.split(" ")[0]