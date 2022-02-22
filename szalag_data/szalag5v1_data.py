from _plc_data.plc_data import PLC_Address, PLC_data


class Szalag5v1_Address(PLC_Address):

    S1 = 'I0.0'
    S2 = 'I0.1'
    S3 = 'I0.2'
    S4 = 'I0.3'
    START1 = 'I0.5'
    START2 = 'I0.6'
    STOP = 'I0.7'

    M1 = 'Q0.0'
    M2 = 'Q0.1'
    M3 = 'Q0.2'
    M4 = 'Q0.3'
    UZEM = 'Q4.0'
    HIBA = 'Q4.1'

    READ_BYTES_ADDRESS = ('IB0', 'QB0', 'QB4')


class Szalag5v1_data(PLC_data):

    __s1_old = False
    __s2_old = False
    __s3_old = False
    __s4_old = False
    __start1_old = False
    __start2_old = False
    __stop_old = False

    __m1_old = False
    __m2_old = False
    __m3_old = False
    __m4_old = False
    __uzem_old = False
    __hiba_old = False

    def __init__(self, ip, rack, slot) -> None:
        super().__init__(Szalag5v1_Address(), ip, rack, slot)

        self.__s1 = False
        self.__s2 = False
        self.__s3 = False
        self.__s4 = False
        self.__start1 = False
        self.__start2 = False
        self.__stop = False

        self.__m1 = False
        self.__m2 = False
        self.__m3 = False
        self.__m4 = False
        self.__uzem = False
        self.__hiba = False

    @property
    def s1(self):
        return self.__s1

    @property
    def s2(self):
        return self.__s2

    @property
    def s3(self):
        return self.__s3

    @property
    def s4(self):
        return self.__s4

    @property
    def start1(self):
        return self.__start1

    @property
    def start2(self):
        return self.__start2

    @property
    def stop(self):
        return self.__stop

    @property
    def m1(self):
        return self.__m1

    @property
    def m2(self):
        return self.__m2

    @property
    def m3(self):
        return self.__m3

    @property
    def m4(self):
        return self.__m4

    @property
    def uzem(self):
        return self.__uzem

    @property
    def hiba(self):
        return self.__hiba

    def read_data(self) -> None:
        super().read_data()

        self.__s1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.S1)][PLC_Address.bit_index(Szalag5v1_Address.S1)]
        self.__s2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.S2)][PLC_Address.bit_index(Szalag5v1_Address.S2)]
        self.__s3 = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.S3)][PLC_Address.bit_index(Szalag5v1_Address.S3)]
        self.__s4 = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.S4)][PLC_Address.bit_index(Szalag5v1_Address.S4)]
        self.__start1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.START1)][PLC_Address.bit_index(Szalag5v1_Address.START1)]
        self.__start2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.START2)][PLC_Address.bit_index(Szalag5v1_Address.START2)]
        self.__stop = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.STOP)][PLC_Address.bit_index(Szalag5v1_Address.STOP)]
        self.__m1 = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.M1)][PLC_Address.bit_index(Szalag5v1_Address.M1)]
        self.__m2 = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.M2)][PLC_Address.bit_index(Szalag5v1_Address.M2)]
        self.__m3 = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.M3)][PLC_Address.bit_index(Szalag5v1_Address.M3)]
        self.__m4 = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.M4)][PLC_Address.bit_index(Szalag5v1_Address.M4)]
        self.__uzem = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.UZEM)][PLC_Address.bit_index(Szalag5v1_Address.UZEM)]
        self.__hiba = self.read_byte_data[
            PLC_Address.byte_address(Szalag5v1_Address.HIBA)][PLC_Address.bit_index(Szalag5v1_Address.HIBA)]

    def s1_is_changed(self):
        if self.__s1 != self.__s1_old:
            self.__s1_old = self.__s1
            return True
        return False

    def s2_is_changed(self):
        if self.__s2 != self.__s2_old:
            self.__s2_old = self.__s2
            return True
        return False

    def s3_is_changed(self):
        if self.__s3 != self.__s3_old:
            self.__s3_old = self.__s3
            return True
        return False

    def s4_is_changed(self):
        if self.__s4 != self.__s4_old:
            self.__s4_old = self.__s4
            return True
        return False

    def start1_is_changed(self):
        if self.__start1 != self.__start1_old:
            self.__start1_old = self.__start1
            return True
        return False

    def start2_is_changed(self):
        if self.__start2 != self.__start2_old:
            self.__start2_old = self.__start2
            return True
        return False

    def stop_is_changed(self):
        if self.__stop != self.__stop_old:
            self.__stop_old = self.__stop
            return True
        return False

    def m1_is_changed(self):
        if self.__m1 != self.__m1_old:
            self.__m1_old = self.__m1
            return True
        return False

    def m2_is_changed(self):
        if self.__m2 != self.__m2_old:
            self.__m2_old = self.__m2
            return True
        return False

    def m3_is_changed(self):
        if self.__m3 != self.__m3_old:
            self.__m3_old = self.__m3
            return True
        return False

    def m4_is_changed(self):
        if self.__m4 != self.__m4_old:
            self.__m4_old = self.__m4
            return True
        return False

    def uzem_is_changed(self):
        if self.__uzem != self.__uzem_old:
            self.__uzem_old = self.__uzem
            return True
        return False

    def hiba_is_changed(self):
        if self.__hiba != self.__hiba_old:
            self.__hiba_old = self.__hiba
            return True
        return False
