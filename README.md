###App to retrieve list of movies from Ghibli Productions API

# Setup

Clone the repo:
`git clone https://github.com/devdob/ghibli-movies.git`

cd into directory
`cd ghibli-movies`

Build and run docker compose
`docker-compose up -d --build`

Once done, give the containers a couple of minutes of start up fully, 
then navigate to `localhost:8000/movies`

It might take up to a minute after initial launch until the DB is filled with 
data from the API.
