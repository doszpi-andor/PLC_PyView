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

    @staticmethod
    def byte_index(bit_address) -> int:
        return int(bit_address[1])

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
    read_pii = None
    read_piq = None

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
        except S7ConnectFailed:
            self.read_pii = None
            self.read_piq = None

    def write_data(self):
        pass

    @staticmethod
    def get_page_bit(page, s7_bit_address):
        return bool(page[PLC_Address.byte_index(s7_bit_address)] & (0x01 << PLC_Address.bit_index(s7_bit_address)))
