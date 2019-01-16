import os
from subprocess import Popen, PIPE
import requests
from zipfile import ZipFile
try:
    import urllib2 as urlib
except ImportError:
    import urllib as urlib

#Helper function to download files
def download_file(url, filename, destination, encoding='utf-8'):
    '''downloads a file and extracts it if needed
    url: the url of the file to download (string)
    filename: the filename (string)
    destination: path where to download the file (string)
    encoding: encoding to use when extracting, defaults to utf-8 (string)
    
    returns list with paths of each downloaded/extracted file
    '''
    
    #Check if file exists, download if not
    if not os.path.isfile(destination + '/' + filename):
        print ("Downloading file.")
        #Download with redirect
        urlib.request.urlretrieve(url, filename)
        os.system("mv " + filename + " " + destination)
    else:
        print("File already downloaded.")
    
    #Placeholder for files from container
    files = None
    
    #Get extension   
    file_ext = filename.split('.')[-1]
    if file_ext == 'rar':
        
        #Get files from container
        files = Popen("unrar lb " + destination + "/" + filename, shell=True, stdout=PIPE).stdout.read()
        files = files.decode(encoding).split(sep='\n')[:-1]
        files = [destination + "/" + f.strip() for f in files]
        
        #Extract if needed
        missing = [f for f in files if not (os.path.isfile(f) or os.path.isdir(f))]
        if missing:
            print ("Extracting .{} container.".format(file_ext))
            os.system("unrar x " + destination + "/" + filename + " " + destination)
        else:
            print("File already extracted.")
            
    elif file_ext == 'zip' or file_ext == 'gz':
        
        #Get files from container
        files = Popen("unzip -Z1 " + destination + "/" + filename, shell=True, stdout=PIPE).stdout.read()
        files = files.decode(encoding).split(sep='\n')[:-1]
        files = [destination + "/" + f.strip() for f in files]
        
        #Extract if needed
        missing = [f for f in files if not os.path.isfile(f)]
        if missing:
            print ("Extracting .{} container.".format(file_ext))
            
            ZipFile(destination + "/" + filename).extractall(destination)
            #os.system("unzip " + destination + "/" + filename + " -d " + destination)
        else:
            print("File already extracted.")
            
    else:
        print("Won't extract {} file".format(file_ext))
    
    #Check again and return file path(s)
    if files is None:
        # Check:
        if not os.path.isfile(destination + "/" + filename):
            print ("WARNING! Something is wrong: the file " + filename + " is not there.")
        else:
            print (filename + " in place, you can continue.")
        
        return (destination + "/" + filename)
    else:
        #Check:
        missing = [f for f in files if not (os.path.isfile(f) or os.path.isdir(f))]
        if missing:
            print ("WARNING! Something is wrong: some files are not there.")
            print (missing)
        else:
            print (filename + " contents in place, you can continue.")
            
        return (files)