 if depth == 1:
            #print('Parent: ',path.parent)
            print('Depth: ',depth)
            print('Directory Root')
            #print("Object: {}".format(path.name))
            files_at_root =+ 1
        elif depth == 2:
            print('Depth: ',depth)
            #print("file found at subdir: {}".format(path.name))
            files_at_subdir =+ 1
        elif depth == 3:
            print('Depth: ',depth)
            #print("file found under subdir: {}".format(path.name))
            files_at_othersub =+ 1
        else:
            print('Depth: ',depth)
            files_at_deeper =+ 1
            #print("file under deeper: {}".format(path.name))
