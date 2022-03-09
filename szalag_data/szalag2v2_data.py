
from _plc_data.plc_data import PLC_Address, PLC_data


class Szalag2v2_Address(PLC_Address):

    S1 = 'I0.0'
    S2 = 'I0.1'
    KP1 = 'I0.2'
    KP2 = 'I0.3'
    START = 'I0.6'
    STOP = 'I0.7'

    M1 = 'Q0.0'
    M2 = 'Q0.1'
    UZEM = 'Q4.0'
    HIBA = 'Q4.1'

    READ_BYTES_ADDRESS = (('IB0', 1), ('QB0', 5))

    KS = 'IW64'

    READ_WORDS_ADDRESS = (('IW64', 1), )

    KS_RANGE = 27648


# noinspection PyPep8Naming,SpellCheckingInspection
class Szalag2v2_data(PLC_data):

    __s1_old = False
    __s2_old = False
    __kp1_old = False
    __kp2_old = False
    __start_old = False
    __stop_old = False

    __m1_old = False
    __m2_old = False
    __uzem_old = False
    __hiba_old = False

    __ks_old = 0

    def __init__(self, ip, rack, slot) -> None:
        super().__init__(Szalag2v2_Address(), ip, rack, slot)

        self.__s1 = False
        self.__s2 = False
        self.__kp1 = False
        self.__kp2 = False
        self.__start = False
        self.__stop = False

        self.__m1 = False
        self.__m2 = False
        self.__uzem = False
        self.__hiba = False

        self.__ks = 0

    @property
    def s1(self):
        return self.__s1

    @property
    def s2(self):
        return self.__s2

    @property
    def kp1(self):
        return self.__kp1

    @property
    def kp2(self):
        return self.__kp2

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
    def uzem(self):
        return self.__uzem

    @property
    def hiba(self):
        return self.__hiba

    @property
    def ks(self):
        return self.__ks

    @property
    def ks_percent(self):
        return int(self.__ks / Szalag2v2_Address.KS_RANGE * 100)

    def read_data(self) -> None:
        super().read_data()

        self.__s1 = self.get_bit_in_page(Szalag2v2_Address.S1)
        self.__s2 = self.get_bit_in_page(Szalag2v2_Address.S2)
        self.__kp1 = self.get_bit_in_page(Szalag2v2_Address.KP1)
        self.__kp2 = self.get_bit_in_page(Szalag2v2_Address.KP2)
        self.__start = self.get_bit_in_page(Szalag2v2_Address.START)
        self.__stop = self.get_bit_in_page(Szalag2v2_Address.STOP)

        self.__m1 = self.get_bit_in_page(Szalag2v2_Address.M1)
        self.__m2 = self.get_bit_in_page(Szalag2v2_Address.M2)
        self.__uzem = self.get_bit_in_page(Szalag2v2_Address.UZEM)
        self.__hiba = self.get_bit_in_page(Szalag2v2_Address.HIBA)

        self.__ks = self.get_int_in_page(Szalag2v2_Address.KS)

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

    def kp1_is_changed(self):
        if self.__kp1 != self.__kp1_old:
            self.__kp1_old = self.__kp1
            return True
        return False

    def kp2_is_changed(self):
        if self.__kp2 != self.__kp2_old:
            self.__kp2_old = self.__kp2
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

    def ks_is_changed(self, threshold=0):
        if self.__ks < self.__ks_old - threshold // 2 or \
                self.__ks > self.__ks_old + threshold // 2:
            self.__ks_old = self.__ks
            return True
        return False
