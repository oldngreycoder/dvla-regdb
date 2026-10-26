from dataclasses import replace

from dvla_regdb.regexcept import (
    VehicleIdSharingError,
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
        self._assigned_vehicles = 0
        self._registrations = 0
        self._total_cost = 0.0

    def __len__(self) -> int:
        return len(self._register_store)

    def increment_assigned(self) -> None:
        self._assigned_vehicles += 1

    def increment_registrations(self) -> None:
        self._registrations += 1

    def increment_registration_cost(self, cost: float) -> None:
        self._total_cost = self._total_cost + cost

    def insert_vehicle_registration(
        self,
        registration_id: str,
        year: int,
        vehicle_id: str | None,
        cost: float | None,
    ) -> None:

        if registration_id in self._register_store:
            raise VehicleRegistrationExistsError(
                f"Vehicle Registration {registration_id!r} exists!."
            )
        if vehicle_id is not None:
            if vehicle_id in self._vehicle_registry:
                raise VehicleIdSharingError(f"Vehicle Id {vehicle_id} cannot be shared")

            vehicle = Vehicle(vehicle_id)
            self._vehicle_registry.insert_vehicle(vehicle)

            registration = Registration(
                registration_id=registration_id,
                year=year,
                vehicle=self._vehicle_registry.find_vehicle(vehicle_id),
                cost=cost,
            )
        else:
            registration = Registration(
                registration_id=registration_id,
                year=year,
                vehicle=None,
                cost=cost,
            )

        self.increment_registrations()
        if registration.vehicle is not None:
            self.increment_assigned()
        if registration.cost is not None:
            self.increment_registration_cost(registration.cost)

        self._register_store[registration_id] = registration

    def assign_vehicle_id(self, registration_id: str, vehicle_id: str) -> None:
        registration = self.find_registration(registration_id=registration_id)

        if self.has_vehicle(vehicle_id):
            raise VehicleIdSharingError(f"Vehicle Id {vehicle_id} cannot be shared")

        self._vehicle_registry.insert_vehicle(Vehicle(vehicle_id))
        update_reg = replace(
            registration,
            vehicle=self._vehicle_registry.find_vehicle(vehicle_id=vehicle_id),
        )
        self.update_registration(registration_id, update_reg)

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

    def update_registration(self, registration_id: str, vreg: Registration) -> None:
        if registration_id not in self._register_store:
            raise VehicleRegistrationNotFoundError(
                f"Vehicle Registration{registration_id!r} is not found!."
            )
        self._register_store[registration_id] = vreg

    def registrations(self) -> int:
        return self._registrations

    def assigned_registrations(self) -> int:
        return self._assigned_vehicles

    def total_cost(self) -> float:
        return self._total_cost
