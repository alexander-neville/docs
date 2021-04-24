from container_package import bic

class universal(object):

    serial_number = 1337

    @classmethod
    def get_serial(cls):

        serial = cls.serial_number
        cls.serial_number += 1
        return str(serial).zfill(6)

    def __init__(self, owner):

        self._owner = owner
        self._type = "U"
        self._serial = self.get_serial()
        self._bic = bic.new_bic(self._owner, self._type, self._serial)


    def return_bic(self):

        return self._bic

class reefer(universal):

    def __init__(self, owner):

        self._owner = owner
        self._type = "R"
        self._serial = self.get_serial()
        self._bic = bic.new_bic(self._owner, self._type, self._serial)
