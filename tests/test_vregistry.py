import pytest

from dvla_regdb.regexcept import VehicleExistsError, VehicleNotFoundError
from dvla_regdb.vehicle import Vehicle
from dvla_regdb.vregistry import VRegistry


@pytest.fixture
def vehicle_registry() -> VRegistry:
    vregistry = VRegistry()
    test_12345 = Vehicle(vehicle_id="12345")
    test_67890 = Vehicle(vehicle_id="67890")
    vregistry.insert_vehicle(test_12345)
    vregistry.insert_vehicle(test_67890)
    return vregistry


class TestVRegistry:
    def test_get_vehicle_id_12345(self, vehicle_registry: VRegistry) -> None:
        v12345 = vehicle_registry.find_vehicle("12345")
        assert v12345.vehicle_id == "12345"

    def test_get_vehicle_id_67890(self, vehicle_registry: VRegistry) -> None:
        v12345 = vehicle_registry.find_vehicle("67890")
        assert v12345.vehicle_id == "67890"

    def test_get_vehicle_id_doesnt_exist(self, vehicle_registry: VRegistry) -> None:
        with pytest.raises(VehicleNotFoundError):
            vehicle_registry.find_vehicle("999999")

    def test_vehicle_id_exists(self, vehicle_registry: VRegistry) -> None:
        test_12345 = Vehicle(vehicle_id="12345")
        with pytest.raises(VehicleExistsError):
            vehicle_registry.insert_vehicle(test_12345)
