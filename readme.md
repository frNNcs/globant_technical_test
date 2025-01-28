# Prueba tecnica Globant

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.dev/frNNcs/globant_technical_test)

A Poke-berries statistics API.

## Commands

### Run dev server
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/dev.txt
uvicorn main:app --reload --port 8000
```

## Run containered server
```bash
docker compose up -d
```

### Testing and lighting
```bash
python3 -m pytest
python3 -m flake8
```

### Check Endpoint
```bash
curl -X GET http://127.0.0.1:8000/allBerryStats
```

### Benchmark

```bash
time curl -X GET http://127.0.0.1:800o/allBerryStats
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

---
<details>

<summary>General rules:</summary>

-   Commit your changes to a public repository in GitHub.
-   Add a README.md with instructions to run the code.

Support the following endpoints

GET /allBerryStats

This endpoint should consume an external API to get the proper info, The documentation page for the data source is at [https://pokeapi.co/docs/v2#berries](https://pokeapi.co/docs/v2#berries)

Response:

{
    "berries_names": [...],
    "min_growth_time": "" // time, int
    "median_growth_time": "", // time, float
    "max_growth_time": "" // time, int
    "variance_growth_time": "" // time, float
    "mean_growth_time": "", // time, float
    "frequency_growth_time": "", // time, {growth_time: frequency, ...}
}

-   The data must be human-readable.
-   Use environment variables for configuration.
-   The response must include the content-type header (application/json)
-   Code must be tested with pytest.

For extra points (all of this is optional):

-   Upload and deploy the solution to a free cloud service for example python anywhere or equivalent.
-   Use a containering system like docker
-   Use a cache to speed up the queries.
-   Use a Python library (example: Matplotlib) to create a Histogram graph and display the image in a plain html in a new endpoint.

Please approach this task as an opportunity to showcase your proficiency and attention to detail. While there is no immediate urgency, I kindly ask that you provide us with an estimated time of completion at your earliest convenience. This will help us plan our review process accordingly.

Take the necessary time to ensure quality and accuracy in your work. We value thoroughness over speed and look forward to seeing your solution.

Thank you for your participation in this assessment stage. Should you have any questions or require further clarification on the task, please do not hesitate to reach out.

</details>
