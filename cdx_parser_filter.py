import csv, sys

'''HELPER FUNCTIONS'''
def read_cdx(filename):
    # Output:   Dictionary of cdx information
    # Format:   {document: [meta_data1, meta_data2, ..., meta_dataN]}
    #           meta_data = {'N', 'b', 'a', 'm', 's', 'k', 'r', 'M', 'V'}
    # Note:     This makes the output a dictionary in which each document
    #           contains a list of meta data dictionaries.
    #           To know how many mementos a document has, return the list
    #           length for that document
    cdx_dict = {}
    fieldnames = ['N', 'b', 'a', 'm', 's', 'k', 'r', 'M', 'V', 'g']
    with open(filename, 'r') as cdxfile:
        try:
            reader = csv.DictReader(cdxfile, fieldnames=fieldnames, delimiter=' ')
            reader.next()   # Skip header information
            for row in reader:
                orig_uri = row['a'] # Name of file being processed
                uri_metadata = {'N': row['N'], 'b': row['b'], 'm': row['m'], \
                                's': row['s'], 'k': row['k'], 'r': row['r'], \
                                'M': row['M'], 'V': row['V'], 'g': row['g']}
                #print doc_name
                #print doc_metadata
                try:
                    cdx_dict[orig_uri].append(uri_metadata)
                except:
                    if orig_uri[:3] != 'dns' and orig_uri != '-':
                        cdx_dict[orig_uri] = []
                        cdx_dict[orig_uri].append(uri_metadata)
        except:
            print('File %s is too large to process' % filename)
        return cdx_dict

'''START SCRIPT'''
def main():
    num_arg = len(sys.argv)
    if num_arg < 2:
        print 'Usage: cdx_parser.py collection_id_1 collection_id_2 ... collection_id_n'
        return
    cdx_collections = sys.argv[1:]
    target_uri = 'http://abcnews.go.com/US/Weather/wireStory?id=7166541'
    for collection in cdx_collections:
        print collection
        cdx_file = 'C:/_Kayla/phd_research/cdx_data/index-' + collection + '.cdx'
        cdx_dict = read_cdx(cdx_file)
        if cdx_dict:
            collection_uris = cdx_dict.keys()
            output_file = 'test/' + collection + '_uri.csv'
            with open(output_file, 'w') as f:
                print('Writing to %s' % output_file)
                f.write('N b a m s k r M V g\n')
                for uri in collection_uris:
                    if uri[:len(target_uri)] == target_uri:
                        for meta_data in cdx_dict[uri]:
                            date = meta_data['b']
                            f.write('%s %s %s %s %s %s %s %s %s %s\n' % \
                            (meta_data['N'], meta_data['b'], uri, \
                            meta_data['m'], meta_data['s'], meta_data['k'], \
                            meta_data['r'], meta_data['M'], meta_data['V'], \
                            meta_data['g']))

if __name__ == "__main__":
    main()
