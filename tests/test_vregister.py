import pytest

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

        vrgstrn_AB01_CDE = vehicle_register.find_registration("AB01 CDE")
        vrgstrn_FG02_HJK = vehicle_register.find_registration("FG02 HJK")
        rgstrn_L33T_H4X0R = vehicle_register.find_registration("L33T H4X0R")

        assert (
            vrgstrn_AB01_CDE.registration_id == "AB01 CDE"
            and vrgstrn_AB01_CDE.year == 2001
            and vrgstrn_AB01_CDE.vehicle == Vehicle("12345")
        )

        assert (
            vrgstrn_FG02_HJK.registration_id == "FG02 HJK"
            and vrgstrn_FG02_HJK.year == 2002
            and vrgstrn_FG02_HJK.vehicle == Vehicle("67890")
        )

        assert (
            rgstrn_L33T_H4X0R.registration_id == "L33T H4X0R"
            and rgstrn_L33T_H4X0R.year == 2022
            and rgstrn_L33T_H4X0R.vehicle is None
        )

    def test_find_vehicle_registration(self, vehicle_register: VRegister) -> None:
        vrgstrn_AB01_CDE = vehicle_register.find_registration("AB01 CDE")
        vrgstrn_FG02_HJK = vehicle_register.find_registration("FG02 HJK")

        assert (
            vrgstrn_AB01_CDE.registration_id == "AB01 CDE"
            and vrgstrn_AB01_CDE.year == 2001
            and vrgstrn_AB01_CDE.vehicle == Vehicle("12345")
        )

        assert (
            vrgstrn_FG02_HJK.registration_id == "FG02 HJK"
            and vrgstrn_FG02_HJK.year == 2002
            and vrgstrn_FG02_HJK.vehicle == Vehicle("67890")
        )

    def test_find_registration(self, vehicle_register: VRegister) -> None:
        rgstrn_L33T_H4X0R = vehicle_register.find_registration("L33T H4X0R")
        assert (
            rgstrn_L33T_H4X0R.registration_id == "L33T H4X0R"
            and rgstrn_L33T_H4X0R.year == 2022
            and rgstrn_L33T_H4X0R.vehicle is None
        )
