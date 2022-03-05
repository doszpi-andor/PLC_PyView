from _snap7.snap7_connect import PLC_Connect, S7ConnectFailed


# noinspection PyPep8Naming
class PLC_Address:
    """
    PLC Address
    """

    READ_BYTES_ADDRESS = ()
    READ_WORDS_ADDRESS = ()

    @staticmethod
    def byte_address(bit_address) -> str:
        """
        PLC byte address create
        :param str bit_address: PLC bit address
        :return: PLC byte address
        """
        byte_index, bit_index = (int(x) for x in bit_address[1:].split(sep='.'))
        return bit_address[0] + 'B' + str(byte_index)

    @staticmethod
    def bit_index(bit_address) -> int:
        """
        PLC bit index create
        :param str bit_address: PLC but address
        :return: PLC bit index
        """
        byte_index, bit_index = (int(x) for x in bit_address[1:].split(sep='.'))
        return bit_index


# noinspection PyPep8Naming
class PLC_data:
    read_byte_data = {}
    read_word_data = {}

    def __init__(self, plc_address, ip, rack, slot):
        self.plc_address = plc_address
        self.__plc_connect = PLC_Connect(ip, rack, slot)

    @property
    def connected(self) -> bool:
        """
        PLC Snap7 connected
        :return: PLC Snap7 connected state
        """
        return self.__plc_connect.connected

    def reconnect(self, ip):
        """
        PLC reconnected
        :param ip: PLC ip address
        """
        self.__plc_connect.disconnect()
        self.__plc_connect.ip = ip

    def disconnect(self) -> None:
        """
        PLC Snap7 disconnected
        """
        self.__plc_connect.disconnect()

    def read_data(self) -> None:
        """
        Read PLC data bytes
        Data to read_byte_data
        """

        try:
            for byte_address, read_length in self.plc_address.READ_BYTES_ADDRESS:
                read_byte_page = self.__plc_connect.get_bytes(byte_address, read_length)
                byte_index = int(byte_address[2:])
                for index in range(0, read_length):
                    self.read_byte_data[byte_address[:2] + str(byte_index + index)] = read_byte_page[index]

            for word_address, read_length in self.plc_address.READ_WORDS_ADDRESS:
                read_word_page = self.__plc_connect.get_ints(word_address, read_length)
                word_index = int(word_address[2:])
                for index in range(0, read_length):
                    self.read_word_data[word_address[:2] + str(word_index + index * 2)] = read_word_page[index]

        except S7ConnectFailed:
            for byte_address, read_length in self.plc_address.READ_BYTES_ADDRESS:
                byte_index = int(byte_address[2:])
                for index in range(0, read_length):
                    self.read_byte_data[byte_address[:2] + str(byte_index + index)] = 0x00

            for word_address, read_length in self.plc_address.READ_WORDS_ADDRESS:
                word_index = int(word_address[2:])
                for index in range(0, read_length):
                    self.read_word_data[word_address[:2] + str(word_index + index * 2)] = 0

    def write_data(self):
        pass

    @staticmethod
    def get_bit_in_page(byte_page, bit_address):
        return bool(byte_page[PLC_Address.byte_address(bit_address)]
                    & (0x01 << PLC_Address.bit_index(bit_address)))

    @staticmethod
    def get_int_in_page(word_page, word_address):
        return word_page[word_address]
