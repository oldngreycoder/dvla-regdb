from dvla_regdb.regexcept import (
    VehicleRegistrationExistsError,
    VehicleRegistrationNotFoundError,
)
from dvla_regdb.registration import Registration
from dvla_regdb.vehicle import Vehicle
from dvla_regdb.vregistry import VRegistry


class VRegister:
    def __init__(self) -> None:
        self._register_store: dict[str, Registration] = {}
        self._vehicle_registry = VRegistry()

    def __len__(self) -> int:
        return len(self._register_store)

    def insert_vehicle_registration(
        self, registration_id: str, year: int, vehicle_id: str
    ) -> None:
        if registration_id in self._register_store:
            raise VehicleRegistrationExistsError(
                f"Vehicle Registration {registration_id!r} exists!."
            )
        if vehicle_id not in self._vehicle_registry:
            vehicle = Vehicle(vehicle_id)
            self._vehicle_registry.insert_vehicle(vehicle)
        registration = Registration(
            registration_id, year, self._vehicle_registry.find_vehicle(vehicle_id)
        )
        self._register_store[registration_id] = registration

    def insert_registration(self, registration_id: str, year: int) -> None:
        if registration_id in self._register_store:
            raise VehicleRegistrationExistsError(
                f"Vehicle Registration {registration_id!r} exists!."
            )
        registration = Registration(registration_id, year, None)
        self._register_store[registration_id] = registration

    def find_registration(self, registration_id: str) -> Registration:
        if registration_id not in self._register_store:
            raise VehicleRegistrationNotFoundError(
                f"Vehicle Registration{registration_id!r} is not found!."
            )
        return self._register_store[registration_id]

    def find_vehicle_id_for_registration(self, registration_id: str) -> str | None:
        reg = self.find_registration(registration_id)
        if reg.vehicle is None:
            return None
        return reg.vehicle.vehicle_id

    def has_vehicle(self, vid: str) -> bool:
        return vid in self._vehicle_registry

    def count(self) -> int:
        return len(self._register_store)
