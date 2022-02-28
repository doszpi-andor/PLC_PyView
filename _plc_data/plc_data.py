from snap7.util import get_bool

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

    INPUT_START_BYTE_ADDRESS = ''
    INPUT_PROCESS_IMAGE_SIZE = 0

    OUTPUT_START_BYTE_ADDRESS = ''
    OUTPUT_PROCESS_IMAGE_SIZE = 0

    @staticmethod
    def byte_address(bit_address) -> str:
        """
        PLC byte address create
        :param str bit_address: PLC bit address
        :return: PLC byte address
        """
        return bit_address[0] + 'B' + bit_address[1]

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
    input_process_image = None
    output_process_image = None

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
            if self.__plc_address.INPUT_START_BYTE_ADDRESS != '' and self.__plc_address.INPUT_PROCESS_IMAGE_SIZE > 0:
                self.input_process_image = self.__plc_connect.get_bytes(self.__plc_address.INPUT_START_BYTE_ADDRESS,
                                                                        self.__plc_address.INPUT_PROCESS_IMAGE_SIZE)
            if self.__plc_address.OUTPUT_START_BYTE_ADDRESS != '' and self.__plc_address.OUTPUT_PROCESS_IMAGE_SIZE > 0:
                self.output_process_image = self.__plc_connect.get_bytes(self.__plc_address.OUTPUT_START_BYTE_ADDRESS,
                                                                         self.__plc_address.OUTPUT_PROCESS_IMAGE_SIZE)
        except S7ConnectFailed:
            self.input_process_image = None
            self.output_process_image = None

    def write_data(self):
        pass
