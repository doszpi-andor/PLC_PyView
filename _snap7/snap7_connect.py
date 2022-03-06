from snap7.client import Client
from snap7.exceptions import Snap7Exception
from snap7.types import Areas
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

    def get_byte(self, s7_address, length):
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'B':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                return self.__get_byte(Areas.PE, address, length)
            elif s7_address[0] == 'Q':
                return self.__get_byte(Areas.PA, address, length)
            elif s7_address[0] == 'M':
                return self.__get_byte(Areas.MK, address, length)
        else:
            return 0

    def set_byte(self, s7_address, length, byte_page) -> None:
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'B':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                self.__set_byte(Areas.PE, address, length, byte_page)
            elif s7_address[0] == 'Q':
                self.__set_byte(Areas.PA, address, length, byte_page)
            elif s7_address[0] == 'M':
                self.__set_byte(Areas.MK, address, length, byte_page)

    def get_int(self, s7_address, length):
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'W':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                return self.__get_int(Areas.PE, address, length)
            elif s7_address[0] == 'Q':
                return self.__get_int(Areas.PA, address, length)
            elif s7_address[0] == 'M':
                return self.__get_int(Areas.MK, address, length)
        return 0

    def set_int(self, s7_address, length, int_page) -> None:
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'W':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                self.__set_int(Areas.PE, address, length, int_page)
            elif s7_address[0] == 'Q':
                self.__set_int(Areas.PA, address, length, int_page)
            elif s7_address[0] == 'M':
                self.__set_int(Areas.MK, address, length, int_page)

    def __get_byte(self, area, address, length):
        try:
            result = self.__plc.read_area(area, 0, address, length)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed
        byte_list = []
        for index in range(0, length):
            byte_list.append(get_byte(result, index))
        return byte_list

    def __set_byte(self, area, address, length, data):
        try:
            result = self.__plc.read_area(area, 0, address, length)
            for index in range(0, length):
                set_byte(result, index, data[index])
            self.__plc.write_area(area, 0, address, result)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed

    def __get_int(self, area, address, length):
        try:
            result = self.__plc.read_area(area, 0, address, length * 2)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed
        int_list = []
        for index in range(0, length):
            int_list.append(get_int(result, index * 2))
        return int_list

    def __set_int(self, area, address, length, data):
        try:
            result = self.__plc.read_area(area, 0, address, length * 2)
            for index in range(0, length):
                set_int(result, index * 2, data[index])
            self.__plc.write_area(area, 0, address, result)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed

    def __connect(self):
        if not self.__connected:
            if self.__ip == '':
                self.__connected = False
                raise S7ConnectFailed
            try:
                self.__plc.connect(self.__ip, self.__rack, self.__slot)
            except Snap7Exception:
                self.__connected = False
                raise S7ConnectFailed
            self.__connected = True
        return True


if __name__ == '__main__':
    # plc = PLC_Connect('172.16.65.1', 0, 2)
    plc = PLC_Connect('192.168.90.2', 0, 1)

    print(plc.get_int('IW64', 4))
