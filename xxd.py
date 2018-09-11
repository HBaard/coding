import string

def print_buf(counter, buf):
    buf2 = [('%02x' % ord(i)) for i in buf]
    print '{0}: {1:<39}  {2}'.format(('%07x' % (counter * 16)),
        ' '.join([''.join(buf2[i:i + 2]) for i in range(0, len(buf2), 2)]),
        ''.join([c if c in string.printable[:-5] else '.' for c in buf]))

def fxxd(file_path):
    with open(file_path, 'r') as f:
        xxd(f.read())

def xxd(data):
    chunks = [data[i:i + 16] for i in xrange(0, len(data), 16)]
    for ix,chunk in enumerate(chunks):
        print_buf(ix, chunk)
