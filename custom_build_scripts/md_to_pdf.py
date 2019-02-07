import re, os, glob, pypandoc

def extract_title(mdstring):
    pattern = r"[Tt]itle: (.*)?\n"
    match = re.search(pattern, mdstring)
    try:
        title = match.group(1)
    except:
        title = "(Lesson title not found)"
    return title

def strip_yaml(mdstring):
    return mdstring.partition("\n\n")[-1]

def make_pdf(mdfile):
    with open(mdfile) as mdf:
        md = mdf.read()
    title = extract_title(md)
    md = "# {} \n\n".format(title) + strip_yaml(md)
    outfile = os.path.basename(mdfile).split(".")[0] + ".pdf"
    pypandoc.convert_text(md, 'pdf', format="md", outputfile=outfile)

make_pdf("content/Lessons/abelbaker.md")
