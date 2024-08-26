# music_collab

The backend for music_collab, a platform that provides a real-time collaborative environment for songwriters to create and update lyrics and chord progressions together.

Core Features:
- Lyric writing interface with tools like a rhyming dictionary and syllable counter.
- Chord progression generator and editor.
- Cloud-based project sharing and collaboration.
- Integration with popular DAWs (Digital Audio Workstations).
- Version control for lyrics and music.

## Using Docker

- Install Docker.
- Ensure you have a `env/.env` file set up!
- From the root project folder run `docker-compose build`. This command builds the backend image and pulls the postgres image.
- To set up the database, run `docker-compose run --rm backend ./manage.py migrate` command to run migrations
- From the root project folder run `docker-compose up` to run the required containers.
  - The docker-postgres container uses the `env/.env` to configure the database, username and password.
  - First time this is run, it builds the docker image from the code base
  - In order to rebuild the image run `docker-compose build` before the `... up` command
- If using docker-compose, whenever a significant change is made to the `requirements.txt` file, it is best to run `docker-compose build` to ensure that your images are up to date.
- To run tests, the command to be used is `docker-compose run --rm backend ./manage.py test`
