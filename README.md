# Filter_api
A python API for filtering Csv file data given by Adjust.
[More details](https://gist.github.com/kotik/93bbded94031a04e46f75cbef23b2ec7)

## Dependencies ##

To install dependencies, you just need to create a new envirement then run.
  `pip install -r requirement.txt`
I used for the project:
* [Falcon](https://falcon.readthedocs.io/en/stable/): Falcon as a minimalist library for building speedy web APIs.
* [Pandas](https://pandas.pydata.org/): Pandas as a powerful and flexible tool to manipulation data.
* [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/): Waitress as Python WSGI server.
 
## How to run ##
To run the project, you need to:
* Download the project or clone in.
* Install all the dependencies using `pip install -r requirement.txt. 
* Navigate to your folder filter_api.
* Start the local server using by `waitress-serve --port=8000 tfilter_api:app`.
* The adress of the application is: http://localhost:8000/api/filter.
* Lest's filter only countries in DE: http://localhost:8000/api/filter?countries=[DE].
* Enjoy playing with the filter :smiley:.


## Authors ##

* Jihen Bouguerra
  * Github: [https://github.com/jihenBouguerra](https://github.com/jihenBouguerra)
  * Email: [bouguera.jihen@gmail.com](bouguera.jihen@gmail.com)
  * LinkedIn: [jihen-bouguerra](https://www.linkedin.com/in/jihen-bouguerra/)
