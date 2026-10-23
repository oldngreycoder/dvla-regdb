from dvla_regdb.regexcept import VehicleExistsError, VehicleNotFoundError
from dvla_regdb.vehicle import Vehicle


class VRegistry:
    def __init__(self) -> None:
        self._vehicle_registry: dict[str, Vehicle] = {}

    def __contains__(self, vehicle_id: object) -> bool:
        return vehicle_id in self._vehicle_registry

    def insert_vehicle(self, vehicle: Vehicle) -> None:
        if vehicle.vehicle_id in self._vehicle_registry:
            raise VehicleExistsError(f"Vehicle {vehicle.vehicle_id!r} exists!.")
        self._vehicle_registry[vehicle.vehicle_id] = vehicle

    def find_vehicle(self, vehicle_id: str) -> Vehicle:
        if vehicle_id not in self._vehicle_registry:
            raise VehicleNotFoundError(f"Vehicle {vehicle_id!r} is not found!.")
        return self._vehicle_registry[vehicle_id]
