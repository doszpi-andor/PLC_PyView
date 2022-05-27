from _plc_data.plc_data import PLC_Address, PLC_data


class Szalag3_Address(PLC_Address):

    S1 = 'I0.0'
    S2 = 'I0.1'
    S3 = 'I0.2'
    S4 = 'I0.3'
    S5 = 'I0.4'
    KP = 'I0.5'
    START = 'I0.6'
    STOP = 'I0.7'

    M1 = 'Q0.0'
    M2 = 'Q0.1'
    M3 = 'Q0.2'
    M4 = 'Q0.3'
    M5 = 'Q0.4'
    UZEM = 'Q0.5'
    SZALAG_HIBA = 'Q0.6'
    KOCSI_HOBA = 'Q0.7'
    SILO1_URES = 'Q1.0'
    SILO2_URES = 'Q1.1'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))

    KS = 'IW64'

    READ_WORDS_TAG_ADDRESS = (('IW64', 1),)

    KS_RANGE = 25000


class Szalag3_data(PLC_data):

    __s1_old = False
    __s2_old = False
    __s3_old = False
    __s4_old = False
    __s5_old = False
    __kp_old = False
    __start_old = False
    __stop_old = False

    __m1_old = False
    __m2_old = False
    __m3_old = False
    __m4_old = False
    __m5_old = False
    __uzem_old = False
    __szalag_hiba_old = False
    __kocsi_hiba_old = False
    __silo1_ures_old = False
    __silo2_ures_old = False

    __ks_old = 0

    def __init__(self, ip, rack, slot) -> None:
        super().__init__(Szalag3_Address(), ip, rack, slot)

        self.__s1 = False
        self.__s2 = False
        self.__s3 = False
        self.__s4 = False
        self.__s5 = False
        self.__kp = False
        self.__start = False
        self.__stop = False

        self.__m1 = False
        self.__m2 = False
        self.__m3 = False
        self.__m4 = False
        self.__m5 = False
        self.__uzem = False
        self.__szalag_hiba = False
        self.__kocsi_hiba = False
        self.__silo1_ures = False
        self.__silo2_ures = False

        self.__ks = 0

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
    def s5(self):
        return self.__s5

    @property
    def kp(self):
        return self.__kp

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
    def m5(self):
        return self.__m5

    @property
    def uzem(self):
        return self.__uzem

    @property
    def szalag_hiba(self):
        return self.__szalag_hiba

    @property
    def kocsi_hiba(self):
        return self.__kocsi_hiba

    @property
    def silo1_ures(self):
        return self.__silo1_ures

    @property
    def silo2_ures(self):
        return self.__silo2_ures

    @property
    def ks(self):
        return self.__ks

    @property
    def ks_percent(self):
        return int(self.__ks / Szalag3_Address.KS_RANGE * 100)

    def read_data(self) -> None:
        super().read_data()

        self.__s1 = self.get_bit_tag_page(Szalag3_Address.S1)
        self.__s2 = self.get_bit_tag_page(Szalag3_Address.S2)
        self.__s3 = self.get_bit_tag_page(Szalag3_Address.S3)
        self.__s4 = self.get_bit_tag_page(Szalag3_Address.S4)
        self.__s5 = self.get_bit_tag_page(Szalag3_Address.S5)
        self.__kp = self.get_bit_tag_page(Szalag3_Address.KP)
        self.__start = self.get_bit_tag_page(Szalag3_Address.START)
        self.__stop = self.get_bit_tag_page(Szalag3_Address.STOP)

        self.__m1 = self.get_bit_tag_page(Szalag3_Address.M1)
        self.__m2 = self.get_bit_tag_page(Szalag3_Address.M2)
        self.__m3 = self.get_bit_tag_page(Szalag3_Address.M3)
        self.__m4 = self.get_bit_tag_page(Szalag3_Address.M4)
        self.__m5 = self.get_bit_tag_page(Szalag3_Address.M5)
        self.__uzem = self.get_bit_tag_page(Szalag3_Address.UZEM)
        self.__szalag_hiba = self.get_bit_tag_page(Szalag3_Address.SZALAG_HIBA)
        self.__kocsi_hiba = self.get_bit_tag_page(Szalag3_Address.KOCSI_HOBA)
        self.__silo1_ures = self.get_bit_tag_page(Szalag3_Address.SILO1_URES)
        self.__silo2_ures = self.get_bit_tag_page(Szalag3_Address.SILO2_URES)

        self.__ks = self.get_int_tag_page(Szalag3_Address.KS)

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

    def s5_is_changed(self):
        if self.__s5 != self.__s5_old:
            self.__s5_old = self.__s5
            return True
        return False

    def kp_is_changed(self):
        if self.__kp != self.__kp_old:
            self.__kp_old = self.__kp
            return True
        return False

    def start_is_changed(self):
        if self.__start != self.__start_old:
            self.__start_old = self.__start
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

    def m5_is_changed(self):
        if self.__m5 != self.__m5_old:
            self.__m5_old = self.__m5
            return True
        return False

    def uzem_is_changed(self):
        if self.__uzem != self.__uzem_old:
            self.__uzem_old = self.__uzem
            return True
        return False

    def szalag_hiba_is_changed(self):
        if self.__szalag_hiba != self.__szalag_hiba_old:
            self.__szalag_hiba_old = self.__szalag_hiba
            return True
        return False

    def kocsi_hiba_is_changed(self):
        if self.__kocsi_hiba != self.__kocsi_hiba_old:
            self.__kocsi_hiba_old = self.__kocsi_hiba
            return True
        return False

    def silo1_ures_is_changed(self):
        if self.__silo1_ures != self.__silo1_ures_old:
            self.__silo1_ures_old = self.__silo1_ures
            return True
        return False

    def silo2_ures_is_changed(self):
        if self.__silo2_ures != self.__silo2_ures_old:
            self.__silo2_ures_old = self.__silo2_ures
            return True
        return False

    def ks_is_changed(self, threshold=0):
        if self.__ks < self.__ks_old - threshold // 2 or \
                self.__ks > self.__ks_old + threshold // 2:
            self.__ks_old = self.__ks
            return True
        return False
