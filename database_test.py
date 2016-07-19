
from FoRREST import FoRREST
from FoRREST.plugins.extract.Model import Extract_Model
from playhouse.shortcuts import model_to_dict

# If you call forrest.py, run this.
if __name__ == '__main__':
    forrest = FoRREST('test_binaries/crackme0x00a')

    # forrest.add_entry()

    file_obj = forrest.select()

    if file_obj:
        for model in file_obj:
            print ""
            print "FoRREST:"
            print "----------"
            print model_to_dict(model)

            print ""
            print "Raw:"
            print "----------"
            print forrest.raw.select(model).__dict__

            print ""
            print "Extract:"
            print "----------"
            print forrest.extract.select(model).__dict__

    else:
        print "Select returned empty!"
