Dev Challenge design to serve some commands from punkapi, Dockerfile and compose are present in this repository.

API behind the scenes: `https://punkapi.com/documentation/v2`

Airflow Docker repo: `https://punkapi.com/documentation/v2`

Usage Without Docker
**********************

\* Check install page for installation

Execute sample code:
::

    python -m src byname -n Punk
    python -m src byid -i 193
    python -m src byinterval -f 10-2011 -u 10-2013
    python -m src byfood -f cream_cheese_frosting


Usage With Docker
**********************

Execute with parameters:
::

    docker run --rm devchallenge_devchallenge byname -n Punk
    docker run --rm devchallenge_devchallenge byid -i 193
    docker run --rm devchallenge_devchallenge byinterval -f 10-2011 -u 10-2013
    docker run --rm devchallenge_devchallenge byfood -f cream_cheese_frosting

Usage With Airflow
**********************

Execute with docker Airflow::

    docker-compose up

Will start all containers, execution of devchallenge happens within the webserver

Set able parameters in Airflow:

1.  beer_name[Matched as full or partial string], default is 'Punk' # use underscore insteadof space
2.  beer_id [exact matched]
3.  brewed_from [i.e. 10-2011], brewed_until[i.e. 10-2013]
4.  food_pairing [i.e. cream_cheese_frosting] # use underscore insteadof space
