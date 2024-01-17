# Search Engine
While it is misleading to call this project a search engine, what I am doing is closest thing to a search engine I have ever created.
##

Most of the notes is are in the [Jupiter notebook](./search.ipynb)

## How to run it

- run `python main.py` for normal instances
- add option: `--jobs` or `--products` to specify the thing to search in
- add option `--query [search string]` to specify what you are searching

### Example

1. Search for book review related jobs: 
    - `python main.py --jobs --query "Book review"`
2. Search a showering jell related products: 
    - `python main.py --products --query "Showering jell"`