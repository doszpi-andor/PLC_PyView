from _snap7.snap7_connect import PLC_Connect, S7ConnectFailed


class PLC_Address:
    """
    PLC Address
    :var str IP: PLC ipv4 address (string)
    :var int RACK: PLC rack number
    :var int SLOT: PLC slot number
    :var list BYTES_ADDRESS: PLC read bytes
    """
    IP, RACK, SLOT = None, None, None

    BYTES_ADDRESS = ()
    WORDS_ADDRESS = ()

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


class PLC_data:
    """
    :param PLC_Address plc_address:
    :var dict read_byte_data:
    """
    read_byte_data = {}
    read_word_data = {}

    write_byte_data = {}

    def __init__(self, plc_address):
        self.__plc_address = plc_address
        self.__plc_connect = PLC_Connect(plc_address.IP, plc_address.RACK, plc_address.SLOT)

    @property
    def connected(self) -> bool:
        """
        PLC Snap7 connected
        :return: PLC Snap7 connected state
        """
        return self.__plc_connect.connected

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
            for byte_address in self.__plc_address.BYTES_ADDRESS:
                self.read_byte_data[byte_address] = self.__plc_connect.get_bits(byte_address)
            for word_address in self.__plc_address.WORDS_ADDRESS:
                self.read_word_data[word_address] = self.__plc_connect.get_int(word_address)
        except S7ConnectFailed:
            for byte_address in self.__plc_address.BYTES_ADDRESS:
                self.read_byte_data[byte_address] = [False, False, False, False, False, False, False, False]
            for word_address in self.__plc_address.WORDS_ADDRESS:
                self.read_word_data[word_address] = 0

    def write_data(self):
        try:
            for byte_address in self.__plc_address.BYTES_ADDRESS:
                self.__plc_connect.set_bits(byte_address, self.write_byte_data[byte_address])
        except S7ConnectFailed:
            pass
