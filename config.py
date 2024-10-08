from configparser import ConfigParser
def config(filename="database.ini",section="postgresql"):
    #create parser
    parser=ConfigParser()
    parser.read(filename)   #Read config file
    db={}
    if parser.has_section(section):
        params=parser.items(section)
        for param in params:
            db[param[0]]=param[1]
    else:
        raise Exception('Section{0} is not found in in {1} file'.format(section,filename))
    return(db)  #returns the credentials
