from _plc_data.plc_data import PLC_Address, PLC_data


# noinspection PyPep8Naming,SpellCheckingInspection
class Szalag4v1_Address(PLC_Address):
    S1 = 'I0.0'
    S2 = 'I0.1'
    S3 = 'I0.3'
    S4 = 'I0.4'
    START1 = 'I0.5'
    START2 = 'I0.6'
    STOP = 'I0.7'

    M1 = 'Q0.0'
    M2_BAL = 'Q0.1'
    M2_JOBB = 'Q0.2'
    M3 = 'Q0.3'
    M4 = 'Q0.4'
    UZEM1 = 'Q0.5'
    UZEM2 = 'Q0.6'
    HIBA = 'Q0.7'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))


# noinspection PyPep8Naming,SpellCheckingInspection
class Szalag4v1_data(PLC_data):
    __s1_old = False
    __s2_old = False
    __s3_old = False
    __s4_old = False
    __start1_old = False
    __start2_old = False
    __stop_old = False

    __m1_old = False
    __m2_bal_old = False
    __m2_jobb_old = False
    __m3_old = False
    __m4_old = False
    __uzem1_old = False
    __uzem2_old = False
    __hiba_old = False

    def __init__(self, ip, rack, slot) -> None:
        super().__init__(Szalag4v1_Address(), ip, rack, slot)

        self.__s1 = False
        self.__s2 = False
        self.__s3 = False
        self.__s4 = False
        self.__start1 = False
        self.__start2 = False
        self.__stop = False

        self.__m1 = False
        self.__m2_bal = False
        self.__m2_jobb = False
        self.__m3 = False
        self.__m4 = False
        self.__uzem1 = False
        self.__uzem2 = False
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
    def m2_bal(self):
        return self.__m2_bal

    @property
    def m2_jobb(self):
        return self.__m2_jobb

    @property
    def m3(self):
        return self.__m3

    @property
    def m4(self):
        return self.__m4

    @property
    def uzem1(self):
        return self.__uzem1

    @property
    def uzem2(self):
        return self.__uzem2

    @property
    def hiba(self):
        return self.__hiba

    def read_data(self) -> None:
        super().read_data()

        self.__s1 = self.get_bit_tag_page(Szalag4v1_Address.S1)
        self.__s2 = self.get_bit_tag_page(Szalag4v1_Address.S2)
        self.__s3 = self.get_bit_tag_page(Szalag4v1_Address.S3)
        self.__s4 = self.get_bit_tag_page(Szalag4v1_Address.S4)
        self.__start1 = self.get_bit_tag_page(Szalag4v1_Address.START1)
        self.__start2 = self.get_bit_tag_page(Szalag4v1_Address.START2)
        self.__stop = self.get_bit_tag_page(Szalag4v1_Address.STOP)

        self.__m1 = self.get_bit_tag_page(Szalag4v1_Address.M1)
        self.__m2_bal = self.get_bit_tag_page(Szalag4v1_Address.M2_BAL)
        self.__m2_jobb = self.get_bit_tag_page(Szalag4v1_Address.M2_JOBB)
        self.__m3 = self.get_bit_tag_page(Szalag4v1_Address.M3)
        self.__m4 = self.get_bit_tag_page(Szalag4v1_Address.M4)
        self.__uzem1 = self.get_bit_tag_page(Szalag4v1_Address.UZEM1)
        self.__uzem2 = self.get_bit_tag_page(Szalag4v1_Address.UZEM2)
        self.__hiba = self.get_bit_tag_page(Szalag4v1_Address.HIBA)

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

    def m2_bal_is_changed(self):
        if self.__m2_bal != self.__m2_bal_old:
            self.__m2_bal_old = self.__m2_bal
            return True
        return False

    def m2_jobb_is_changed(self):
        if self.__m2_jobb != self.__m2_jobb_old:
            self.__m2_jobb_old = self.__m2_jobb
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

    def uzem1_is_changed(self):
        if self.__uzem1 != self.__uzem1_old:
            self.__uzem1_old = self.__uzem1
            return True
        return False

    def uzem2_is_changed(self):
        if self.__uzem2 != self.__uzem2_old:
            self.__uzem2_old = self.__uzem2
            return True
        return False

    def hiba_is_changed(self):
        if self.__hiba != self.__hiba_old:
            self.__hiba_old = self.__hiba
            return True
        return False
