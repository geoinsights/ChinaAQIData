Python Library for de- and encoding of WCF-Binary streams
---------------------------------------------------------

Inside of a .Net environment WCF services uses the proprietary WCF-Binary-XML
protocol as described `here <https://blogs.msdn.com/b/drnick/archive/2009/09/11/binary-encoding-part-4.aspx>`_.

Because of the only implementation for decoding and encoding such binary
streams exists in .Net itself (and there mostly with validation and/or
auto correction features), we had decided to write our own python library
according to Microsoft's `Open Specification <http://msdn.microsoft.com/en-us/library/cc219210(v=PROT.10).aspx>`_.

The library has a rudimentary commandline interface for converting XML to
WCF-Binary and vice versa, as well as a plugin for our Burp-Python proxy.

The commandline interface consists of two python scripts:

+------------+------------------------------------+------------------------------+
| Script     | Description                        | Examples                     |
+============+====================================+==============================+
| wcf2xml.py | * converts WCF-Binary to XML       | | ./wcf2xml.py request.bin   |
|            |    * reads from stdin or from file | | ./wcf2xml.py < request.bin |
|            |    * writes to stdout              |                              |
+------------+------------------------------------+------------------------------+
| xml2wcf.py | * converts XML to WCF-Binary       | | ./xml2wcf.py request.xml   |
|            |    * reads from stdin or from file | | ./xml2wcf.py < request.xml |
|            |    * writes to stdout              |                              |
+------------+------------------------------------+------------------------------+

View and edit WCF-Binary-streams with Burp Suite 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of fiddlers advantages are his extensibility and his WCF-Binary plugins.
Sadly, this plugins can only decode and display the binary content as XML text.

Our first choice tool for Webapptests (Burp Suite) has also a plugin feature,
and you could also find plugins for decode (and encode XML back to) WCF-Binary
streams. 

But all WCF-Binary plugins out there are based on the .Net library. 
Therefore you have to use Microsoft Windows, or some Mono constellation. 
Another disadvantage is the validation and auto-correction of such libraries...
not very useful for penetration testing ;-)

That's why we've decided to write a small python library which enables us to decode and encode 
WCF-Binary streams. In combination with our python-to-Burp plugin we can decode, edit and 
encode WCF-Binary streams on the fly.

At the moment you'll need three Burp instances to use all Burp features. 
The first one decodes and encodes the data from/to the client. The 
second one operates on the XML like it was a normal request/response. The third 
one encodes/decodes the data to/from the server.

.. graphviz::
    
    graph strucure {
        rankdir=LR;
        burp_c [shape=box,label="'Client-Burp'\nPort 55666\nWcfPlugin"];
        burp [shape=box,label="'Cleartext-Burp'\nPort 55667",color=green];
        burp_s [shape=box,label="'Server-Burp'\nPort 55668\nWcfPlugin"];
        client -- server [label="normal communication without Burp\n(WCF-Binary)",color=red];
        client -- burp_c [label="WCF-Binary",color=blue];
        burp_c -- burp -- burp_s [label="XML",color=green];
        burp_s -- server [label="WCF-Binary",color=blue];
    }

But we are working on a one-Burp-solution.

After setting up pyBurp, you only have to connect to your current Burp
instance, change the current root directory to the path were pyWCFBin is saved
and load the WcfPlugin::

    $ nc localhost 55666
    cd /home/foo/Downloads/pyWCFBin
    add WcfPlugin
    quit
    $


