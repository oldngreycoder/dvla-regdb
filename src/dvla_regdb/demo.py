from dvla_regdb.register import VRegister
from dvla_regdb.sample_data import create_sample_register


def find_vehicle_id(vregister: VRegister, vid: str) -> str:
    veh_id = vregister.find_vehicle_id_for_registration(vid)
    if veh_id is None:
        veh_id = "Unassigned"
    return veh_id


def demo() -> None:
    vregister = create_sample_register()

    print(f"There are {vregister.count()} registrations")

    vid = vregister.find_registration("AB01 CDE")
    if vid.vehicle is not None:
        print(
            f"Registration {vid.registration_id}  Year {vid.year} "
            f"Id {vid.vehicle.vehicle_id}"
        )

    print(f"Registration {'AB01 CDE'} has Id {find_vehicle_id(vregister, 'AB01 CDE')}")

    print(f"Registration {'FG02 HJK'} has Id {find_vehicle_id(vregister, 'FG02 HJK')}")

    print(
        f"Registration {'L33T H4X0R'} has Id {find_vehicle_id(vregister, 'L33T H4X0R')}"
    )


if __name__ == "__main__":
    demo()
