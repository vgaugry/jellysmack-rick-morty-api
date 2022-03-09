# jellysmack-rick-morty-api
Rick & Morty API for Jellysmack recruitment by Vincent Gaugry.

## Usage
First, you need to install all requirements :
```bash
pip install -r requirements.txt
```
> :warning: **remember to use a pyhton virtualenv**
> 
To launch the API server locally, execute those commands :
```bash
cd app
uvicorn main:app --reload
```

when API server is running you can access it at : http://127.0.0.1:8000/docs

## Work description
>Took me 7 hours to develop that project.
> 
>Features completed = feature 1, feature 2, feature 3 and CSV export feature.

### Git repository organisation
The functionnal part is on the `main` branch.

You can find all features in order of development on `feature1`, `feature2`, `feature3` and `featureCSV` branches.

You can also find a unit test initiation on the branch `tests` but it needs refactoring to work properly.

### Personal approach
I choose to work with SQLite and SQLAlchemy since the SQLite build is quite simple. It's my first project using SQLAlchemy. I decided to use it because FastAPI describe it in the documentation.

It took me some time to properly understand the SQLAlchemy ORM. It allows us to have a good control over datas and to map our entities with Pydantic schemas.

### To go further
- Finish all the features
- Refactoring module import and handle a proper use of unit tests
- Cover all the routes and crud action with unit tests
- Refactoring with crud, models and schemas folder
- Refactoring with routes folder and routers
- Use a proper DB like PostgreSQL for production 