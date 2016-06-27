#!/usr/bin/python

from plugins import *
import subprocess
import os


class Idamous:

    def __init__(self):
        """
            Description:
                This sets up the class.

            Returns:
                None
        """
        # Change to not being hardcoded later
        self.operating_system = 'linux'
        self.current_file = None
        self.raw = raw.File.File(self)
        self.extract = extract.Extract.Extract(self)
        self.interpret = interpret.Interpret.Interpret(self)

    def set_file(self, params):
        """
            Description:
                Sets the file to be used.

            Args:
                str - The name of the file.
                [str] - The name of the file (first element of list).

            Example:
                binaries/mybin.out

            Returns:
                None
        """
        if type(params) == str:
            filename = params
        else:
            filename = params[0]

        if (os.path.isfile(filename)):
            self.current_file = filename
        else:
            print "[-] That file does not exist!"


    def get_file(self, params=None):
        """
            Description:
                Gets the filename and path of the current file. Returns
                None if no file.

            Returns:
                str? - The name and filepath of the file.
        """
        return self.current_file

    def get_raw_data(self, params=None):
        """
            Description:
                Gets a dictionary of all of the raw metadata.

            Returns:
                dict(str : (int | str)) - {
                    'name': str,
                    'extension': str,
                    'size': int,
                    'md5': str,
                    'sha1': str,
                    'sha256': str
                }
        """
        output = {}

        if self.current_file:
            output['name'] = self.raw.get_name()
            output['extension'] = self.raw.get_extension()
            output['size'] = self.raw.get_size()
            output['md5'] = self.raw.get_md5()
            output['sha1'] = self.raw.get_sha1()
            output['sha256'] = self.raw.get_sha256()
        else:
            print "No file selected! Please select with",\
                "load [filename]"

        return output

    def get_extracted_data(self, params=None):
        """
            Description:
                Gets a dictionary of all of the extracted data.

            Returns:
                dict(str : (list | str)) - {
                    'type': str,
                    'version': str,
                    'architecture': int,
                    'compiler': str,
                    'sections': list
                }
        """
        output = {}

        if self.current_file:
            output['type'] = self.extract.get_filetype()
            output['version'] = self.extract.get_version()
            output['architecture'] = self.extract.get_architecture()
            output['compiler'] = self.extract.get_compiler()
            output['sections'] = self.extract.get_sections()
        else:
            print "No file selected! Please select with",\
                "load [filename]"

        return output

    def get_interpreted_data(self, params=None):
        """
            Description:
                Gets a dictionary of all of the raw metadata.

            Returns:
                dict(str : int) - {
                    'opcodes': list,
                    'strings': list,
                    'imports': list,
                    'exports': list,
                    'header_information': list,
                }
        """
        output = {}

        if self.current_file:
            output['opcodes'] = self.interpret.get_opcodes()
            output['strings'] = self.interpret.get_strings()
            output['imports'] = self.interpret.get_imports()
            output['exports'] = self.interpret.get_exports()
            output['header_info'] = self.interpret.get_header_information()
        else:
            print "No file selected! Please select with",\
                "load [filename]"

        return output

    def get_help(self, params=None):
        """
            Description:
                Prints to std a message of help that is read in from help.txt.

            Returns:
                None
        """
        with open('help.txt', 'r') as f:
            print f.read()

    def _shell(self, commandName, args, stdin=None):
        """
            Description:
                Make a call to the terminal and return the output.

            Returns:
                list - The output from the call split by line.
        """
        cmd = [commandName]
        if type(args) == str:
            cmd.append(args)
        else:
            cmd.extend(args)

        print 'running', cmd

        if stdin:
            out, err = subprocess.Popen(
                cmd,
                stdin=stdin,
                stdout=subprocess.PIPE
            ).communicate()
        else:
            out, err = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE
            ).communicate()

        if out:
            out = out.splitlines()
        if err:
            err = err.splitlines()

        return out, err

    def _shell_std(self, commandName, args, stdin=None):
        """
            Description:
                Make a call to the terminal and return the output.

            Returns:
                stdout - The stdout pipe.
        """
        cmd = [commandName]
        if type(args) == str:
            cmd.append(args)
        else:
            cmd.extend(args)

        print 'running', cmd

        if stdin:
            out = subprocess.Popen(cmd, stdin=stdin, stdout=subprocess.PIPE)
        else:
            out = subprocess.Popen(cmd, stdout=subprocess.PIPE)

        return out.stdout
