from dvla_regdb.register import VRegister


def create_sample_register() -> VRegister:
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
        registration_id="AG1L3", year=2022, vehicle_id="999999", cost=100.0
    )

    return vregister
