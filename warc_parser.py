import sys

'''HELPER FUNCTIONS'''
def process_warc(filename):
    # Output:
    # Format:   {document: [meta_data1, meta_data2, ..., meta_dataN]}
    #           meta_data = {'N', 'b', 'a', 'm', 's', 'k', 'r', 'M', 'V'}
    # Note:
    collection_id = filename.split('-')[1]
    crawl_date = filename.split('-')[2]
    output_file = 'test/warc_headers_' + collection_id + '_' + crawl_date + '.txt'

    with open(output_file, 'w') as headerfile:
        with open(filename, 'rb') as warcfile:
            for line in warcfile:
                if line[:4] == 'WARC':
                    headerfile.write(line[:-2] + '\n')
                    if line[:len('WARC-Record-ID')] == 'WARC-Record-ID':
                        headerfile.write('\n')
    return output_file



'''START SCRIPT'''
def main():
    num_arg = len(sys.argv)
    if num_arg != 2:
        print 'Usage: warc_parser.py file_path'
        return
    warc_file = sys.argv[1]
    process_warc(warc_file)


if __name__ == "__main__":
    main()
