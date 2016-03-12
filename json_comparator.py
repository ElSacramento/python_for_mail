
# coding: utf-8

# In[24]:

import json
error_list = list()


# In[17]:

def comparator(ethalon_path, json_file_path):
    ethalon = open(ethalon_path)
    json_file = open(json_file_path)

    try:
        json_data = json.load(json_file)
    except ValueError:
        raise Exception("json isn't valid")
    try:
        ethalon_data = json.load(ethalon)
    except ValueError:
        raise Exception("ethalon isn't valid")
    
    if json_data != ethalon_data:
        compare_json(ethalon_data,json_data, 1)
    
    #raise list with all exceptions
    if len(error_list):
        raise Exception("\n"+"\n".join([str(e) for e in error_list]))


# In[18]:

def compare_dicts(first, second, ethalon_id, keyname):
    if len(first) < len(second):
        first, second = second, first
        #to control where is ethalon
        ethalon_id = 2 if (ethalon_id == 1) else 1
    
    #check if second have first items
    for item1 in first.items():
        if (item1[0] in second.keys()):
            item2 = (item1[0], second[item1[0]])
            compare_json(item1,item2,ethalon_id, keyname)
        else:
            if ethalon_id == 1:
                #if ethalon is first, item1 isn't in json   
                error_list.append(Exception("can't find key " + keyname + '-' + item1[0]))
                #json can include another item
                if (len(first) == len(second)):
                    for item in second.items():
                        if item[0] not in first.keys():
                            error_list.append(Exception("extra key " + keyname + '-' + item[0]))
            else:
                #if ethalon is second, item1 is extra
                error_list.append(Exception("extra key " + keyname + '-' + item1[0]))


# In[19]:

def compare_lists(first, second, ethalon_id, keyname):
    if len(first) < len(second):
        first, second = second, first
        #to control where is ethalon
        ethalon_id = 2 if (ethalon_id == 1) else 1
        
    #counter for blocks in list    
    i = 0
    #compare lists items
    for item1, item2 in zip(first,second): 
        compare_json(item1,item2, ethalon_id, keyname + '(block number ' + str(i + 1) + ')')
        i += 1
    #counter for blocks in list
    index = len(second) 
    #check if there is extra blocks 
    while index < len(first):
        if ethalon_id == 1:
            #if ethalon is first, json haven't this block
            error_list.append(Exception("can't find block number " + str(index + 1) + ' in list with key ' + keyname))
        else:
            #if ethalon is second, this block is extra
            error_list.append(Exception("extra block number " + str(index + 1) + ' in list with key ' + keyname))
        index += 1


# In[20]:

def compare_tuples(first, second, ethalon_id, keyname):
    if type(first[1]) == type(list()):
        keyname += '-' + first[0]
        compare_json(first[1], second[1], ethalon_id, keyname)
    else:
        if type(first[1]) == type(dict()):
            keyname += '-' + first[0]                    
            compare_json(first[1], second[1], ethalon_id, keyname)
        else: 
            if type(first[1]) != type(second[1]):
                error_list.append(Exception("wrong type of value on key " + keyname + '-' + first[0]))
            else: 
                if first[1] != second[1]:
                    error_list.append(Exception("wrong value on key " + keyname + '-' + first[0]))


# In[21]:

def compare_json(first,second, ethalon_id, keyname = ""):
    #keyname is path to error
    if type(first) == type(second):
        
        if type(first) == type(dict()):
            compare_dicts(first, second, ethalon_id, keyname)
        
        if type(first) == type(list()):
            compare_lists(first,second,ethalon_id,keyname)
        
        if type(first) == type(tuple()):
            compare_tuples(first,second,ethalon_id,keyname)
    
    else:
        error_list.append(Exception("wrong type of value on key " + keyname))


# In[25]:

import sys
import argparse


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(description='Write paths to json files.')
	parser.add_argument('ethalon', metavar='path_to_ethalon', type=str,
                   help='ethalon for comparator')
	parser.add_argument('json', metavar='path_to_json', type=str,
                   help='json for comparator')

	args = parser.parse_args()

	comparator(args.ethalon, args.json)
    



