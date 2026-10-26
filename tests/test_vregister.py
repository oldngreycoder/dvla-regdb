import pytest

from dvla_regdb.regexcept import (
    VehicleIdSharingError,
    VehicleRegistrationExistsError,
    VehicleRegistrationNotFoundError,
)
from dvla_regdb.register import VRegister
from dvla_regdb.vehicle import Vehicle


@pytest.fixture
def vehicle_register() -> VRegister:
    vregister = VRegister()
    vregister.insert_vehicle_registration(
        registration_id="AB01 CDE", year=2001, vehicle_id="12345", cost=None
    )
    vregister.insert_vehicle_registration(
        registration_id="FG02 HJK", year=2002, vehicle_id="67890", cost=None
    )
    vregister.insert_vehicle_registration(
        registration_id="L33T H4X0R", year=2022, vehicle_id=None, cost=1000000.0
    )
    vregister.insert_vehicle_registration(
        registration_id="AGIL3", year=2022, vehicle_id="999999", cost=100.0
    )

    return vregister


class TestVRegistry:
    def test_insert_registration(self, vehicle_register: VRegister) -> None:

        vAB01_CDE = vehicle_register.find_registration("AB01 CDE")
        vFG02_HJK = vehicle_register.find_registration("FG02 HJK")
        vL33T_H4X0R = vehicle_register.find_registration("L33T H4X0R")
        vAGIL3 = vehicle_register.find_registration("AGIL3")

        assert (
            vAB01_CDE.registration_id == "AB01 CDE"
            and vAB01_CDE.year == 2001
            and vAB01_CDE.vehicle == Vehicle("12345")
            and vAB01_CDE.cost is None
        )

        assert (
            vFG02_HJK.registration_id == "FG02 HJK"
            and vFG02_HJK.year == 2002
            and vFG02_HJK.vehicle is not None
            and vFG02_HJK.vehicle == Vehicle("67890")
            and vFG02_HJK.cost is None
        )

        assert (
            vL33T_H4X0R.registration_id == "L33T H4X0R"
            and vL33T_H4X0R.year == 2022
            and vL33T_H4X0R.vehicle is None
            and vL33T_H4X0R.cost is not None
            and vL33T_H4X0R.cost == 1000000.00
        )

        assert (
            vAGIL3.registration_id == "AGIL3"
            and vAGIL3.year == 2022
            and vAGIL3.vehicle is not None
            and vAGIL3.vehicle == Vehicle("999999")
            and vAGIL3.cost is not None
            and vAGIL3.cost == 100.00
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

    def test_count(self, vehicle_register: VRegister) -> None:
        assert vehicle_register.count() == 4

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
            vehicle_register.insert_vehicle_registration(
                registration_id="AB01 CDE", year=2001, vehicle_id="12345", cost=None
            )

    def test_half_insert(self, vehicle_register: VRegister) -> None:
        with pytest.raises(VehicleRegistrationExistsError):
            vehicle_register.insert_vehicle_registration(
                registration_id="AB01 CDE", year=2001, vehicle_id="99999", cost=None
            )
        assert not vehicle_register.has_vehicle("99999")

    def test_assign_vehicle_id(self, vehicle_register: VRegister) -> None:
        vehicle_register.assign_vehicle_id(
            registration_id="L33T H4X0R", vehicle_id="111111"
        )
        assert vehicle_register.has_vehicle("111111")
        vreg = vehicle_register.find_registration("L33T H4X0R")
        assert vreg.vehicle is not None
        assert vreg.vehicle.vehicle_id == "111111"

    def test_shared_vehicle_id(self, vehicle_register: VRegister) -> None:
        with pytest.raises(VehicleIdSharingError):
            vehicle_register.insert_vehicle_registration(
                registration_id="DEAD BEEF", year=2001, vehicle_id="12345", cost=None
            )
        with pytest.raises(VehicleRegistrationNotFoundError):
            vreg = vehicle_register.find_registration("DEAD BEEF")
            assert vreg.vehicle is None

    def test_assign_vehicle_id_no_sharing(self, vehicle_register: VRegister) -> None:
        with pytest.raises(VehicleIdSharingError):
            vehicle_register.assign_vehicle_id(
                registration_id="L33T H4X0R", vehicle_id="12345"
            )

    def test_assigned_registrations(self, vehicle_register: VRegister) -> None:
        assert vehicle_register.assigned_registrations() == 3

    def test_registrations(self, vehicle_register: VRegister) -> None:
        assert vehicle_register.registrations() == 4

    def test_cost(self, vehicle_register: VRegister) -> None:
        assert vehicle_register.total_cost() == 1000100
