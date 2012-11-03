import urllib
import json
import re

def getcourseurl(phenny, input):

  coursename = input.group().split()[1:]
  if len(coursename) > 2:
    phenny.say(input.nick + ": I don't understand that course name.")
    return

  if coursename

  course = json.loads(urllib.urlopen("http://benwr.net:4567/detail/ece/2504").read())
  urlfmt = "https://banweb.banner.vt.edu/ssb/prod/HZSKVTSC.P_ProcComments?CRN={0}&TERM={1}&YEAR={2}&SUBJ={3}&CRSE={4}"
  url = urlfmt.format(course[0]["crn"],
                      course[0]["term"][4:],
                      course[0]["term"][:4],
                      course[0]["subject"],
                      course[0]["number"])

getcourseurl.commands = ["course"]
getcourseurl.priority = 'medium'
