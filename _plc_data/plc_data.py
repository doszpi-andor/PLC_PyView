from _snap7.snap7_connect import PLC_Connect, S7ConnectFailed


# noinspection PyPep8Naming
class PLC_Address:
    """
    PLC Address
    """

    READ_PII_ADDRESS = None
    READ_PII_SIZE = None

    READ_PIQ_ADDRESS = None
    READ_PIQ_SIZE = None

    READ_AI_ADDRESS = None
    READ_AI_SIZE = None

    def byte_index(self, bit_address) -> int:
        byte_address, bit_index = (int(x) for x in bit_address[1:].split(sep='.'))
        return byte_address - int(self.READ_PIQ_ADDRESS[2:])

    @staticmethod
    def bit_index(bit_address) -> int:
        """
        PLC bit index create
        :param str bit_address: PLC but address
        :return: PLC bit index
        """
        byte_address, bit_index = (int(x) for x in bit_address[1:].split(sep='.'))
        return bit_index

    def word_index(self, word_address):
        return (int(word_address[2:]) - int(self.READ_AI_ADDRESS[2:])) // 2


# noinspection PyPep8Naming
class PLC_data:
    read_pii = None
    read_piq = None
    read_ai = None

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
            if self.__plc_address.READ_PII_ADDRESS is not None and self.__plc_address.READ_PII_SIZE is not None:
                self.read_pii = self.__plc_connect.get_bytes(self.__plc_address.READ_PII_ADDRESS,
                                                             self.__plc_address.READ_PII_SIZE)
            if self.__plc_address.READ_PIQ_ADDRESS is not None and self.__plc_address.READ_PIQ_SIZE is not None:
                self.read_piq = self.__plc_connect.get_bytes(self.__plc_address.READ_PIQ_ADDRESS,
                                                             self.__plc_address.READ_PIQ_SIZE)
            if self.__plc_address.READ_AI_ADDRESS is not None and self.__plc_address.READ_AI_SIZE is not None:
                self.read_ai = self.__plc_connect.get_ints(self.__plc_address.READ_AI_ADDRESS,
                                                           self.__plc_address.READ_AI_SIZE)
        except S7ConnectFailed:
            self.read_pii = None
            self.read_piq = None
            self.read_ai = None

    def write_data(self):
        pass

    def get_page_bit(self, page, bit_address):
        return bool(page[self.__plc_address.byte_index(bit_address)] &
                    (0x01 << self.__plc_address.bit_index(bit_address)))

    def get_page_int(self, page, word_address):
        return page[self.__plc_address.word_index(word_address)]
