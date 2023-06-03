from _plc_data.plc_data import PLC_Address, PLC_data


# noinspection SpellCheckingInspection,PyPep8Naming
class Szalag8v1_Address(PLC_Address):

    SBE = 'I0.0'
    SA = 'I0.1'
    SB = 'I0.2'
    NYUGTA = 'I0.5'
    START = 'I0.6'
    STOP = 'I0.7'

    M1 = 'Q0.0'
    M2A = 'Q0.1'
    M2B = 'Q0.2'
    MEGTELT_A = 'Q0.3'
    MEGTELT_B = 'Q0.4'
    FOLYAMAT = 'Q0.5'
    UZEM = 'Q4.0'
    HIBA = 'Q4.1'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))


# noinspection SpellCheckingInspection,PyPep8Naming
class Szalag8v1_data(PLC_data):

    __sbe_old = False
    __sa_old = False
    __sb_old = False
    __nyugta_old = False
    __start_old = False
    __stop_old = False
    __m1_old = False
    __m2a_old = False
    __m2b_old = False
    __megtelt_a_old = False
    __megtelt_b_old = False
    __folyamat_old = False
    __uzem_old = False
    __hiba_old = False

    def __init__(self, ip, rack, slot) -> None:
        super().__init__(Szalag8v1_Address(), ip, rack, slot)
        self.sbe = False
        self.sa = False
        self.sb = False
        self.nyugta = False
        self.start = False
        self.stop = False
        self.m1 = False
        self.m2a = False
        self.m2b = False
        self.megtelt_a = False
        self.megtelt_b = False
        self.folyamat = False
        self.uzem = False
        self.hiba = False

    def read_data(self):
        super().read_data()

        self.sbe = self.get_bit_tag_page(Szalag8v1_Address.SBE)
        self.sa = self.get_bit_tag_page(Szalag8v1_Address.SA)
        self.sb = self.get_bit_tag_page(Szalag8v1_Address.SB)
        self.start = self.get_bit_tag_page(Szalag8v1_Address.START)
        self.stop = self.get_bit_tag_page(Szalag8v1_Address.STOP)
        self.nyugta = self.get_bit_tag_page(Szalag8v1_Address.NYUGTA)

        self.m1 = self.get_bit_tag_page(Szalag8v1_Address.M1)
        self.m2a = self.get_bit_tag_page(Szalag8v1_Address.M2A)
        self.m2b = self.get_bit_tag_page(Szalag8v1_Address.M2B)
        self.megtelt_a = self.get_bit_tag_page(Szalag8v1_Address.MEGTELT_A)
        self.megtelt_b = self.get_bit_tag_page(Szalag8v1_Address.MEGTELT_B)
        self.uzem = self.get_bit_tag_page(Szalag8v1_Address.UZEM)
        self.hiba = self.get_bit_tag_page(Szalag8v1_Address.HIBA)

    def sbe_is_changed(self):
        if self.sbe != self.__sbe_old:
            self.__sbe_old = self.sbe
            return True
        return False

    def sa_is_changed(self):
        if self.sa != self.__sa_old:
            self.__sa_old = self.sa
            return True
        return False

    def sb_is_changed(self):
        if self.sb != self.__sb_old:
            self.__sb_old = self.sb
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

    def m1_is_changed(self):
        if self.m1 != self.__m1_old:
            self.__m1_old = self.m1
            return True
        return False

    def m2a_is_changed(self):
        if self.m2a != self.__m2a_old:
            self.__m2a_old = self.m2a
            return True
        return False

    def m2b_is_changed(self):
        if self.m2b != self.__m2b_old:
            self.__m2b_old = self.m2b
            return True
        return False

    def megtelt_a_is_changed(self):
        if self.megtelt_a != self.__megtelt_a_old:
            self.__megtelt_a_old = self.megtelt_a
            return True
        return False

    def megtelt_b_is_changed(self):
        if self.megtelt_b != self.__megtelt_b_old:
            self.__megtelt_b_old = self.megtelt_b
            return True
        return False

    def folyamat_is_changed(self):
        if self.folyamat != self.__folyamat_old:
            self.__folyamat_old = self.folyamat
            return True
        return False

    def uzem_is_changed(self):
        if self.uzem != self.__uzem_old:
            self.__uzem_old = self.uzem
            return True
        return False

    def hiba_is_changed(self):
        if self.hiba != self.__hiba_old:
            self.__hiba_old = self.hiba
            return True
        return False
