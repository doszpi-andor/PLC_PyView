from _plc_data.plc_data import PLC_Address, PLC_data


class Atemelo_C_Address(PLC_Address):

    JELADO_1 = 'I0.2'
    JELADO_2 = 'I0.1'
    JELADO_3 = 'I0.0'
    ARALMAS_A = 'I0.4'
    ARAMLAS_B = 'I0.5'
    NYUGTA = 'I0.7'

    MOTOR_A = 'Q0.0'
    MOTOR_B = 'Q0.1'
    HIBA_LAMPA = 'Q4.1'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))


class Atemelo_C_Data(PLC_data):

    __jelado_1_old = False
    __jelado_2_old = False
    __jelado_3_old = False
    __aramlas_a_old = False
    __aramlas_b_old = False
    __nyugta_old = False

    __motor_a_old = False
    __motor_b_old = False
    __hiba_lampa_old = False

    def __init__(self, ip, rack, slot):
        super().__init__(Atemelo_C_Address(), ip, rack, slot)
        self.__jelado_1 = False
        self.__jelado_2 = False
        self.__jelado_3 = False
        self.__aramlas_a = False
        self.__aramlas_b = False
        self.__nyugta = False

        self.__motor_a = False
        self.__motor_b = False
        self.__hiba_lampa = False

    @property
    def jelado_1(self):
        return self.__jelado_1

    @property
    def jelado_2(self):
        return self.__jelado_2

    @property
    def jelado_3(self):
        return self.__jelado_3

    @property
    def aramlas_a(self):
        return self.__aramlas_a

    @property
    def aramlas_b(self):
        return self.__aramlas_b

    @property
    def nyugta(self):
        return self.__nyugta

    @property
    def motor_a(self):
        return self.__motor_a

    @property
    def motor_b(self):
        return self.__motor_b

    @property
    def hiba_lampa(self):
        return self.__hiba_lampa

    def read_data(self):
        super().read_data()

        self.__jelado_1 = self.get_bit_tag_page(Atemelo_C_Address.JELADO_1)
        self.__jelado_2 = self.get_bit_tag_page(Atemelo_C_Address.JELADO_2)
        self.__jelado_3 = self.get_bit_tag_page(Atemelo_C_Address.JELADO_3)
        self.__aramlas_a = self.get_bit_tag_page(Atemelo_C_Address.ARALMAS_A)
        self.__aramlas_b = self.get_bit_tag_page(Atemelo_C_Address.ARAMLAS_B)
        self.__nyugta = self.get_bit_tag_page(Atemelo_C_Address.NYUGTA)

        self.__motor_a = self.get_bit_tag_page(Atemelo_C_Address.MOTOR_A)
        self.__motor_b = self.get_bit_tag_page(Atemelo_C_Address.MOTOR_B)
        self.__hiba_lampa = self.get_bit_tag_page(Atemelo_C_Address.HIBA_LAMPA)

    def jeladi_1_is_changed(self):
        if self.__jelado_1 != self.__jelado_1_old:
            self.__jelado_1_old = self.__jelado_1
            return True
        return False

    def jeladi_2_is_changed(self):
        if self.__jelado_2 != self.__jelado_2_old:
            self.__jelado_2_old = self.__jelado_2
            return True
        return False

    def jeladi_3_is_changed(self):
        if self.__jelado_3 != self.__jelado_3_old:
            self.__jelado_3_old = self.__jelado_3
            return True
        return False

    def aramlas_a_is_changed(self):
        if self.__aramlas_a != self.__aramlas_a_old:
            self.__aramlas_a_old = self.__aramlas_a
            return True
        return False

    def aramlas_b_is_changed(self):
        if self.__aramlas_b != self.__aramlas_b_old:
            self.__aramlas_b_old = self.__aramlas_b
            return True
        return False

    def nyugta_is_changed(self):
        if self.__nyugta != self.__nyugta_old:
            self.__nyugta_old = self.__nyugta
            return True
        return False

    def motor_a_is_changed(self):
        if self.__motor_a != self.__motor_a_old:
            self.__motor_a_old = self.__motor_a
            return True
        return False

    def motor_b_is_changed(self):
        if self.__motor_b != self.__motor_b_old:
            self.__motor_b_old = self.__motor_b
            return True
        return False

    def hiba_lampa_is_changed(self):
        if self.__hiba_lampa != self.__hiba_lampa_old:
            self.__hiba_lampa_old = self.__hiba_lampa
            return True
        return False
