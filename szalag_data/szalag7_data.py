from _plc_data.plc_data import PLC_Address, PLC_data


class Szalag7_Address(PLC_Address):

    START = 'I0.0'
    STOP = 'I0.1'

    M1 = 'Q0.0'
    M2 = 'Q0.1'
    M3 = 'Q0.2'
    M4 = 'Q0.3'
    UZEM = 'Q0.6'
    HIBA = 'Q0.7'

    S1 = 'I2.0'
    S2 = 'I2.1'
    S3 = 'I2.2'
    S4 = 'I2.3'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))
    WRITE_BYTES_TAG_ADDRESS = (('IB2', 1),)


class Szalag7_data(PLC_data):
    __start_old = False
    __stop__old = False

    __m1_old = False
    __m2_old = False
    __m3_old = False
    __m4_old = False
    __uzem_old = False
    __hiba_old = False

    def __init__(self, ip, rack, slot):
        super().__init__(Szalag7_Address(), ip, rack, slot)

        self.__start = False
        self.__stop = False

        self.__m1 = False
        self.__m2 = False
        self.__m3 = False
        self.__m4 = False
        self.__uzem = False
        self.__hiba = False

        self.__s1 = False
        self.__s2 = False
        self.__s3 = False
        self.__s4 = False

    @property
    def start(self):
        return self.__start

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

    @property
    def s1(self):
        return self.__s1

    @s1.setter
    def s1(self, data):
        if data in [True, False]:
            self.__s1 = data
        else:
            raise TypeError

    @property
    def s2(self):
        return self.__s2

    @s2.setter
    def s2(self, data):
        if data in [True, False]:
            self.__s2 = data
        else:
            raise TypeError

    @property
    def s3(self):
        return self.__s3

    @s3.setter
    def s3(self, data):
        if data in [True, False]:
            self.__s3 = data
        else:
            raise TypeError

    @property
    def s4(self):
        return self.__s4

    @s4.setter
    def s4(self, data):
        if data in [True, False]:
            self.__s4 = data
        else:
            raise TypeError

    def read_data(self) -> None:
        super().read_data()

        self.__start = self.get_bit_tag_page(Szalag7_Address.START)
        self.__stop = self.get_bit_tag_page(Szalag7_Address.STOP)

        self.__m1 = self.get_bit_tag_page(Szalag7_Address.M1)
        self.__m2 = self.get_bit_tag_page(Szalag7_Address.M2)
        self.__m3 = self.get_bit_tag_page(Szalag7_Address.M3)
        self.__m4 = self.get_bit_tag_page(Szalag7_Address.M4)
        self.__uzem = self.get_bit_tag_page(Szalag7_Address.UZEM)
        self.__hiba = self.get_bit_tag_page(Szalag7_Address.HIBA)

    def write_data(self):
        self.write_tag_page_clear()

        self.set_bit_tag_page(Szalag7_Address.S1, self.__s1)
        self.set_bit_tag_page(Szalag7_Address.S2, self.__s2)
        self.set_bit_tag_page(Szalag7_Address.S3, self.__s3)
        self.set_bit_tag_page(Szalag7_Address.S4, self.__s4)

        super().write_data()

    def start_is_changed(self):
        if self.__start != self.__start_old:
            self.__start_old = self.__start
            return True
        return False

    def stop_is_changed(self):
        if self.__stop != self.__stop__old:
            self.__stop__old = self.__stop
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
