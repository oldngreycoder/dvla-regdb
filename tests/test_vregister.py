import pytest

from dvla_regdb.regexcept import (
    VehicleRegistrationExistsError,
    VehicleRegistrationNotFoundError,
)
from dvla_regdb.register import VRegister
from dvla_regdb.vehicle import Vehicle


@pytest.fixture
def vehicle_register() -> VRegister:
    vregister = VRegister()
    vregister.insert_vehicle_registration("AB01 CDE", 2001, "12345")
    vregister.insert_vehicle_registration("FG02 HJK", 2002, "67890")
    vregister.insert_registration("L33T H4X0R", 2022)

    return vregister


class TestVRegistry:
    def test_insert_registration(self, vehicle_register: VRegister) -> None:

        vAB01_CDE = vehicle_register.find_registration("AB01 CDE")
        vFG02_HJK = vehicle_register.find_registration("FG02 HJK")
        vL33T_H4X0R = vehicle_register.find_registration("L33T H4X0R")

        assert (
            vAB01_CDE.registration_id == "AB01 CDE"
            and vAB01_CDE.year == 2001
            and vAB01_CDE.vehicle == Vehicle("12345")
        )

        assert (
            vFG02_HJK.registration_id == "FG02 HJK"
            and vFG02_HJK.year == 2002
            and vFG02_HJK.vehicle == Vehicle("67890")
        )

        assert (
            vL33T_H4X0R.registration_id == "L33T H4X0R"
            and vL33T_H4X0R.year == 2022
            and vL33T_H4X0R.vehicle is None
        )

    def test_find_vehicle_registration(self, vehicle_register: VRegister) -> None:
        vAB01_CDE = vehicle_register.find_registration("AB01 CDE")
        vFG02_HJK = vehicle_register.find_registration("FG02 HJK")

        assert (
            vAB01_CDE.registration_id == "AB01 CDE"
            and vAB01_CDE.year == 2001
            and vAB01_CDE.vehicle == Vehicle("12345")
        )

        assert (
            vFG02_HJK.registration_id == "FG02 HJK"
            and vFG02_HJK.year == 2002
            and vFG02_HJK.vehicle == Vehicle("67890")
        )

    def test_find_registration(self, vehicle_register: VRegister) -> None:
        vL33T_H4X0R = vehicle_register.find_registration("L33T H4X0R")
        assert (
            vL33T_H4X0R.registration_id == "L33T H4X0R"
            and vL33T_H4X0R.year == 2022
            and vL33T_H4X0R.vehicle is None
        )

    def test_len(self, vehicle_register: VRegister) -> None:
        assert len(vehicle_register) == 3

    def test_reg_with_vehicle(self, vehicle_register: VRegister) -> None:
        vFG02_HJK = vehicle_register.find_vehicle_id_for_registration("FG02 HJK")
        assert vFG02_HJK == "67890"

    def test_reg_no_vehicle(self, vehicle_register: VRegister) -> None:
        vL33T_H4X0R = vehicle_register.find_vehicle_id_for_registration("L33T H4X0R")
        assert vL33T_H4X0R is None

    def test_reg_unknown(self, vehicle_register: VRegister) -> None:
        with pytest.raises(VehicleRegistrationNotFoundError):
            vehicle_register.find_vehicle_id_for_registration("unknown")

    def test_duplicate_registration(self, vehicle_register: VRegister) -> None:
        with pytest.raises(VehicleRegistrationExistsError):
            vehicle_register.insert_vehicle_registration("AB01 CDE", 2001, "12345")

    def test_half_insert(self, vehicle_register: VRegister) -> None:
        with pytest.raises(VehicleRegistrationExistsError):
            vehicle_register.insert_vehicle_registration("AB01 CDE", 2001, "99999")
        assert not vehicle_register.has_vehicle("99999")
