from _plc_data.plc_data import PLC_Address, PLC_data


# noinspection PyPep8Naming,SpellCheckingInspection
class Szalag6v0_Address(PLC_Address):

    S1 = 'I0.0'
    START = 'I0.6'
    STOP = 'I0.7'

    M1 = 'Q0.0'
    M2 = 'Q0.1'
    M3 = 'Q0.2'
    UZEM = 'Q4.0'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))


# noinspection PyPep8Naming,SpellCheckingInspection
class Szalag6v0_data(PLC_data):

    __s1_old = False
    __start_old = False
    __stop_old = False

    __m1_old = False
    __m2_old = False
    __m3_old = False
    __uzem_old = False

    def __init__(self, ip, rack, slot) -> None:
        super().__init__(Szalag6v0_Address(), ip, rack, slot)

        self.__s1 = False
        self.__start = False
        self.__stop = False

        self.__m1 = False
        self.__m2 = False
        self.__m3 = False
        self.__uzem = False

    @property
    def s1(self):
        return self.__s1

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
    def uzem(self):
        return self.__uzem

    def read_data(self) -> None:
        super().read_data()

        self.__s1 = self.get_bit_tag_page(Szalag6v0_Address.S1)
        self.__start = self.get_bit_tag_page(Szalag6v0_Address.START)
        self.__stop = self.get_bit_tag_page(Szalag6v0_Address.STOP)

        self.__m1 = self.get_bit_tag_page(Szalag6v0_Address.M1)
        self.__m2 = self.get_bit_tag_page(Szalag6v0_Address.M2)
        self.__m3 = self.get_bit_tag_page(Szalag6v0_Address.M3)
        self.__uzem = self.get_bit_tag_page(Szalag6v0_Address.UZEM)

    def s1_is_changed(self):
        if self.__s1 != self.__s1_old:
            self.__s1_old = self.__s1
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

    def uzem_is_changed(self):
        if self.__uzem != self.__uzem_old:
            self.__uzem_old = self.__uzem
            return True
        return False
