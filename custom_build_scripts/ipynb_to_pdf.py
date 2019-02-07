import nbformat, nbconvert, warnings, re, os, glob
warnings.filterwarnings("ignore")

def extract_title_ipynb(cell0):
    source = cell0["source"]
    pattern = r"[Tt]itle: (.*)?\n"
    match = re.search(pattern, source)
    try:
        title = match.group(1)
    except:
        title = "(Lesson title not found)"
    newcell = {'cell_type': 'markdown', 'metadata': {}, 'source': '# {}'.format(title)}
    return nbformat.from_dict(newcell)

def nameclean(notebook_file):
    basename = os.path.basename(notebook_file)
    pdffile = basename.split(".")[0] + ".pdf"
    oldsource1 = "\n<hr>\n[Download this lesson in PDF]({attach}../images/" + pdffile + ")\n<hr>"
    oldsource2 = "\n<hr>\n[Download this lesson in PDF]({attach}../images/" + pdffile + ") [Download Jupyter Notebook file]({attach}../images/" + basename + ")\n<hr>"
    source = "\n<hr>\n[Download this lesson in PDF]({attach}../images/" + pdffile + ") [Download Jupyter Notebook file]({static}" + basename + ")\n<hr>"
    return oldsource1, oldsource2, source


def add_link_to_pdf_ipynb(notebook_file):
    nb = nbformat.read(notebook_file, 4)
    _, _, source = nameclean(notebook_file)
    if nb.cells[-1]["source"] != source:
        newcell = nbformat.from_dict({'cell_type': 'markdown', 'metadata': {}, 'source': source})
        nb.cells.append(newcell)
        nbformat.write(nb, notebook_file)

def remove_pdf_link_ipynb(notebook_file):
    nb = nbformat.read(notebook_file, 4)
    oldsource1, oldsource2, source = nameclean(notebook_file)
    while nb.cells[-1]["source"] in [source, oldsource1, oldsource2]:
        nb.cells.pop()
        nbformat.write(nb, notebook_file)

def make_pdf_from_ipynb(notebook_file):
    remove_pdf_link_ipynb(notebook_file)
    exporter = nbconvert.PDFExporter()
    nb = nbformat.read(notebook_file, 4)
    firstcell = nb["cells"][0]
    nb["cells"][0] = extract_title_ipynb(nb["cells"][0])
    pdf, resources = exporter.from_notebook_node(nb)
    outfile = "content/images/" + os.path.basename(notebook_file).split(".")[0] + ".pdf"
    with open(outfile, "wb") as tp:
        tp.write(pdf)
    add_link_to_pdf_ipynb(notebook_file)

if __name__ == "__main__":
    notebooks = glob.glob("content/Lessons/*.ipynb")
    for notebook in notebooks:
        make_pdf_from_ipynb(notebook)

