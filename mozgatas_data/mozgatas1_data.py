from _plc_data.plc_data import PLC_Address, PLC_data


class Mozgatas1A_Address(PLC_Address):
    E2 = 'I0.0'
    E1 = 'I0.1'
    E0 = 'I0.0'

    M_FEL = 'Q0.0'
    M_LE = 'Q0.1'
    M_FOG = 'Q0.2'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))


class Mozgatas1A_data(PLC_data):

    __e2_old = False
    __e1_old = False
    __e0_old = False

    __m_fel_old = False
    __m_le_old = False
    __m_fog_old = False

    def __init__(self, ip, rack, slot) -> None:
        super().__init__(Mozgatas1A_Address(), ip, rack, slot)

        self.e2 = False
        self.e1 = False
        self.e0 = False

        self.m_fel = False
        self.m_le = False
        self.m_fog = False

    def read_data(self):
        super().read_data()

        self.e2 = self.get_bit_tag_page(Mozgatas1A_Address.E2)
        self.e1 = self.get_bit_tag_page(Mozgatas1A_Address.E1)
        self.e0 = self.get_bit_tag_page(Mozgatas1A_Address.E0)

        self.m_fel = self.get_bit_tag_page(Mozgatas1A_Address.M_FEL)
        self.m_le = self.get_bit_tag_page(Mozgatas1A_Address.M_LE)
        self.m_fog = self.get_bit_tag_page(Mozgatas1A_Address.M_FOG)

    def e0_is_changed(self):
        if self.e0 != self.__e0_old:
            self.__e0_old = self.e0
            return True
        return False

    def e1_is_changed(self):
        if self.e1 != self.__e1_old:
            self.__e1_old = self.e1
            return True
        return False

    def e2_is_changed(self):
        if self.e2 != self.__e2_old:
            self.__e2_old = self.e2
            return True
        return False

    def m_fel_is_changed(self):
        if self.m_fel != self.__m_fel_old:
            self.__m_fel_old = self.m_fel
            return True
        return False

    def m_le_is_changed(self):
        if self.m_le != self.__m_le_old:
            self.__m_le_old = self.m_le
            return True
        return False

    def m_fog_is_changed(self):
        if self.m_fog != self.__m_fog_old:
            self.__m_fog_old = self.m_fog
            return True
        return False
