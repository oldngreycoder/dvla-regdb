from dataclasses import dataclass


@dataclass(frozen=True)
class Vehicle:
    vehicle_id: str
