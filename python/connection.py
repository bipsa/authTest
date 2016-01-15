import urllib2
import traceback
import json
import sys

def make_request(url, token):
	print 'Requesting the following url ' + url
	request = urllib2.Request(url, None, {"Authorization": "Bearer %s" % token})
	try:
		response = urllib2.urlopen(request)
		response_content = response.read()
		print response_content
	except urllib2.HTTPError, e:
		print 'HTTPError = ' + str(e.code)
		print e.read() 
	except urllib2.URLError, e:
		print 'URLError = ' + str(e.reason)
	except urllib2.HTTPException, e:
		print 'HTTPException'
	except Exception:
		print 'generic exception: ' + traceback.format_exc()

url = raw_input('Please enter the url (Optional): ')
if not url:
	url = 'https://x.jet.com/'

token  = raw_input('Please enter the auth token: ')
if not token:
	token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1uQ19WWmNBVGZNNXBPWWlKSE1iYTlnb0VLWSIsImtpZCI6Ik1uQ19WWmNBVGZNNXBPWWlKSE1iYTlnb0VLWSJ9.eyJhdWQiOiJodHRwczovL3dwLnFhLmpldC5jb20vIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTNmYjAyYzUtM2YzZi00MGRlLTg1NmQtNzMyODU1NWRjZTc5LyIsImlhdCI6MTQ1Mjg3NzYyNywibmJmIjoxNDUyODc3NjI3LCJleHAiOjE0NTI4ODE1MjcsImFjciI6IjEiLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiOGFkMjM1ZDYtOWE5NS00OTIzLWFhODUtYzAxZjAzOGZkMzM2IiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJSb21lcm8iLCJnaXZlbl9uYW1lIjoiU2ViYXN0aWFuIiwiaXBhZGRyIjoiMTkwLjg0LjE3Mi4xOTUiLCJuYW1lIjoiU2ViYXN0aWFuIFJvbWVybyIsIm9pZCI6IjRmZjk3ZjU4LWE5YzgtNDA2OS1iZjk2LTdiYWNjNGM3OGM4MiIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS00MTM3Nzc4MjcyLTU0OTczODg4LTI1NDQxMjIzMjQtMTM2MjEiLCJzY3AiOiJSZWFkX1dyaXRlX2pldHdwdGVzdF9XZWJBUEkgdXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiV0p5Ty1XbHBpbkw1RWs2aW03UkZva2YtdG1KNlVLYVBOd3haOUs5dmNrRSIsInRpZCI6IjkzZmIwMmM1LTNmM2YtNDBkZS04NTZkLTczMjg1NTVkY2U3OSIsInVuaXF1ZV9uYW1lIjoic2ViYXN0aWFuLnJvbWVyb0BqZXQuY29tIiwidXBuIjoic2ViYXN0aWFuLnJvbWVyb0BqZXQuY29tIiwidmVyIjoiMS4wIn0.n70uynD5-Ys8otnTeyhNmHbHJjztMKhza6UvvdItLhSrdrcavpoQVOrtPWip3PP6lPD_v2O4tgDVjH_QryA0wk9AyhlyyrZXuKeBWirCkOq5CKipTUuZ_DVdbtmFzMwORdyk4ShLSODh2aZgmBNuKgnYysiA-XgLRBn3h3HD-CJtFM4D3-b9MaJKX5igKwvsTgCGpXJQer_uLXwVH6JBnXt088zemXyV2ln-FyRDzAtLiakYIQ-s7oaXHarfgjU767fMqq1J_CII3xIE0xOE7iLYPOu0cLDXjP7_rJCjVNVtDYq_826A1oQMrVM5Ctec4_60s2gqQeoa3YkGnl96TQ'
#Making the request
make_request(url, token)




	