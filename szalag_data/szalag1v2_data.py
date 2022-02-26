from _plc_data.plc_data import PLC_Address, PLC_data


class Szalag1v2_Address(PLC_Address):

    S1 = 'I0.0'
    S2 = 'I0.1'
    S3 = 'I0.2'
    START1 = 'I0.4'
    STOP1 = 'I0.5'
    START2 = 'I0.6'
    STOP2 = 'I0.7'
    M1 = 'Q0.0'
    M2 = 'Q0.1'
    M3 = 'Q0.2'
    UZEM1 = 'Q0.3'
    UZEM2 = 'Q0.4'
    HIBA1 = 'Q0.5'
    HIBA2 = 'Q4.0'
    HIBA3 = 'Q4.1'

    READ_BYTES_ADDRESS = ('IB0', 'QB0', 'QB4')


class Szalag1v2_data(PLC_data):

    __s1_old = False
    __s2_old = False
    __s3_old = False
    __start1_old = False
    __stop1_old = False
    __start2_old = False
    __stop2_old = False
    __m1_old = False
    __m2_old = False
    __m3_old = False
    __uzem1_old = False
    __uzem2_old = False
    __hiba1_old = False
    __hiba2_old = False
    __hiba3_old = False

    def __init__(self, ip, rack, slot) -> None:
        super().__init__(Szalag1v2_Address(), ip, rack, slot)
        self.s1 = False
        self.s2 = False
        self.s3 = False
        self.start1 = False
        self.stop1 = False
        self.start2 = False
        self.stop2 = False
        self.m1 = False
        self.m2 = False
        self.m3 = False
        self.uzem1 = False
        self.uzem2 = False
        self.hiba1 = False
        self.hiba2 = False
        self.hiba3 = False

    def read_data(self):
        super().read_data()

        self.s1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.S1)][PLC_Address.bit_index(Szalag1v2_Address.S1)]
        self.s2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.S2)][PLC_Address.bit_index(Szalag1v2_Address.S2)]
        self.s3 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.S3)][PLC_Address.bit_index(Szalag1v2_Address.S3)]
        self.start1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.START1)][PLC_Address.bit_index(Szalag1v2_Address.START1)]
        self.stop1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.STOP1)][PLC_Address.bit_index(Szalag1v2_Address.STOP1)]
        self.start2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.START2)][PLC_Address.bit_index(Szalag1v2_Address.START2)]
        self.stop2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.STOP2)][PLC_Address.bit_index(Szalag1v2_Address.STOP2)]

        self.m1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.M1)][PLC_Address.bit_index(Szalag1v2_Address.M1)]
        self.m2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.M2)][PLC_Address.bit_index(Szalag1v2_Address.M2)]
        self.m3 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.M3)][PLC_Address.bit_index(Szalag1v2_Address.M3)]
        self.uzem1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.UZEM1)][PLC_Address.bit_index(Szalag1v2_Address.UZEM1)]
        self.uzem2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.UZEM2)][PLC_Address.bit_index(Szalag1v2_Address.UZEM2)]
        self.hiba1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.HIBA1)][PLC_Address.bit_index(Szalag1v2_Address.HIBA1)]
        self.hiba2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.HIBA2)][PLC_Address.bit_index(Szalag1v2_Address.HIBA2)]
        self.hiba3 = self.read_byte_data[
            PLC_Address.byte_address(Szalag1v2_Address.HIBA3)][PLC_Address.bit_index(Szalag1v2_Address.HIBA3)]

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

    def s3_is_changed(self):
        if self.s3 != self.__s3_old:
            self.__s3_old = self.s3
            return True
        return False

    def start1_is_changed(self):
        if self.start1 != self.__start1_old:
            self.__start1_old = self.start1
            return True
        return False

    def stop1_is_changed(self):
        if self.stop1 != self.__stop1_old:
            self.__stop1_old = self.stop1
            return True
        return False

    def start2_is_changed(self):
        if self.start2 != self.__start2_old:
            self.__start2_old = self.start2
            return True
        return False

    def stop2_is_changed(self):
        if self.stop2 != self.__stop2_old:
            self.__stop2_old = self.stop2
            return True
        return False

    def m1_is_changed(self):
        if self.m1 != self.__m1_old:
            self.__m1_old = self.m1
            return True
        return False

    def m2_is_changed(self):
        if self.m2 != self.__m2_old:
            self.__m2_old = self.m2
            return True
        return False

    def m3_is_changed(self):
        if self.m3 != self.__m3_old:
            self.__m3_old = self.m3
            return True
        return False

    def uzem1_is_changed(self):
        if self.uzem1 != self.__uzem1_old:
            self.__uzem1_old = self.uzem1
            return True
        return False

    def uzem2_is_changed(self):
        if self.uzem2 != self.__uzem2_old:
            self.__uzem2_old = self.uzem2
            return True
        return False

    def hiba1_is_changed(self):
        if self.hiba1 != self.__hiba1_old:
            self.__hiba1_old = self.hiba1
            return True
        return False

    def hiba2_is_changed(self):
        if self.hiba2 != self.__hiba2_old:
            self.__hiba2_old = self.hiba2
            return True
        return False

    def hiba3_is_changed(self):
        if self.hiba3 != self.__hiba3_old:
            self.__hiba3_old = self.hiba3
            return True
        return False
