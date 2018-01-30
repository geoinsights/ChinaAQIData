# vim: set ts=4 sw=4 tw=79 fileencoding=utf-8:
from __future__ import absolute_import
from io import BytesIO, StringIO
import array

from bluec0re import ICallback

from wcf.records import Record, print_records, dump_records
from wcf.xml2records import XMLParser


def encode_decode(headers, data):

    if not data:
        return headers, data


    if 'X-WCF-Encode' in headers:
        data = dump_records(XMLParser.parse(data))
        del headers['X-WCF-Encode']
        headers['Content-Type'] = 'application/soap+msbin1'
        headers['Content-Length'] = str(len(data))
    else:
        #print headers['Content-type']
        if 'Content-Type' not in headers or headers['Content-Type'] != 'application/soap+msbin1':
            return headers, data
        #print headers
        fp = BytesIO(data)
        data = Record.parse(fp)
        fp.close()
        fp = StringIO()
        print_records(data, fp=fp)
        data = fp.getvalue()
        fp.close()
        headers['X-WCF-Encode'] = '1'
        headers['Content-Type'] = 'text/soap+xml'
        headers['Content-Length'] = str(len(data))
    return headers, data

class WcfPlugin(ICallback):

    def __str__(self):
        return type(self).__name__

    def processProxyMessage(self, *args, **kwargs):
        messageIsRequest = args[1]
        message = args[10]
       
        message = message.tostring()
        i = message.find('\x0d\x0a\x0d\x0a')
        header = message[:i]
        lines = header.split('\x0d\x0a')
        data = message[i+4:]

        headers = {}
        for i in range(1, len(lines)):
            n,v = lines[i].split(': ')
            headers[n.strip()] = v.strip()

        headers, data = encode_decode(headers,data)

        header = "%s\r\n" % lines[0]
        for n,v in headers.iteritems():
            header += '%s: %s\r\n' % (n,v)
        header += '\r\n'
        return array.array('b', header+data)

