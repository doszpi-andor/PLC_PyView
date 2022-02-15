from _config.plc_config_read import PLC_Config
from _plc_data.plc_data import PLC_Address, PLC_data


# noinspection SpellCheckingInspection
class Szalag1v0_Address(PLC_Address):
    IP_LIST, RACK, SLOT = PLC_Config.read_plc_config('_config/config.xml')
    DEFAULT_IP = PLC_Config.read_plc_default_ip('_config/default.xml')

    S1 = 'I0.0'
    S2 = 'I0.1'
    NYUGTA = 'I0.5'
    START = 'I0.6'
    STOP = 'I0.7'
    M1 = 'Q0.0'
    M2 = 'Q0.1'
    UZEM = 'Q0.5'
    HIBA1 = 'Q4.0'
    HIBA2 = 'Q4.1'

    READ_BYTES_ADDRESS = ('IB0', 'QB0', 'QB4')


# noinspection SpellCheckingInspection
class Szalag1v0_data(PLC_data):

    __s1_old = False
    __s2_old = False
    __nyugta_old = False
    __start_old = False
    __stop_old = False
    __m1_old = False
    __m2_old = False
    __uzem_old = False
    __hiba1_old = False
    __hiba2_old = False

    def __init__(self, ip, rack, slot) -> None:
        super().__init__(Szalag1v0_Address(), ip, rack, slot)
        self.s1 = False
        self.s2 = False
        self.nyugta = False
        self.start = False
        self.stop = False
        self.m1 = False
        self.m2 = False
        self.uzem = False
        self.hiba1 = False
        self.hiba2 = False

    def read_data(self):
        super().read_data()

        self.s1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v0_Address.S1)][PLC_Address.bit_index(Szalag1v0_Address.S1)]
        self.s2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v0_Address.S2)][PLC_Address.bit_index(Szalag1v0_Address.S2)]
        self.nyugta = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v0_Address.NYUGTA)][PLC_Address.bit_index(Szalag1v0_Address.NYUGTA)]
        self.start = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v0_Address.START)][PLC_Address.bit_index(Szalag1v0_Address.START)]
        self.stop = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v0_Address.STOP)][PLC_Address.bit_index(Szalag1v0_Address.STOP)]

        self.m1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v0_Address.M1)][PLC_Address.bit_index(Szalag1v0_Address.M1)]
        self.m2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v0_Address.M2)][PLC_Address.bit_index(Szalag1v0_Address.M2)]
        self.uzem = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v0_Address.UZEM)][PLC_Address.bit_index(Szalag1v0_Address.UZEM)]
        self.hiba1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v0_Address.HIBA1)][PLC_Address.bit_index(Szalag1v0_Address.HIBA1)]
        self.hiba2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v0_Address.HIBA2)][PLC_Address.bit_index(Szalag1v0_Address.HIBA2)]

    def s1_is_changed(self):
        if self.s1 != self.__s1_old:
            self.__s1_old = self.s1
            return True
        return False

    def s2_is_changed(self):
        if self.s2 != self.__s2_old:
            self.__s2_old = self.s2
            return True
        return False

    def start_is_changed(self):
        if self.start != self.__start_old:
            self.__start_old = self.start
            return True
        return False

    def stop_is_changed(self):
        if self.stop != self.__stop_old:
            self.__stop_old = self.stop
            return True
        return False

    def nyugta_is_changed(self):
        if self.nyugta != self.__nyugta_old:
            self.__nyugta_old = self.nyugta
            return True
        return False

    def m1_is_change(self):
        if self.m1 != self.__m1_old:
            self.__m1_old = self.m1
            return True
        return False

    def m2_is_change(self):
        if self.m2 != self.__m2_old:
            self.__m2_old = self.m2
            return True
        return False

    def uzem_is_change(self):
        if self.uzem != self.__uzem_old:
            self.__uzem_old = self.uzem
            return True
        return False

    def hiba1_is_change(self):
        if self.hiba1 != self.__hiba1_old:
            self.__hiba1_old = self.hiba1
            return True
        return False

    def hiba2_is_change(self):
        if self.hiba2 != self.__hiba2_old:
            self.__hiba2_old = self.hiba2
            return True
        return False
