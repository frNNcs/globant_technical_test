# Prueba tecnica Globant

A Poke-berries statistics API.

## Commands

### Start fast-api server

```bash
uvicorn main:app --reload --port 8001
```

### test

```bash
curl -X GET http://127.0.0.1:8001/allBerryStats
```

### Benchmark

```bash
time curl -X GET http://127.0.0.1:8001/allBerryStats

{
    "berries_names": ["cheri", ...],
    "min_growth_time": 2,
    "median_growth_time": 12.859375,
    "max_growth_time": 24,
    "variance_growth_time": 22,
    "mean_growth_time": 12.859375,
    "frequency_growth_time": {
        "3": 5,
        "4": 3,
        "12": 1,
        "8": 7,
        "5": 5,
        "2": 5,
        "6": 4,
        "15": 5,
        "18": 17,
        "24": 12
    }
}

0.00s user 0.01s system 0% cpu 55.375 total
0.01s user 0.01s system 0% cpu 31.564 total
```


## Data

-   [Pokeapi/berries](https://pokeapi.co/docs/v2#berries)

## Tools

-   [FastApi](https://github.com/tiangolo/fastapi)
-   [Pydantic](https://github.com/pydantic/pydantic)
-   [pytest](https://github.com/pytest-dev/pytest)
-   [flake8](https://github.com/pycqa/flake8/)
-   [Uvicorn](https://github.com/encode/uvicorn)
-   [PokeApi](https://pokeapi.co/docs/v2#berries-section)
