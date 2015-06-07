import sys
import os
import re
from subprocess import call

textfiles = sys.argv[1]
readtextfiles = sys.argv[2]
appsrepoPath = os.path.abspath(sys.argv[3])
unpacked = os.path.abspath(sys.argv[4])
manifest = os.path.abspath(sys.argv[5])
code = os.path.abspath(sys.argv[6])
uixml = os.path.abspath(sys.argv[7])

for file in os.listdir(textfiles):
  if (file != ".DS_Store"):
    number = re.search('(.+).txt$', file)
    print file
    number = number.groups(1)[0]
    unpackedSubPath = unpacked + "/" + number + "/"
    manifestPath = manifest + "/" + number + "/"
    codePath = code + "/" + number + "/"
    uixmlPath = uixml + "/" + number + "/"
    if not os.path.exists(unpackedSubPath):
      os.makedirs(unpackedSubPath)
    if not os.path.exists(manifestPath):
      os.makedirs(manifestPath)
    if not os.path.exists(codePath):
      os.makedirs(codePath)
    if not os.path.exists(uixmlPath):
      os.makedirs(uixmlPath)

    path = os.path.join(textfiles, file)

    UnpackCOMMAND = "python " + appsrepoPath + "/tools/apktool_executor.py " + appsrepoPath + " " + unpackedSubPath + " -i " + path
    call(UnpackCOMMAND, shell=True)

    moveCOMMAND = "mv " + textfiles + file + " " + readtextfiles
    call(moveCOMMAND, shell = True)

    ManifestCOMMAND = "python " + appsrepoPath + "/tools/copy_manifest.py " + unpackedSubPath + " " + manifestPath
    call(ManifestCOMMAND, shell=True)

    CodeCOMMAND = "python " + appsrepoPath + "/smali-methods-finder/smali_invoked_methods.py " + unpackedSubPath + "/ " + codePath + "/"
    call(CodeCOMMAND, shell=True)

    uixmlCOMMAND = "python " + appsrepoPath + "/ui-xml/ui_xml.py " + unpackedSubPath + " -o " + uixmlPath
    call(uixmlCOMMAND, shell=True)


