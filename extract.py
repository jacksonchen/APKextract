import sys
import os
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

for root, dirs, files in os.walk(sys.argv[1]):
  if not dirs:
    print "=====No subdirectories====="
    dirPath = os.path.abspath(root)

    UnpackCOMMAND = "python " + appsrepoPath + "/tools/apktool_executor.py " + dirPath + " " + unpackedPath
    call(UnpackCOMMAND, shell=True)

    ManifestCOMMAND = "python " + appsrepoPath + "/tools/copy_manifest.py " + unpackedPath + " " + manifestPath
    call(ManifestCOMMAND, shell=True)

    CodeCOMMAND = "python " + appsrepoPath + "/smali-methods-finder/smali_invoked_methods.py " + unpackedPath + "/ " + codePath + "/"
    call(CodeCOMMAND, shell=True)

    uixmlCOMMAND = "python " + appsrepoPath + "/ui-xml/ui_xml.py " + unpackedPath + " -o " + uixmlPath
    call(uixmlCOMMAND, shell=True)
    break

  else:
    print "=====Multiple subdirectories====="
    for dir in dirs:
      dirPath = os.path.abspath(os.path.join(root, dir))
      unpackedsubPath = os.path.join(unpackedPath, dir)

      if not os.path.exists(unpackedsubPath):
        os.makedirs(unpackedsubPath)

      UnpackCOMMAND = "python " + appsrepoPath + "/tools/apktool_executor.py " + dirPath + " " + unpackedsubPath
      call(UnpackCOMMAND, shell=True)

      ManifestCOMMAND = "python " + appsrepoPath + "/tools/copy_manifest.py " + unpackedsubPath + " " + manifestPath
      call(ManifestCOMMAND, shell=True)

      CodeCOMMAND = "python " + appsrepoPath + "/smali-methods-finder/smali_invoked_methods.py " + unpackedsubPath + "/ " + codePath + "/"
      call(CodeCOMMAND, shell=True)

      uixmlCOMMAND = "python " + appsrepoPath + "/ui-xml/ui_xml.py " + unpackedsubPath + " -o " + uixmlPath
      call(uixmlCOMMAND, shell=True)

    break

