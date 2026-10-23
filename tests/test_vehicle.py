import pytest

from dvla_regdb.vehicle import Vehicle


@pytest.fixture
def vehicle() -> Vehicle:
    return Vehicle(vehicle_id="12345")


class TestVehicle:
    def test_get_vehicle_id(self, vehicle: Vehicle) -> None:
        assert vehicle.vehicle_id == "12345"
