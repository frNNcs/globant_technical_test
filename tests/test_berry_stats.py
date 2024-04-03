import pytest
from httpx import AsyncClient

from api.models.berry import BerryStats
from main import app


@pytest.mark.asyncio
async def test_allBerryStats_ok():
    async with AsyncClient(app=app, base_url='http://test') as client:
        response = await client.get('/allBerryStats')

        assert response.status_code == 200
        assert BerryStats(**response.json()).dict() == response.json()
