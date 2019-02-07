import nbformat, nbconvert, warnings, re, os, glob
warnings.filterwarnings("ignore")

def extract_title_ipynb(cell0):
    source = cell0["source"]
    pattern = r"Title: (.*)?\n"
    match = re.search(pattern, source)
    title = match.group(1)
    newcell = {'cell_type': 'markdown', 'metadata': {}, 'source': '# {}'.format(title)}
    return nbformat.from_dict(newcell)

def add_link_to_pdf_ipynb(notebook_file):
    nb = nbformat.read(notebook_file, 4)
    pdffile = os.path.basename(notebook_file).split(".")[0] + ".pdf"
    source = "\n<hr>\n[Download this lesson in PDF]({attach}/images/" + pdffile + ")\n<hr>"
    if nb.cells[-1]["source"] != source:
        newcell = nbformat.from_dict({'cell_type': 'markdown', 'metadata': {}, 'source': source})
        nb.cells.append(newcell)
        nbformat.write(nb, notebook_file)

def remove_pdf_link_ipynb(notebook_file):
    nb = nbformat.read(notebook_file, 4)
    pdffile = os.path.basename(notebook_file).split(".")[0] + ".pdf"
    source = "\n<hr>\n[Download this lesson in PDF]({attach}/images/" + pdffile + ")\n<hr>"
    if nb.cells[-1]["source"] == source:
        nb.cells.pop()
        nbformat.write(nb, notebook_file)

def make_pdf_from_ipynb(notebook_file):
    remove_pdf_link_ipynb(notebook_file)
    exporter = nbconvert.PDFExporter()
    nb = nbformat.read(notebook_file, 4)
    firstcell = nb["cells"][0]
    nb["cells"][0] = extract_title_ipynb(nb["cells"][0])
    pdf, resources = exporter.from_notebook_node(nb)
    outfile = "../content/images/" + notebook_file.split(".")[0] + ".pdf"
    with open(outfile, "wb") as tp:
        tp.write(pdf)
    add_link_to_pdf_ipynb(notebook_file)


make_pdf_from_ipynb("content/Lessons/errors.ipynb")


# next steps:

# 1.  Hook in pandoc just swiping code from API for MD files. (extract yaml stuff at top, maybe just put lines around it and let it be a yaml block)

# 2.  Write some code to shove it all to a directory under images

# 3.  Write some code to append to every file a "get this as a pdf" -- for markdown, just put at bottom, for ipynb, put in cell.  (Can I get crazy and flip it so the PDFs all have "go to html" as well?)
