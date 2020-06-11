# filter_api

## Dependencies ##

To install dependencies, you just need to create a new envirement then run.
  `pip install -r requirement.txt`
I used for the project:
* [Falcon](https://falcon.readthedocs.io/en/stable/): Falcon as a minimalist library for building speedy web APIs.
* [Pandas](https://pandas.pydata.org/): Pandas as a powerful and flexible tool to manipulation data.
 
## How to run ##
To run the project, you need to:
* Download the project or clone in.
* Install all the dependencies using `pip install -r requirement.txt`. 
* Navigate to your folder filter_api 
* Start the local server using by `node sync.js`.
* Start _server.js_ using `node server.js`.
* The adress of the application is: http://localhost:3132
* Enjoy.
waitress-serve --port=8000 tfilter_api:app

http://localhost:8000/api/filter?countries=[DE]
