import tuf.interposition
from tuf.interposition import urllib2_tuf as urllib2

mozilla_url = 'http://mirror1.poly.edu/update/3/Firefox/24.0/20130910160258/WINNT_x86-msvc/en-US/release/Windows_NT 6.1.1.0 (x64)/default/default/update.xml?force=1'
not_mozilla_url = 'http://mirror1.poly.edu'

# implicitly assumes that tuf.interposition.json is the present working directory

tuf.interposition.configure()
print(urllib2.urlopen(mozilla_url))
print(urllib2.urlopen(not_mozilla_url))
