import pytest

from dvla_regdb.registration import Registration


@pytest.fixture
def registration() -> Registration:
    return Registration(
        registration_id="L33T H4X0R", year=2001, vehicle=None, cost=1000000.0
    )


class TestRegistration:
    def test_registation_data_setup(self, registration: Registration) -> None:
        assert registration.registration_id == "L33T H4X0R"
        assert registration.year == 2001
        assert registration.vehicle is None
        assert registration.cost == 1000000.0
