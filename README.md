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
* Start the local server using by `waitress-serve --port=8000 filter_api:app`.
* The adress of the application is: http://localhost:8000/api/filter.
* Lest's filter only countries in DE: http://localhost:8000/api/filter?countries=[DE].
* Enjoy playing with the filter :smiley:.
* More filters http://localhost:8000/api/filter?countries=[DE]&display=[date,channel,country,cpi,os]&os=[ios,android]&channels=[facebook,google,chartboost].

## API Parameters ##

* [display:list]: List of the columns that should be displayed 
* [countries:list]: List of the countries that should be filtred 
* [os:list]: List of the channels that should be filtred 
* [channels:list]: List of the channels that should be filtred
* [order_by:list]: List of the culumns for the  order by
* [group_by:list]:  List of the culumns for the  group by
* [sum:list]:  List of the culumns that will be summed according to the group by 
* [start_date:Datetime: "%Y-%m-%d"]:  The start date for the date filter 
* [end_date:Datetime: "%Y-%m-%d"]: The end date for the date filter
* [inc: Boolean]: Defines if the order by is ascending

## Exemples ##
### Query 1 ###
* Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
* http://localhost:8000/api/filter?group_by=[channel,country]&sum=[impressions,clicks]&order_by=[clicks]&end_date=2017-06-01&inc=False

![q1](https://user-images.githubusercontent.com/22852604/84398621-77e9a600-ac00-11ea-876f-95144e6f8b09.PNG)

### Query 2 ###
* Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
* http://localhost:8000/api/filter?group_by=[date]&sum=[installs]&order_by=[date]&end_date=2017-05-31&start_date=2017-05-01&inc=True
![q2](https://user-images.githubusercontent.com/22852604/84398623-77e9a600-ac00-11ea-9fdc-aa4c8a81d098.PNG)
### Query 3 ###
* Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
http://localhost:8000/api/filter?group_by=[os]&sum=[revenue]&order_by=[revenue]&end_date=2017-06-01&start_date=2017-06-01&inc=False&countries=[US]
![q3](https://user-images.githubusercontent.com/22852604/84398619-76b87900-ac00-11ea-8ca4-1d52b0359d64.PNG)
### Query 4 ###
* Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.
http://localhost:8000/api/filter?order_by=[cpi]&inc=False&countries=[CA]
![q4](https://user-images.githubusercontent.com/22852604/84398620-77510f80-ac00-11ea-957f-d5c5b1c1c985.PNG)

## Authors ##

* Jihen Bouguerra
  * Github: [https://github.com/jihenBouguerra](https://github.com/jihenBouguerra)
  * Email: [bouguera.jihen@gmail.com](bouguera.jihen@gmail.com)
  * LinkedIn: [jihen-bouguerra](https://www.linkedin.com/in/jihen-bouguerra/)
