from _snap7.snap7_connect import PLC_Connect, S7ConnectFailed


# noinspection PyPep8Naming
class PLC_Address:
    """
    PLC Address
    """
    READ_BYTES_TAG_ADDRESS = ()
    READ_WORDS_TAG_ADDRESS = ()

    READ_BYTES_DB_ADDRESS = ()
    READ_WORDS_DB_ADDRESS = ()

    WRITE_BYTES_TAG_ADDRESS = ()
    WRITE_WORDS_TAG_ADDRESS = ()

    WRITE_BYTES_DB_ADDRESS = ()
    WRITE_WORDS_DB_ADDRESS = ()

    @staticmethod
    def byte_tag_address(bit_address) -> str:
        """
        PLC byte address create
        :param str bit_address: PLC bit address
        :return: PLC byte address
        """
        byte_index, bit_index = (int(x) for x in bit_address[1:].split(sep='.'))
        return bit_address[0] + 'B' + str(byte_index)

    @staticmethod
    def byte_db_address(db_bit_address):
        db_address, byte_address, bit_address = db_bit_address.split(sep='.')
        return db_address + '.' + 'DBB' + byte_address[3:]

    @staticmethod
    def tag_bit_index(bit_address) -> int:
        """
        PLC bit index create
        :param str bit_address: PLC but address
        :return: PLC bit index
        """
        byte_index, bit_index = (int(x) for x in bit_address[1:].split(sep='.'))
        return bit_index

    @staticmethod
    def db_bit_index(db_bit_address):
        db_address, byte_address, bit_address = db_bit_address.split(sep='.')
        return int(bit_address)


