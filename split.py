import re
import sys
import os
folder = ""
counter = 0
name = str(counter) + ".txt"
fo = open(name, "w")

with open(sys.argv[1]) as f:
  for line in f:
    m = re.search('/([^\/]+)/[^\/]+$', line)
    if m:
      if m.groups(1)[0] != folder:
        print counter
        fo.close()
        name = str(counter) + ".txt"
        fo = open(name, "w")
        fo.write(line)
        folder = m.groups(1)[0]
      else:
        fo.write(line)

      counter += 1
