import subprocess

def main():
    print 'main method.'

def test():
    print 'elf test good.'

def other():
    print 'other test.'

def read_header(binary):
    # Got it working with Popen
    p = subprocess.Popen(["readelf", "-h", binary.get_file()], stdout=subprocess.PIPE)
    output, err = p.communicate()
    return output