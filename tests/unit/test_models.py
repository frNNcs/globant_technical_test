import pytest

from api.models.berry import Berry, BerryFirmness, BerryFlavor, BerryFlavorMap


def test_berry_firmness():
    firmness = BerryFirmness(
        name='soft',
        url='https://pokeapi.co/api/v2/berry-firmness/2/'
    )
    assert firmness.name == 'soft'
    assert firmness.url == 'https://pokeapi.co/api/v2/berry-firmness/2/'
    assert firmness.id == 2


def test_berry_flavor():
    flavor = BerryFlavor(
        name='spicy',
        url='https://pokeapi.co/api/v2/berry-flavor/1/'
    )
    assert flavor.name == 'spicy'
    assert flavor.url == 'https://pokeapi.co/api/v2/berry-flavor/1/'
    assert flavor.id == 1


def test_berry_flavor_map():
    flavor_map = BerryFlavorMap(
        flavor=BerryFlavor(
            name='spicy',
            url='https://pokeapi.co/api/v2/berry-flavor/1/'
        ),
        potency=10
    )
    assert flavor_map.flavor.name == 'spicy'
    assert flavor_map.flavor.url == 'https://pokeapi.co/api/v2/berry-flavor/1/'
    assert flavor_map.flavor.id == 1
    assert flavor_map.potency == 10


@pytest.fixture
def berry():
    return Berry(
        id=1,
        name='cheri',
        firmness=BerryFirmness(
            name='soft',
            url='https://pokeapi.co/api/v2/berry-firmness/2/'
        ),
        flavors=[
            BerryFlavorMap(
                flavor=BerryFlavor(
                    name='spicy',
                    url='https://pokeapi.co/api/v2/berry-flavor/1/'
                ),
                potency=10
            ),
        ],
        natural_gift_power=60,
        size=20,
        smoothness=25,
        soil_dryness=15,
        growth_time=3,
        max_harvest=5,
        item={},
        natural_gift_type={}
    )


def test_berry(berry):
    assert berry.id == 1
    assert berry.name == 'cheri'
    assert berry.firmness.name == 'soft'
    assert berry.firmness.url == 'https://pokeapi.co/api/v2/berry-firmness/2/'
    assert berry.firmness.id == 2
    assert len(berry.flavors) == 1
    assert berry.flavors[0].flavor.name == 'spicy'
    assert berry.flavors[0].flavor.url == 'https://pokeapi.co/api/v2/berry-flavor/1/'
    assert berry.flavors[0].flavor.id == 1
    assert berry.flavors[0].potency == 10
    assert berry.natural_gift_power == 60
    assert berry.size == 20
    assert berry.smoothness == 25
    assert berry.soil_dryness == 15
    assert berry.growth_time == 3
    assert berry.max_harvest == 5
    assert berry.item == {}
    assert berry.natural_gift_type == {}
