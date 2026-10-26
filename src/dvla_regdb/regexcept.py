class VehicleRegisterError(Exception):
    """Base class for all Registration Errors"""


class VehicleExistsError(VehicleRegisterError):
    """Vehicle exists with vehicle ID"""


class VehicleNotFoundError(VehicleRegisterError, LookupError):
    """No vehicle found with that vehicle ID"""


class VehicleRegistrationExistsError(VehicleRegisterError):
    """Vehicle registration exists with vehicle registration datastore"""


class VehicleRegistrationNotFoundError(VehicleRegisterError, LookupError):
    """Vehicle registration not found in the vehicle registrations datastore"""


class VehicleRegistrationInputError(VehicleRegisterError):
    """Vehicle registration failed validation check"""


class VehicleIdSharingError(VehicleRegisterError):
    """Vehicle registration failed validation check"""
