from snap7.client import Client
from snap7.exceptions import Snap7Exception
from snap7.types import Areas, S7WLBit, S7WLByte, S7WLWord
from snap7.util import get_bool, set_bool, get_byte, set_byte, get_int, set_int


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

    def get_bit(self, s7_address) -> bool:
        # noinspection SpellCheckingInspection
        """
        Get bit (1 bit)
        :param str s7_address: Simatic Step 7 PLC address
        :return: return get bit
        """
        if len(s7_address) < 4 or s7_address[0] not in ('I', 'Q', 'M'):
            raise S7AddressException
        try:
            address, bit_index = (int(x) for x in s7_address[1:].split(sep='.'))
        except ValueError:
            raise S7AddressException
        if bit_index > 7:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                return self.__get_bit(Areas.PE, address, bit_index)
            elif s7_address[0] == 'Q':
                return self.__get_bit(Areas.PA, address, bit_index)
            elif s7_address[0] == 'M':
                return self.__get_bit(Areas.MK, address, bit_index)
        else:
            return False

    # noinspection SpellCheckingInspection
    def set_bit(self, s7_address, bit_value) -> None:
        """
        Set bit (1 bit)
        :param str s7_address: Simatic Step 7 PLC address
        :param bool bit_value: set bit value
        """
        if len(s7_address) < 4 or s7_address[0] not in ('I', 'Q', 'M'):
            raise S7AddressException
        try:
            address, bit_index = (int(x) for x in s7_address[1:].split(sep='.'))
        except ValueError:
            raise S7AddressException
        if bit_index > 7:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                self.__set_bit(Areas.PE, address, bit_index, bit_value)
            elif s7_address[0] == 'Q':
                self.__set_bit(Areas.PA, address, bit_index, bit_value)
            elif s7_address[0] == 'M':
                self.__set_bit(Areas.MK, address, bit_index, bit_value)

    # noinspection SpellCheckingInspection
    def get_bits(self, s7_address) -> list[bool]:
        """
        Get bits (8 bit)
        :param str s7_address: Simatic Step 7 PLC address
        :return: return get bits (bool list)
        """
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'B':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                return self.__get_bits(Areas.PE, address)
            elif s7_address[0] == 'Q':
                return self.__get_bits(Areas.PA, address)
            elif s7_address[0] == 'M':
                return self.__get_bits(Areas.MK, address)

    # noinspection SpellCheckingInspection
    def set_bits(self, s7_address, bits_value) -> None:
        """
        Set bits (8 bit)
        :param str s7_address: Simatic Step 7 PLC address
        :param list[bool] bits_value: set bits value (bool list)
        """
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'B':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                self.__set_bits(Areas.PE, address, bits_value)
            elif s7_address[0] == 'Q':
                self.__set_bits(Areas.PA, address, bits_value)
            elif s7_address[0] == 'M':
                self.__set_bits(Areas.MK, address, bits_value)

    # noinspection SpellCheckingInspection
    def get_byte(self, s7_address) -> int:
        """
        Get byte (1 byte)
        :param str s7_address: Simatic Step 7 PLC address
        :return: return get byte (hex)
        """
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'B':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                return self.__get_byte(Areas.PE, address)
            elif s7_address[0] == 'Q':
                return self.__get_byte(Areas.PA, address)
            elif s7_address[0] == 'M':
                return self.__get_byte(Areas.MK, address)
        else:
            return 0

    # noinspection SpellCheckingInspection
    def set_byte(self, s7_address, byte_value) -> None:
        """
        Set byte (1 byte)
        :param str s7_address: Simatic Step 7 PLC address
        :param int byte_value: set byte value (hex)
        """
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'B':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                self.__set_byte(Areas.PE, address, byte_value)
            elif s7_address[0] == 'Q':
                self.__set_byte(Areas.PA, address, byte_value)
            elif s7_address[0] == 'M':
                self.__set_byte(Areas.MK, address, byte_value)

    def get_bytes(self, s7_address, length):
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'B':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                return self.__get_bytes(Areas.PE, address, length)
            elif s7_address[0] == 'Q':
                return self.__get_bytes(Areas.PA, address, length)
            elif s7_address[0] == 'M':
                return self.__get_bytes(Areas.MK, address, length)
        else:
            return 0

    # noinspection SpellCheckingInspection
    def get_int(self, s7_address) -> int:
        """
        Get (signed) integer [2 byte]
        :param str s7_address: Simatic Step 7 PLC address
        :return: return get integer
        """
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'W':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                return self.__get_int(Areas.PE, address)
            elif s7_address[0] == 'Q':
                return self.__get_int(Areas.PA, address)
            elif s7_address[0] == 'M':
                return self.__get_int(Areas.MK, address)
        return 0

    # noinspection SpellCheckingInspection
    def set_int(self, s7_address, int_value) -> None:
        """
        Set (signed) integer [2 byte]
        :param str s7_address: Simatic Step 7 PLC address
        :param int int_value: set integer value
        """
        if len(s7_address) < 3 or s7_address[0] not in ('I', 'Q', 'M') or s7_address[1] != 'W':
            raise S7AddressException
        try:
            address = int(s7_address[2:])
        except ValueError:
            raise S7AddressException

        if self.__connect():
            if s7_address[0] == 'I':
                self.__set_int(Areas.PE, address, int_value)
            elif s7_address[0] == 'Q':
                self.__set_int(Areas.PA, address, int_value)
            elif s7_address[0] == 'M':
                self.__set_int(Areas.MK, address, int_value)

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

    def __get_bit(self, area, address, bit_index):
        try:
            result = self.__plc.read_area(area, 0, address, S7WLBit)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed
        return get_bool(result, 0, bit_index)

    def __set_bit(self, area, address, bit_index, bit_value):
        try:
            result = self.__plc.read_area(area, 0, address, S7WLBit)
            set_bool(result, 0, bit_index, bit_value)
            self.__plc.write_area(area, 0, address, result)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed

    def __get_bits(self, area, address):
        try:
            result = self.__plc.read_area(area, 0, address, S7WLBit)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed
        return [get_bool(result, 0, 0),
                get_bool(result, 0, 1),
                get_bool(result, 0, 2),
                get_bool(result, 0, 3),
                get_bool(result, 0, 4),
                get_bool(result, 0, 5),
                get_bool(result, 0, 6),
                get_bool(result, 0, 7)]

    def __set_bits(self, area, address, bits_value):
        if len(bits_value) != 8:
            raise ValueError
        try:
            result = self.__plc.read_area(area, 0, address, S7WLBit)
            set_bool(result, 0, 0, bits_value[0])
            set_bool(result, 0, 1, bits_value[1])
            set_bool(result, 0, 2, bits_value[2])
            set_bool(result, 0, 3, bits_value[3])
            set_bool(result, 0, 4, bits_value[4])
            set_bool(result, 0, 5, bits_value[5])
            set_bool(result, 0, 6, bits_value[6])
            set_bool(result, 0, 7, bits_value[7])
            self.__plc.write_area(area, 0, address, result)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed

    def __get_byte(self, area, address):
        try:
            result = self.__plc.read_area(area, 0, address, S7WLByte)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed
        return get_byte(result, 0)

    def __set_byte(self, area, address, byte_value):
        try:
            result = self.__plc.read_area(area, 0, address, S7WLByte)
            set_byte(result, 0, byte_value)
            self.__plc.write_area(area, 0, address, result)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed

    def __get_bytes(self, area, address, length):
        try:
            result = self.__plc.read_area(area, 0, address, length)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed
        return result

    def __get_int(self, area, address):
        try:
            result = self.__plc.read_area(area, 0, address, S7WLWord)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed
        return get_int(result, 0)

    def __set_int(self, area, address, int_value):
        try:
            result = self.__plc.read_area(area, 0, address, S7WLWord)
            set_int(result, 0, int_value)
            self.__plc.write_area(area, 0, address, result)
        except Snap7Exception:
            self.disconnect()
            raise S7ConnectFailed


if __name__ == '__main__':
    # plc = PLC_Connect('172.16.65.1', 0, 2)
    plc = PLC_Connect('172.17.1.1', 0, 1)

    byte_array = plc.get_bytes('QB0', 1024)
    print(get_bool(byte_array, 4, 0))

