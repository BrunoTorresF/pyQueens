# pyQueens - my N-Queens solution with python3

## Run Instructions

**Requires Docker & Docker Compose**

1. Clone repo: `git clone https://github.com/BrunoTorresF/pyQueens.git`
1. Build containers: `docker-compose up --build -d`
1. Execute main program: `docker-compose run pyqueens`
1. Run tests: `docker-compose run pyqueens_test`
1. Check postgres instance: `docker exec -it postgres psql -U pyqueens -W`
   1. pyqueens role password is: `pyqueens8`

## Problem Context & Instructions

Here's the programming problem: https://en.wikipedia.org/wiki/Eight_queens_puzzle

These are the different aspects of the project you can work on (in order):

- [x] 1. determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens
- [x] 2. iterate over N and store the solutions in postgres using SQLAlchemy
- [x] 3. write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest
- [x] 4. Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)
- [x] 5. setup Travis CI (or similar) for your public GitHub repo to run the tests automatically

## Documentation & References

### N-queens & pytest

- https://www.freecodecamp.org/news/lets-backtrack-and-save-some-queens-1f9ef6af5415/
- https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
- https://www.geeksforgeeks.org/n-queen-problem-using-branch-and-bound/
- https://www.geeksforgeeks.org/n-queen-in-on-space/
- https://jrwalsh1.github.io/posts/permutations-and-the-n-queens-problem/
- https://docs.pytest.org/en/latest/parametrize.html

### Postgres & SQLAlchemy

- https://docs.sqlalchemy.org/en/13/index.html
- https://itnext.io/sqlalchemy-orm-connecting-to-postgresql-from-scratch-create-fetch-update-and-delete-a86bc81333dc
- https://www.compose.com/articles/using-postgresql-through-sqlalchemy/

### Docker

- https://docs.docker.com/
- https://github.com/hmajid2301/medium/tree/master/8.%20Docker%20with%20SQLAlchemy
- https://runnable.com/docker/python/dockerize-your-python-application
- https://www.saltycrane.com/blog/2019/01/how-run-postgresql-docker-mac-local-development/
- https://docs.docker.com/compose/

### CI/CD - CircleCI

- https://circleci.com/docs/2.0/language-python/
- https://circleci.com/docs/2.0/databases/#section=configuration
- https://circleci.com/docs/2.0/workflows/
