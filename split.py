import re
import sys
import os
folder = ""
name = ""
fo = open(sys.argv[1], "r")

with open(sys.argv[1]) as f:
  for line in f:
    m = re.search('/([^\/]+)/[^\/]+$', line)
    if m:
      if m.groups(1)[0] != folder:
        fo.close()
        name = str(m.groups(1)[0]) + ".txt"
        fo = open(name, "w")
        fo.write(line)
        folder = m.groups(1)[0]
      else:
        fo.write(line)
