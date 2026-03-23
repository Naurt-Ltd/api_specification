For the Python examples, you'll require some set up.

First, place a file called `api.key` next to this one containing only the API
key from Naurt you wish to use.

Then, make and activate a virtual environment.

In the `python` directory above this one, build the `naurt_api` package with
`python -m build` (you may need to do `python -m pip install --upgrade build`).

Install with `pip install -e .`.

Change directory back to the `examples` folder, and run examples from here 
e.g. `python forward_geocode.py`

I strongly advise against installing a local package to your system Python!
Always use a virtual env!