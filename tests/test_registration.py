import pytest

from dvla_regdb.registration import Registration
from dvla_regdb.vehicle import Vehicle


@pytest.fixture
def registration() -> Registration:
    return Registration(
        registration_id="AB01 CDE", year=2001, vehicle=Vehicle("12345"), cost=None
    )


class TestRegistration:
    def test_registration_data_setup(self, registration: Registration) -> None:
        assert registration.registration_id == "AB01 CDE"
        assert registration.year == 2001
        assert registration.vehicle is not None
        assert registration.vehicle == Vehicle("12345")
        assert registration.cost is None
