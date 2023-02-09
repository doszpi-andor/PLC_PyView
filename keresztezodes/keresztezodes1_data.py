from _plc_data.plc_data import PLC_Address, PLC_data


class Keresztezodes1_Address(PLC_Address):

    A_PIROS = 'Q0.0'
    A_SARGA = 'Q0.1'
    A_ZOLD = 'Q0.2'
    B_PIROS = 'Q0.3'
    B_SARGA = 'Q0.4'
    B_ZOLD = 'Q0.5'

    READ_BYTES_TAG_ADDRESS = (('QB0', 1), )

class Keresztezodes1_data(PLC_data):

    __a_piros_old = False
    __a_sarga_old = False
    __a_zold_old = False
    __b_piros_old = False
    __b_sarga_old = False
    __b_zold_old = False

    def __init__(self, ip, rack, slot) -> None:
        super().__init__(Keresztezodes1_Address(), ip, rack, slot)
        self.a_piros = False
        self.a_sarga = False
        self.a_zold = False
        self.b_piros = False
        self.b_sarga = False
        self.b_zold = False

    def read_data(self):
        super().read_data()

        self.a_piros = self.get_bit_tag_page(Keresztezodes1_Address.A_PIROS)
        self.a_sarga = self.get_bit_tag_page(Keresztezodes1_Address.A_SARGA)
        self.a_zold = self.get_bit_tag_page(Keresztezodes1_Address.A_ZOLD)

        self.b_piros = self.get_bit_tag_page(Keresztezodes1_Address.B_PIROS)
        self.b_sarga = self.get_bit_tag_page(Keresztezodes1_Address.B_SARGA)
        self.b_zold = self.get_bit_tag_page(Keresztezodes1_Address.B_ZOLD)

    def a_piros_is_changed(self):
        if self.a_piros != self.__a_piros_old:
            self.__a_piros_old = self.a_piros
            return True
        return False

    def a_sarga_is_changed(self):
        if self.a_sarga != self.__a_sarga_old:
            self.__a_sarga_old = self.a_sarga
            return True
        return False

    def a_zold_is_changed(self):
        if self.a_zold != self.__a_zold_old:
            self.__a_zold_old = self.a_zold
            return True
        return False

    def b_piros_is_changed(self):
        if self.b_piros != self.__b_piros_old:
            self.__b_piros_old = self.b_piros
            return True
        return False

    def b_sarga_is_changed(self):
        if self.b_sarga != self.__b_sarga_old:
            self.__b_sarga_old = self.b_sarga
            return True
        return False

    def b_zold_is_changed(self):
        if self.b_zold != self.__b_zold_old:
            self.__b_zold_old = self.b_zold
            return True
        return False
