import subprocess, os, glob

def get_changes(extension):
    startdir = os.getcwd()
    os.chdir("content/Lessons")
    changes = subprocess.getoutput("changes " + extension).split("\n")
    os.chdir(startdir)
    return changes

def paths_to_tweak(extension):
    out = []
    changed_files = get_changes(extension)
    paths = glob.glob("content/Lessons/*." + extension)
    for path in paths:
        base = os.path.basename(path)
        if base in changed_files:
            out.append(path)
    return out

print(paths_to_tweak("md"))
