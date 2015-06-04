import sys
import os
import re
from subprocess import call

appsrepo = sys.argv[2]
unpacked = sys.argv[3]
manifest = sys.argv[4]
code = sys.argv[5]
uixml = sys.argv[6]
appsrepoPath = os.path.abspath(appsrepo)
unpackedPath = os.path.abspath(unpacked)
manifestPath = os.path.abspath(manifest)
codePath = os.path.abspath(code)
uixmlPath = os.path.abspath(uixml)

for file in os.listdir(sys.argv[1]):
  m = re.search('(.+).txt$', file)
  unpackedSubPath = unpackedPath + "/" + m.groups(1)[0] + "/"
  if not os.path.exists(unpackedSubPath):
    os.makedirs(unpackedSubPath)

  path = os.path.join(sys.argv[1], file)

  UnpackCOMMAND = "python " + appsrepoPath + "/tools/apktool_executor.py " + appsrepoPath + " " + unpackedSubPath + " -i " + path
  call(UnpackCOMMAND, shell=True)

  ManifestCOMMAND = "python " + appsrepoPath + "/tools/copy_manifest.py " + unpackedSubPath + " " + manifestPath
  call(ManifestCOMMAND, shell=True)

  CodeCOMMAND = "python " + appsrepoPath + "/smali-methods-finder/smali_invoked_methods.py " + unpackedSubPath + "/ " + codePath + "/"
  call(CodeCOMMAND, shell=True)

  uixmlCOMMAND = "python " + appsrepoPath + "/ui-xml/ui_xml.py " + unpackedSubPath + " -o " + uixmlPath
  call(uixmlCOMMAND, shell=True)


