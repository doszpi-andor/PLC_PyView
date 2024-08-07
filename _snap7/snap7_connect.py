from snap7.client import Client
from snap7.type import Areas
from snap7.util import get_byte, set_byte, get_int, set_int


class S7AddressException(Exception):
    """
    S7 Address exception
    """
    pass


class S7ConnectFailed(Exception):
    """
    S7 Connect Failed
    """
    pass


# noinspection PyPep8Naming
class PLC_Connect:
    """
    Snap 7 connection
    :parameter str ip: PLC ip address (string)
    :parameter int rack: PLC rack id
    :parameter int slot: PLC slot id
    """

    def __init__(self, ip, rack, slot):
        self.__ip = ip
        self.__rack = rack
        self.__slot = slot
        self.__plc = Client()
        self.__connected = False

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        self.__ip = ip

    @property
    def connected(self) -> bool:
        """
        PLC connected information (getter)
        :return: PLC connected boolean
        """
        return self.__connected

    def disconnect(self) -> None:
        """
        PLC disconnecting
        """
        self.__connected = False
        self.__plc.disconnect()

    def get_tag_byte(self, s7_address, length):
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'B':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                return self.__get_byte(Areas.PE, 0, address, length)
            elif s7_address[0] == 'Q':
                return self.__get_byte(Areas.PA, 0, address, length)
            elif s7_address[0] == 'M':
                return self.__get_byte(Areas.MK, 0, address, length)
        else:
            return 0

    def get_db_byte(self, s7_address, length):
        try:
            db_address, byte_address = s7_address.split(sep='.')
        except ValueError:
            raise S7AddressException

        if len(db_address) < 3 or db_address[0:2] != 'DB':
            raise S7AddressException

        if len(byte_address) < 4 or byte_address[0:3] != 'DBB':
            raise S7AddressException

        try:
            db_number = int(db_address[2:])
            byte_number = int(byte_address[3:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            return self.__get_byte(Areas.DB, db_number, byte_number, length)
        else:
            return 0

    def set_tag_byte(self, s7_address, length, byte_page) -> None:
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'B':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                self.__set_byte(Areas.PE, 0, address, length, byte_page)
            elif s7_address[0] == 'Q':
                self.__set_byte(Areas.PA, 0, address, length, byte_page)
            elif s7_address[0] == 'M':
                self.__set_byte(Areas.MK, 0, address, length, byte_page)

    def set_db_byte(self, s7_address, length, byte_page):
        try:
            db_address, byte_address = s7_address.split(sep='.')
        except ValueError:
            raise S7AddressException

        if len(db_address) < 3 or db_address[0:2] != 'DB':
            raise S7AddressException

        if len(byte_address) < 4 or byte_address[0:3] != 'DBB':
            raise S7AddressException

        try:
            db_number = int(db_address[2:])
            byte_number = int(byte_address[3:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            self.__set_byte(Areas.DB, db_number, byte_number, length, byte_page)

    def get_tag_int(self, s7_address, length):
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'W':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                return self.__get_int(Areas.PE, 0, address, length)
            elif s7_address[0] == 'Q':
                return self.__get_int(Areas.PA, 0, address, length)
            elif s7_address[0] == 'M':
                return self.__get_int(Areas.MK, 0, address, length)
        return 0

    def get_db_int(self, s7_address, length):
        try:
            db_address, byte_address = s7_address.split(sep='.')
        except ValueError:
            raise S7AddressException

        if len(db_address) < 3 or db_address[0:2] != 'DB':
            raise S7AddressException

        if len(byte_address) < 4 or byte_address[0:3] != 'DBW':
            raise S7AddressException

        try:
            db_number = int(db_address[2:])
            byte_number = int(byte_address[3:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            return self.__get_int(Areas.DB, db_number, byte_number, length)
        else:
            return 0

    def set_tag_int(self, s7_address, length, int_page) -> None:
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'W':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                self.__set_int(Areas.PE, 0, address, length, int_page)
            elif s7_address[0] == 'Q':
                self.__set_int(Areas.PA, 0, address, length, int_page)
            elif s7_address[0] == 'M':
                self.__set_int(Areas.MK, 0, address, length, int_page)

    def set_db_int(self, s7_address, length, int_page):
        try:
            db_address, byte_address = s7_address.split(sep='.')
        except ValueError:
            raise S7AddressException

        if len(db_address) < 3 or db_address[0:2] != 'DB':
            raise S7AddressException

        if len(byte_address) < 4 or byte_address[0:3] != 'DBW':
            raise S7AddressException

        try:
            db_number = int(db_address[2:])
            byte_number = int(byte_address[3:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            self.__set_int(Areas.DB, db_number, byte_number, length, int_page)

    def __get_byte(self, area, db_number, address, length):
        try:
            result = self.__plc.read_area(area, db_number, address, length)
        except RuntimeError:
            self.disconnect()
            raise S7ConnectFailed
        byte_list = []
        for index in range(0, length):
            byte_list.append(get_byte(result, index))
        return byte_list

    def __set_byte(self, area, db_number, address, length, data):
        try:
            result = self.__plc.read_area(area, db_number, address, length)
            for index in range(0, length):
                set_byte(result, index, data[index])
            self.__plc.write_area(area, db_number, address, result)
        except RuntimeError:
            self.disconnect()
            raise S7ConnectFailed

    def __get_int(self, area, db_number, address, length):
        try:
            result = self.__plc.read_area(area, db_number, address, length * 2)
        except RuntimeError:
            self.disconnect()
            raise S7ConnectFailed
        int_list = []
        for index in range(0, length):
            int_list.append(get_int(result, index * 2))
        return int_list

    def __set_int(self, area, db_number, address, length, data):
        try:
            result = self.__plc.read_area(area, db_number, address, length * 2)
            for index in range(0, length):
                set_int(result, index * 2, data[index])
            self.__plc.write_area(area, db_number, address, result)
        except RuntimeError:
            self.disconnect()
            raise S7ConnectFailed

    def __connect(self):
        if not self.__connected:
            if self.__ip == '':
                self.__connected = False
                raise S7ConnectFailed
            try:
                self.__plc.connect(self.__ip, self.__rack, self.__slot)
            except RuntimeError:
                self.__connected = False
                raise S7ConnectFailed
            self.__connected = True
        return True


if __name__ == '__main__':
    # plc = PLC_Connect('172.16.65.1', 0, 2)
    plc = PLC_Connect('192.168.90.2', 0, 1)

    print(plc.get_tag_int('IW64', 4))

