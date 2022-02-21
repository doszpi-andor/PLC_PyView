from _snap7.snap7_connect import PLC_Connect, S7ConnectFailed


# noinspection PyPep8Naming
class PLC_Address:
    """
    PLC Address
    :var int RACK: PLC rack number
    :var int SLOT: PLC slot number
    :var list READ_BYTES_ADDRESS: PLC read bytes
    :var list READ_WORDS_ADDRESS: PLC read words
    :var list WRITE_BYTES_ADDRESS: PLC write bytes
    :var list WRITE_WORDS_ADDRESS: PLC write words
    """

    READ_BYTES_ADDRESS = ()
    READ_WORDS_ADDRESS = ()

    WRITE_BYTES_ADDRESS = ()
    WRITE_WORDS_ADDRESS = ()

    @staticmethod
    def byte_address(bit_address) -> str:
        """
        PLC byte address create
        :param str bit_address: PLC bit address
        :return: PLC byte address
        """
        return bit_address[0] + 'B' + bit_address[1]

    @staticmethod
    def bit_index(bit_address) -> int:
        """
        PLC bit index create
        :param str bit_address: PLC but address
        :return: PLC bit index
        """
        return int(bit_address[3])


# noinspection PyPep8Naming
class PLC_data:
    """
    PLC data
    :param PLC_Address plc_address: PLC Address class
    :param str ip:  PLC ip address
    :var dict read_byte_data: read PLC data bytes
    :var dict read_word_data: read PLC data words
    :var dict write_byte_data: write PLC data bytes
    :var dict write_word_data: write PLC data words
    """
    read_byte_data = {}
    read_word_data = {}

    write_byte_data = {}
    write_word_data = {}

    def __init__(self, plc_address, ip, rack, slot):
        self.__plc_address = plc_address
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
            for byte_address in self.__plc_address.READ_BYTES_ADDRESS:
                self.read_byte_data[byte_address] = self.__plc_connect.get_bits(byte_address)
            for word_address in self.__plc_address.READ_WORDS_ADDRESS:
                self.read_word_data[word_address] = self.__plc_connect.get_int(word_address)
        except S7ConnectFailed:
            for byte_address in self.__plc_address.READ_BYTES_ADDRESS:
                self.read_byte_data[byte_address] = [False, False, False, False, False, False, False, False]
            for word_address in self.__plc_address.READ_WORDS_ADDRESS:
                self.read_word_data[word_address] = 0

    def write_data(self):
        """
            Write PLC data bytes
            Data to read_byte_data
        """
        try:
            for byte_address in self.__plc_address.WRITE_BYTES_ADDRESS:
                self.__plc_connect.set_bits(byte_address, self.write_byte_data[byte_address])
            for word_address in self.__plc_address.WRITE_WORDS_ADDRESS:
                self.__plc_connect.set_int(word_address, self.write_word_data[word_address])
        except S7ConnectFailed:
            pass
