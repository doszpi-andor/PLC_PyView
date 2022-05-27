
from _plc_data.plc_data import PLC_Address, PLC_data


# noinspection SpellCheckingInspection,PyPep8Naming
class Tartaly2_Address(PLC_Address):

    T1_TELI = 'I0.0'
    T1_MELEG = 'I0.1'
    T1_HIDEG = 'I0.2'
    T3_TELI = 'I0.3'
    T3_MELEG = 'I0.4'
    T3_HIDEG = 'I0.5'
    START = 'I0.6'
    STOP = 'I0.7'

    T1_TOLT = 'Q0.0'
    T1_FUT = 'Q0.1'
    T1_URIT = 'Q0.2'
    T3_TOLT = 'Q0.3'
    T3_FUT = 'Q0.4'
    T3_URIT = 'Q0.5'
    T2_ADALEK = 'Q0.6'
    T4_ADALEK = 'Q1.0'
    T2_URIT = 'Q0.7'
    T4_URIT = 'Q1.1'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))

    T2_SZINT = 'IW64'
    T4_SZINT = 'IW66'

    READ_WORDS_TAG_ADDRESS = (('IW64', 2),)

    T2_SZINT_RANGE = 24000
    T4_SZINT_RANGE = 24000


# noinspection SpellCheckingInspection,PyPep8Naming
class Tartaly2_data(PLC_data):
    __t1_teli_old = False
    __t1_meleg_old = False
    __t1_hideg_old = False
    __t3_teli_old = False
    __t3_meleg_old = False
    __t3_hideg_old = False
    __start_old = False
    __stop_old = False

    __t1_tolt_old = False
    __t1_fut_old = False
    __t1_urit_old = False
    __t3_tolt_old = False
    __t3_fut_old = False
    __t3_urit_old = False
    __t2_adalek_old = False
    __t4_adalek_old = False
    __t2_urit_old = False
    __t4_urit_old = False

    __t2_szint_old = 0
    __t4_szint_old = 0

    def __init__(self, ip, rack, slot):
        super().__init__(Tartaly2_Address(), ip, rack, slot)

        self.__t1_teli = False
        self.__t1_meleg = False
        self.__t1_hideg = False
        self.__t3_teli = False
        self.__t3_meleg = False
        self.__t3_hideg = False
        self.__start = False
        self.__stop = False

        self.__t1_tolt = False
        self. __t1_fut = False
        self.__t1_urit = False
        self.__t3_tolt = False
        self.__t3_fut = False
        self.__t3_urit = False
        self.__t2_adalek = False
        self.__t4_adalek = False
        self.__t2_urit = False
        self.__t4_urit = False

        self.__t2_szint = 0
        self.__t4_szint = 0

    @property
    def t1_teli(self):
        return self.__t1_teli

    @property
    def t1_meleg(self):
        return self.__t1_meleg

    @property
    def t1_hideg(self):
        return self.__t1_hideg

    @property
    def t3_teli(self):
        return self.__t3_teli

    @property
    def t3_meleg(self):
        return self.__t3_meleg

    @property
    def t3_hideg(self):
        return self.__t3_hideg

    @property
    def start(self):
        return self.__start

    @property
    def stop(self):
        return self.__stop

    @property
    def t1_tolt(self):
        return self.__t1_tolt

    @property
    def t1_fut(self):
        return self.__t1_fut

    @property
    def t1_urit(self):
        return self.__t1_urit

    @property
    def t3_tolt(self):
        return self.__t3_tolt

    @property
    def t3_fut(self):
        return self.__t3_fut

    @property
    def t3_urit(self):
        return self.__t3_urit

    @property
    def t2_adalek(self):
        return self.__t2_adalek

    @property
    def t4_adalek(self):
        return self.__t4_adalek

    @property
    def t2_urit(self):
        return self.__t2_urit

    @property
    def t4_urit(self):
        return self.__t4_urit

    @property
    def t2_szint(self):
        return self.__t2_szint

    @property
    def t2_szint_percent(self):
        return int(self.__t2_szint / Tartaly2_Address.T2_SZINT_RANGE * 100)

    @property
    def t4_szint(self):
        return self.__t4_szint

    @property
    def t4_szint_percent(self):
        return int(self.__t4_szint / Tartaly2_Address.T4_SZINT_RANGE * 100)

    def read_data(self) -> None:
        super().read_data()

        self.__t1_teli = self.get_bit_tag_page(Tartaly2_Address.T1_TELI)
        self.__t1_meleg = self.get_bit_tag_page(Tartaly2_Address.T1_MELEG)
        self.__t1_hideg = self.get_bit_tag_page(Tartaly2_Address.T1_HIDEG)
        self.__t3_teli = self.get_bit_tag_page(Tartaly2_Address.T3_TELI)
        self.__t3_meleg = self.get_bit_tag_page(Tartaly2_Address.T3_MELEG)
        self.__t3_hideg = self.get_bit_tag_page(Tartaly2_Address.T3_HIDEG)
        self.__start = self.get_bit_tag_page(Tartaly2_Address.START)
        self.__stop = self.get_bit_tag_page(Tartaly2_Address.STOP)

        self.__t1_tolt = self.get_bit_tag_page(Tartaly2_Address.T1_TOLT)
        self.__t1_fut = self.get_bit_tag_page(Tartaly2_Address.T1_FUT)
        self.__t1_urit = self.get_bit_tag_page(Tartaly2_Address.T1_URIT)
        self.__t3_tolt = self.get_bit_tag_page(Tartaly2_Address.T3_TOLT)
        self.__t3_fut = self.get_bit_tag_page(Tartaly2_Address.T3_FUT)
        self.__t3_urit = self.get_bit_tag_page(Tartaly2_Address.T3_URIT)
        self.__t2_adalek = self.get_bit_tag_page(Tartaly2_Address.T2_ADALEK)
        self.__t4_adalek = self.get_bit_tag_page(Tartaly2_Address.T4_ADALEK)
        self.__t2_urit = self.get_bit_tag_page(Tartaly2_Address.T2_URIT)
        self.__t4_urit = self.get_bit_tag_page(Tartaly2_Address.T4_URIT)

        self.__t2_szint = self.get_int_tag_page(Tartaly2_Address.T2_SZINT)
        self.__t4_szint = self.get_int_tag_page(Tartaly2_Address.T4_SZINT)

    def t1_teli_is_changed(self):
        if self.__t1_teli != self.__t1_teli_old:
            self.__t1_teli_old = self.t1_teli
            return True
        return False

    def t1_meleg_is_changed(self):
        if self.__t1_meleg != self.__t1_meleg_old:
            self.__t1_meleg_old = self.__t1_meleg
            return True
        return False

    def t1_hideg_is_changed(self):
        if self.__t1_hideg != self.__t1_hideg_old:
            self.__t1_hideg_old = self.__t1_hideg
            return True
        return False

    def t3_teli_is_changed(self):
        if self.__t3_teli != self.__t3_teli_old:
            self.__t3_teli_old = self.__t3_teli
            return True
        return False

    def t3_meleg_is_changed(self):
        if self.__t3_meleg != self.__t3_meleg_old:
            self.__t3_meleg_old = self.__t3_meleg
            return True
        return False

    def t3_hideg_is_changed(self):
        if self.__t3_hideg != self.__t3_hideg_old:
            self.__t3_hideg_old = self.__t3_hideg
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

    def t1_tolt_is_changed(self):
        if self.__t1_tolt != self.__t1_tolt_old:
            self.__t1_tolt_old = self.__t1_tolt
            return True
        return False

    def t1_fut_is_changed(self):
        if self.__t1_fut != self.__t1_fut_old:
            self.__t1_fut_old = self.__t1_fut
            return True
        return False

    def t1_urit_is_changed(self):
        if self.__t1_urit != self.__t1_urit_old:
            self.__t1_urit_old = self.__t1_urit
            return True
        return False

    def t3_tolt_is_changed(self):
        if self.__t3_tolt != self.__t3_tolt_old:
            self.__t3_tolt_old = self.__t3_tolt
            return True
        return False

    def t3_fut_is_changed(self):
        if self.__t3_fut != self.__t3_fut_old:
            self.__t3_fut_old = self.__t3_fut
            return True
        return False

    def t3_urit_is_changed(self):
        if self.__t3_urit != self.__t3_urit_old:
            self.__t3_urit_old = self.__t3_urit
            return True
        return False

    def t2_adalek_is_changed(self):
        if self.__t2_adalek != self.__t2_adalek_old:
            self.__t2_adalek_old = self.__t2_adalek
            return True
        return False

    def t4_adalek_is_changed(self):
        if self.__t4_adalek != self.__t4_adalek_old:
            self.__t4_adalek_old = self.__t4_adalek
            return True
        return False

    def t2_urit_is_changed(self):
        if self.__t2_urit != self.__t2_urit_old:
            self.__t2_urit_old = self.__t2_urit
            return True
        return False

    def t4_urit_is_changed(self):
        if self.__t4_urit != self.__t4_urit_old:
            self.__t4_urit_old = self.__t4_urit
            return True
        return False

    def t2_szint_is_changed(self, threshold=0):
        if self.__t2_szint < self.__t2_szint_old - threshold // 2 or \
                self.__t2_szint > self.__t2_szint_old + threshold // 2:
            self.__t2_szint_old = self.__t2_szint
            return True
        return False

    def t4_szint_is_changed(self, threshold=0):
        if self.__t4_szint < self.__t4_szint_old - threshold // 2 or \
                self.__t4_szint > self.__t4_szint_old + threshold // 2:
            self.__t4_szint_old = self.__t4_szint
            return True
        return False
