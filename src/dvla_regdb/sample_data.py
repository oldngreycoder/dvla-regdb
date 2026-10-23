from dvla_regdb.register import VRegister


def create_sample_register() -> VRegister:
    vregister = VRegister()
    vregister.insert_vehicle_registration("AB01 CDE", 2001, "12345")
    vregister.insert_vehicle_registration("FG02 HJK", 2002, "67890")
    vregister.insert_registration("L33T H4X0R", 2022)
    return vregister