# noinspection PyPep8Naming
class PLC_data:
    read_byte_tag = {}
    read_word_tag = {}

    read_byte_db = {}
    read_word_db = {}

    write_byte_tag = {}
    write_word_tag = {}

    write_byte_db = {}
    write_word_db = {}

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
            # read byte tag
            for byte_address, length in self.plc_address.READ_BYTES_TAG_ADDRESS:
                read_byte_page = self.__plc_connect.get_tag_byte(byte_address, length)
                byte_index = int(byte_address[2:])
                for index in range(0, length):
                    self.read_byte_tag[byte_address[:2] + str(byte_index + index)] = read_byte_page[index]

            # read byte db
            for db_byte_address, length in self.plc_address.READ_BYTES_DB_ADDRESS:
                read_byte_page = self.__plc_connect.get_db_byte(db_byte_address, length)
                db_address, byte_address = db_byte_address.split(sep='.')
                byte_index = int(byte_address[3:])
                for index in range(0, length):
                    self.read_byte_db[db_address + '.' + byte_address[:3] +
                                      str(byte_index + index)] = read_byte_page[index]

            # read word tag
            for word_address, length in self.plc_address.READ_WORDS_TAG_ADDRESS:
                read_word_page = self.__plc_connect.get_tag_int(word_address, length)
                word_index = int(word_address[2:])
                for index in range(0, length):
                    self.read_word_tag[word_address[:2] + str(word_index + index * 2)] = read_word_page[index]

            for db_word_address, length in self.plc_address.READ_WORDS_DB_ADDRESS:
                read_word_page = self.__plc_connect.get_db_int(db_word_address, length)
                db_address, word_address = db_word_address.split(sep='.')
                byte_index = int(word_address[3:])
                for index in range(0, length):
                    self.read_word_db[db_address + '.' + word_address[:3] +
                                      str(byte_index + index * 2)] = read_word_page[index]

        except S7ConnectFailed:
            for byte_address, length in self.plc_address.READ_BYTES_TAG_ADDRESS:
                byte_index = int(byte_address[2:])
                for index in range(0, length):
                    self.read_byte_tag[byte_address[:2] + str(byte_index + index)] = 0x00

            for db_byte_address, length in self.plc_address.READ_BYTES_DB_ADDRESS:
                db_address, byte_address = db_byte_address.split(sep='.')
                byte_index = int(byte_address[3:])
                for index in range(0, length):
                    self.read_byte_db[db_address + '.' + byte_address[:3] + str(byte_index + index)] = 0x00

            for word_address, length in self.plc_address.READ_WORDS_TAG_ADDRESS:
                word_index = int(word_address[2:])
                for index in range(0, length):
                    self.read_word_tag[word_address[:2] + str(word_index + index * 2)] = 0

            for db_word_address, length in self.plc_address.READ_WORDS_DB_ADDRESS:
                db_address, word_address = db_word_address.split(sep='.')
                byte_index = int(word_address[3:])
                for index in range(0, length):
                    self.read_word_db[db_address + '.' + word_address[:3] +
                                      str(byte_index + index * 2)] = 0

    def write_data(self):
        try:
            # writ byte tag
            for byte_address, length in self.plc_address.WRITE_BYTES_TAG_ADDRESS:
                byte_index = int(byte_address[2:])
                data = []
                for index in range(0, length):
                    data.append(self.write_byte_tag[byte_address[:2] + str(byte_index + index)])
                self.__plc_connect.set_tag_byte(byte_address, length, data)

            # writ byte db
            for db_byte_address, length in self.plc_address.WRITE_BYTES_DB_ADDRESS:
                db_address, byte_address = db_byte_address.split(sep='.')
                byte_index = int(byte_address[3:])
                data = []
                for index in range(0, length):
                    data.append(self.write_byte_db[db_address + '.' + byte_address[:3] + str(byte_index + index)])
                self.__plc_connect.set_db_byte(db_byte_address, length, data)

            # writ word tag
            for word_address, length in self.plc_address.WRITE_WORDS_TAG_ADDRESS:
                word_index = int(word_address[2:])
                data = []
                for index in range(0, length):
                    data.append(self.write_word_tag[word_address[:2] + str(word_index + index * 2)])
                self.__plc_connect.set_tag_int(word_address, length, data)

            # writ word db
            for db_word_address, length in self.plc_address.WRITE_WORDS_DB_ADDRESS:
                db_address, word_address = db_word_address.split(sep='.')
                word_index = int(word_address[3:])
                data = []
                for index in range(0, length):
                    data.append(self.write_word_db[db_address + '.' + word_address[:3] + str(word_index + index * 2)])
                self.__plc_connect.set_db_int(db_word_address, length, data)
        except S7ConnectFailed:
            pass

    def write_tag_page_clear(self):
        for byte_address, read_length in self.plc_address.WRITE_BYTES_TAG_ADDRESS:
            byte_index = int(byte_address[2:])
            for index in range(0, read_length):
                self.write_byte_tag[byte_address[:2] + str(byte_index + index)] = 0x00

    def write_db_page_clear(self):
        for db_byte_address, length in self.plc_address.WRITE_BYTES_DB_ADDRESS:
            db_address, byte_address = db_byte_address.split(sep='.')
            byte_index = int(byte_address[3:])
            for index in range(0, length):
                self.write_byte_db[db_address + '.' + byte_address[:3] + str(byte_index + index)] = 0x00

    def set_bit_tag_page(self, bit_address, data):
        old_data = self.write_byte_tag[PLC_Address.byte_tag_address(bit_address)]
        clear_mask = 255 - (0x01 << PLC_Address.tag_bit_index(bit_address))
        old_data = old_data & clear_mask
        if data:
            old_data = old_data + (0x01 << PLC_Address.tag_bit_index(bit_address))
        self.write_byte_tag[PLC_Address.byte_tag_address(bit_address)] = old_data

    def set_bit_db_page(self, db_bit_address, data):
        old_data = self.write_byte_db[PLC_Address.byte_db_address(db_bit_address)]
        clear_mask = 255 - (0x01 << PLC_Address.db_bit_index(db_bit_address))
        old_data = old_data & clear_mask
        if data:
            old_data = old_data + (0x01 << PLC_Address.db_bit_index(db_bit_address))
        self.write_byte_db[PLC_Address.byte_db_address(db_bit_address)] = old_data

    def set_int_tag_page(self, word_address, data):
        self.write_word_tag[word_address] = data

    def set_int_db_page(self, db_word_address, data):
        self.write_word_db[db_word_address] = data

    def get_bit_tag_page(self, bit_address):
        return bool(self.read_byte_tag[PLC_Address.byte_tag_address(bit_address)]
                    & (0x01 << PLC_Address.tag_bit_index(bit_address)))

    def get_bit_db_page(self, db_bit_address):
        return bool(self.read_byte_db[PLC_Address.byte_db_address(db_bit_address)]
                    & (0x01 << PLC_Address.db_bit_index(db_bit_address)))

    def get_int_tag_page(self, word_address):
        return self.read_word_tag[word_address]

    def get_int_db_page(self, db_word_address):
        return self.read_word_db[db_word_address]
