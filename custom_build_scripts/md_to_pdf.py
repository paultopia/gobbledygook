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

def make_link_text(mdfile):
    retstring = "\n\n[Download lesson PDF]({attach}../images/"
    filename = os.path.basename(mdfile).split(".")[0] + ".pdf"
    endstring = ")\n\n"
    return retstring + filename + endstring

def add_link_text(mdfile, mdstring):
    linktext = make_link_text(mdfile)
    if not mdstring.endswith(linktext):
        outstring = mdstring + linktext
        with open(mdfile, "w") as mdf:
            mdf.write(outstring)

def remove_link_text(mdfile, mdstring):
    linktext = make_link_text(mdfile)
    if mdstring.endswith(linktext):
        outstring = mdstring.split(linktext)[0]
        return outstring
    return mdstring

def make_pdf_from_md(mdfile):
    with open(mdfile) as mdf:
        mdstring = mdf.read()
    original = mdstring
    title = extract_title(mdstring)
    mdstring = "# {} \n\n".format(title) + strip_yaml(mdstring)
    mdstring = remove_link_text(mdfile, mdstring)
    outfile = "content/images/" + os.path.basename(mdfile).split(".")[0] + ".pdf"
    pypandoc.convert_text(mdstring, 'pdf', format="md", outputfile=outfile)
    add_link_text(mdfile, original)


if __name__ == "__main__":
    notebooks = glob.glob("content/Lessons/*.md")
    for notebook in notebooks:
        make_pdf_from_md(notebook)

