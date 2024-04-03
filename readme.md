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

## Data
- [Pokeapi/berries](https://pokeapi.co/docs/v2#berries)

## Tools
- [FastApi](https://github.com/tiangolo/fastapi)
- [Pydantic](https://github.com/pydantic/pydantic)
- [pytest](https://github.com/pytest-dev/pytest)
- [flake8](https://github.com/pycqa/flake8/)
- [Uvicorn](https://github.com/encode/uvicorn)
- [PokeApi](https://pokeapi.co/docs/v2#berries-section)
