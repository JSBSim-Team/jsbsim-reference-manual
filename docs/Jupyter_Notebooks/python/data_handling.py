import os, errno, fnmatch, csv

import tailer #pip install tailer
import lxml.etree as etree
from itertools import chain

#----------------------------------------------------------
# Show full text file with or without line numbers.
# 
# Default shows line numbers
# Text is aligned up to 9999 lines of code

def show_file(fname,num_lines=1):
    file = open(fname, 'r')
    if num_lines==1:
        i=1
        for line in file:
            print('{0:4d}'.format(i) + '| ' + line, end='')
            i+=1
    else:
        print(line, end='')

        
#----------------------------------------------------------
# Show text file first and last part
#

def show_file_contents(fname, head=0, tail=0):
    for line in tailer.head(open(fname), head):
        print(line)
    print('\t...')
    print('\t...')
    for line in tailer.tail(open(fname), tail):
        print(line)
        
        
#----------------------------------------------------------
# Create directory
# 

def mkdir_p(path):
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

#----------------------------------------------------------
# Move files from/to folder, with update check
#   example: move_files_to_folder('*.csv', './pippo')
#

def move_files_to_folder(expr, to_folder, from_folder='.', clean_destination_first=False):
    # create a folder, if not present
    mkdir_p(to_folder)
    
    # first clean
    if clean_destination_first:
        for e in os.listdir(to_folder):
            if os.path.isfile('{0}/{1}'.format(to_folder,e)):
                os.remove('{0}/{1}'.format(to_folder,e)) 
    
    # then move
    for e in os.listdir(from_folder):
        if os.path.isfile('{0}/{1}'.format(from_folder,e)):
            if fnmatch.fnmatch(e, expr):
                if os.path.isfile('{0}/{1}'.format(to_folder,e)):
                    # first clean matched/pre-existing files                    
                    os.remove('{0}/{1}'.format(to_folder,e)) 
                os.rename('{0}/{1}'.format(from_folder,e),'{0}/{1}'.format(to_folder,e))


#----------------------------------------------------------
# http://lxml.de/tutorial.html
def pretty_print_from_file(fname, nodename):
    tree = etree.parse(fname)
    xmlstring0 = etree.tostring(tree.find(nodename), xml_declaration=False, pretty_print=True, encoding="unicode")
    xmlstring1 = re.sub('\\sxmlns:xsi="[^"]+"', '', xmlstring0, count=1)
    xmlstring = re.sub(r'^\s*$', '', xmlstring1)
    
    print('')
    #print(xmlstring)
    print('\n'.join([line for line in xmlstring.split('\n') if line.strip()]))
    print('')
    
    
#----------------------------------------------------------
# CSV - Dictionary conversion
# CSV has keys as headers and values in columns
# 
def dict_to_csv_col(dictionary, path):
    keys = sorted(dictionary.keys())
    with open(path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(keys)
        writer.writerows(zip(*[dictionary[key] for key in keys]))

def csv_col_to_dict(path):
    dictionary = { }
    csv_data = open(path,'r')
    data = list(csv.reader(csv_data))
    dictionary = dict(zip(data[0],map(list,zip(*data[1:]))))
    for key in dictionary.keys(): 
        dictionary[key] = [float(i) for i in dictionary[key]]
    return dictionary


#----------------------------------------------------------
# Search in list for closest value to assigned one
# Returns both index and value
# 

def takeClosest(myList, myNumber):
    
    from bisect import bisect_left
    
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return pos, myList[0]
    if pos == len(myList):
        return pos, myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return pos, after
    else:
        return pos, before