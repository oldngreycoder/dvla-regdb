from pytest_bdd import given, parsers, scenarios, then, when

from dvla_regdb.register import VRegister
from dvla_regdb.sample_data import create_sample_register

scenarios("registrations.feature")  # collect every scenario in the file


@given("The Register contains Registrations", target_fixture="register")
def register() -> VRegister:
    return create_sample_register()


@when("I count the registrations", target_fixture="count")
def count_registrations(register: VRegister) -> int:
    return register.registrations()


@then(parsers.parse("there are {expected:d} registrations"))
def check_count(count: int, expected: int) -> None:
    assert count == expected


@when("I accumulate the registration cost", target_fixture="total_cost")
def accumulate_cost(register: VRegister) -> float:
    return register.total_cost()


@then(parsers.parse("the total cost is {expected:d}"))
def check_cost(total_cost: float, expected: float) -> None:
    assert total_cost == expected


@then(parsers.parse('the vehicle_id is "{expected}"'))
def check_vehicle_id(actual_vehicle_id: str | None, expected: str) -> None:
    expected_vehicle_id = None if expected == "Unassigned" else expected
    assert actual_vehicle_id == expected_vehicle_id


@when(
    parsers.parse('I look up the vehicle_id of "{registration_id}"'),
    target_fixture="actual_vehicle_id",
)
def look_up_vehicle_id(register: VRegister, registration_id: str) -> str | None:
    return register.find_vehicle_id_for_registration(registration_id)
