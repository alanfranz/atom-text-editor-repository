#!/usr/bin/python2.7 -u
# dependencies: feedparser, requests
# this is quite sketchy, no unit tests, etc, but does the work.

import feedparser
import pickle
from os.path import expanduser, join, sep, dirname, realpath, basename
import sys
import tempfile
import urllib
import re
import time
import shutil
import requests
from hashlib import md5

WHAT="atom-stable"

VALID_VERSION = re.compile("^\d+\.\d+\.\d+$")
IGNORE_RELEASES = re.compile(".*beta.*")

statefilename = join(dirname(realpath(__file__)), "state-{0}.pickle".format(WHAT))
try:
    state = pickle.load(open(statefilename))
except IOError:
    state = set()

d = feedparser.parse('https://github.com/atom/atom/releases.atom')
# we check the latest 5 non-ignored releases only.
latest_valid_releases = [entry.title.strip() for entry in d.entries if not IGNORE_RELEASES.match(entry.title.strip())][0:5]
for release in latest_valid_releases:
    if release in state:
        print "latest release is already ok, doing nothing. We already know about " + " ".join(latest_valid_releases)
        sys.exit(0)
    if not VALID_VERSION.match(release):
        print "Invalid release: '{0}'".format(release)
        sys.exit(1)
    break
else:
    print "found no unknown release, doing nothing. We already know about " + " ".join(latest_valid_releases)
    sys.exit(0)


print "downloading new release %s" % release

deb_url = "https://github.com/atom/atom/releases/download/v%s/atom-amd64.deb" % release
deb_filename="atom_{0}_amd64.deb".format(release)

print "retrieving remote deb file"
deb_response = requests.get(deb_url)
deb_response.raise_for_status()
print "retrieved deb with md5 %s" % (md5(deb_response.content).hexdigest())

rpm_url = "https://github.com/atom/atom/releases/download/v%s/atom.x86_64.rpm" % release
rpm_filename="atom-{0}.x86_64.rpm".format(release)

print "retrieving remote rpm file"
rpm_response = requests.get(rpm_url)
rpm_response.raise_for_status()
print "retrieved rpm with md5 %s" % (md5(rpm_response.content).hexdigest())

with open(deb_filename, "w") as f:
    f.write(deb_response.content)

with open(rpm_filename, "w") as f:
    f.write(rpm_response.content)

state.add(release)
pickle.dump(state, open(statefilename, "w"))
print "added release %s" % release
