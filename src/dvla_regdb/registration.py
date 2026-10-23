from dataclasses import dataclass

from dvla_regdb.vehicle import Vehicle


@dataclass(frozen=True)
class Registration:
    registration_id: str
    year: int
    vehicle: Vehicle | None = None
