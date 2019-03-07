import sys, nbformat

HELP_STRING = """
python add_header_to_ipynb.py FILE_PATH --> print first cell
python add_header_to_ipynb.py FILE_PATH, TITLE, TAGS, YYYY-MM-DD --> add header cell for pelican
"""

def make_header_cell(title, tags, date):
    baseline_cell = {'cell_type': 'markdown',
                 'metadata': {},
                 'source': ''}
    mystring='''- title: {}
- tags: {}
- date: {}'''.format(title, tags, date)
    baseline_cell["source"] = mystring
    return baseline_cell

def add_header_to_notebook(notebook, header):
    nb = nbformat.read(notebook, 4)
    newcell = nbformat.from_dict(header)
    nb.cells.insert(0, newcell)
    nbformat.write(nb, notebook)

def read_notebook(notebook):
    nb = nbformat.read(notebook, 4)
    print(nb.cells[0])


def do_the_thing():
    args = sys.argv
    if len(args) == 2:
        read_notebook(args[1])
    elif len(args) < 5:
        print(HELP_STRING)
    else:
        notebook = args[1]
        header = make_header_cell(*args[2:])
        add_header_to_notebook(notebook, header)


if __name__ == "__main__":
    do_the_thing()
    
