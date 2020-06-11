# filter_api

## Dependencies ##

To install dependencies, you just need to create a new envirement then run.
  pip install -r requirement.txt
I used for the project:
* [Falcon](https://falcon.readthedocs.io/en/stable/): Falcon as a minimalist library for building speedy web APIs.
* [Pandas](https://pandas.pydata.org/): Pandas as a powerful and flexible tool to manipulation data.
 

waitress-serve --port=8000 tfilter_api:app

http://localhost:8000/api/filter?countries=[DE]
