import logging
class YamlReaderError(Exception):
    pass

def data_merge(a, b):
    """merges b into a and return merged result

    NOTE: tuples and arbitrary objects are not handled as it is totally ambiguous what should happen"""
    key = None
    log=logging.getLogger('data_merge')
    log.setLevel(logging.INFO)
    logging.basicConfig( level=logging.INFO)

    # ## debug output
    # sys.stderr.write("DEBUG: %s to %s\n" %(b,a))
    try:
        if a is None or isinstance(a, str)  or isinstance(a, int)  or isinstance(a, float):
            # border case for first run or if a is a primitive
            a = b
        elif isinstance(a, list):
            # lists can be only appended
            if isinstance(b, list):
                # merge lists
                for element in b:
                    if element in a:
                        log.warn ('Conflicting elemt is ({})'.format(element))
                        log.info ("ListA ({}) ListB({})".format(a,b))
                a.extend(b) ## Better to report - if duplication found
                
            else:
                # append to list
                a.append(b)
        elif isinstance(a, dict):
            # dicts must be merged
            if isinstance(b, dict):
                for key in b:
                    if key in a:
                        log.info("merging ({}) of key ({}) to ({})".format(b[key], key , a[key]))
                        a[key] = data_merge(a[key], b[key])
                    else:
                        a[key] = b[key]
            else:
                raise YamlReaderError('Cannot merge non-dict ({}) into dict ({})'.format(b, a))
        else:
            raise YamlReaderError('NOT IMPLEMENTED ({}) into ({})'.format(b, a))
    except TypeError as e:
        raise YamlReaderError('TypeError ({}) in key ({}) when merging ({}) into ({})'.format(e, key, b, a))
    return a

# def main():
#     #d1={'a':[1,2,3,4],'b':20,'c':'bb','d':{'a':8,c20}}
#     #logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
# 
#     d1={'a':[1,2,3,4],'b':20,'c':'bb'}
#     d2={'a':[1,2,7,20],'b':30,'c':'bc'}
#     data_merge(d1,d2)
# if __name__ == '__main__':
#     main()
    