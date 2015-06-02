import sys
import os
from subprocess import call
appsrepo = sys.argv[2]
targetDir = sys.argv[3]

for root, dirs, files in os.walk(sys.argv[1]):
  if not dirs:
    dirPath = os.path.abspath(root)
    appsrepoPath = os.path.abspath(appsrepo)
    targetDirPath = os.path.abspath(targetDir)
    UnpackCOMMAND = "python " + appsrepoPath + "/tools/apktool_executor.py " + dirPath + " " + targetDirPath
    print UnpackCOMMAND
    call(UnpackCOMMAND, shell=True)
  else:
    for dir in dirs:
      dirPath = os.path.join(root, dir)
      UnpackCOMMAND = "python " + appsrepo + "/tools/apktool_executor.py " + dirPath + " " + targetDir
      call(UnpackCOMMAND, shell=True)
