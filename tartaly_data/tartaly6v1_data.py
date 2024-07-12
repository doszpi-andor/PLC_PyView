from _plc_data.plc_data import PLC_Address, PLC_data


# noinspection SpellCheckingInspection,PyPep8Naming
class Tartaly6v1_Address(PLC_Address):

    T1_TELI = 'I0.0'
    START = 'I0.6'
    STOP = 'I0.7'

    T1_TOLT = 'Q0.0'
    T2_TOLT = 'Q0.1'
    T2_ADALEK = 'Q0.2'
    T2_URIT = 'Q0.3'
    T3_TOLT = 'Q0.4'
    T3_ADALEK = 'Q0.5'
    T3_URIT = 'Q4.0'
    UZEM = 'Q4.1'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))

    T2_SZINT = 'IW64'
    T3_SZINT = 'IW66'

    READ_WORDS_TAG_ADDRESS = (('IW64', 2),)

    T2_SZINT_RANGE = 24000
    T3_SZINT_RANGE = 24000


# noinspection SpellCheckingInspection,PyPep8Naming
class Tartaly6_data(PLC_data):

    __t1_teli_old = False
    __start_old = False
    __stop_old = False

    __t1_tolt_old = False
    __t2_tolt_old = False
    __t2_adalek_old = False
    __t2_urit_old = False
    __t3_tolt_old = False
    __t3_adalek_old = False
    __t3_urit_old = False
    __uzem_old = False

    __t2_szint_old = 0
    __t3_szint_old = 0

    def __init__(self, ip, rack, slot):
        super().__init__(Tartaly6v1_Address(), ip, rack, slot)
        self.__t1_teli = False
        self.__start = False
        self.__stop = False

        self.__t1_tolt = False
        self.__t2_tolt = False
        self.__t2_adalek = False
        self.__t2_urit = False
        self.__t3_tolt = False
        self.__t3_adalek = False
        self.__t3_urit = False
        self.__uzem = False

        self.__t2_szint = 0
        self.__t3_szint = 0

    @property
    def t1_teli(self):
        return self.__t1_teli

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
    def t2_tolt(self):
        return self.__t2_tolt

    @property
    def t2_adalek(self):
        return self.__t2_adalek

    @property
    def t2_urit(self):
        return self.__t2_urit

    @property
    def t3_tolt(self):
        return self.__t3_tolt

    @property
    def t3_adalek(self):
        return self.__t3_adalek

    @property
    def t3_urit(self):
        return self.__t3_urit

    @property
    def uzem(self):
        return self.__uzem

    @property
    def t2_szint(self):
        return self.__t2_szint

    @property
    def t2_szint_percent(self):
        return int(self.__t2_szint / Tartaly6v1_Address.T2_SZINT_RANGE * 100)

    @property
    def t3_szint_percent(self):
        return int(self.__t3_szint / Tartaly6v1_Address.T3_SZINT_RANGE * 100)

    def read_data(self):
        super().read_data()

        self.__t1_teli = self.get_bit_tag_page(Tartaly6v1_Address.T1_TELI)
        self.__start = self.get_bit_tag_page(Tartaly6v1_Address.START)
        self.__stop = self.get_bit_tag_page(Tartaly6v1_Address.STOP)

        self.__t1_tolt = self.get_bit_tag_page(Tartaly6v1_Address.T1_TOLT)
        self.__t2_tolt = self.get_bit_tag_page(Tartaly6v1_Address.T2_TOLT)
        self.__t2_adalek = self.get_bit_tag_page(Tartaly6v1_Address.T2_ADALEK)
        self.__t2_urit = self.get_bit_tag_page(Tartaly6v1_Address.T2_URIT)
        self.__t3_tolt = self.get_bit_tag_page(Tartaly6v1_Address.T3_TOLT)
        self.__t3_adalek = self.get_bit_tag_page(Tartaly6v1_Address.T3_ADALEK)
        self.__t3_urit = self.get_bit_tag_page(Tartaly6v1_Address.T3_URIT)
        self.__uzem = self.get_bit_tag_page(Tartaly6v1_Address.UZEM)

        self.__t2_szint = self.get_int_tag_page(Tartaly6v1_Address.T2_SZINT)
        self.__t3_szint = self.get_int_tag_page(Tartaly6v1_Address.T3_SZINT)

    def t1_teli_is_changed(self):
        if self.__t1_teli != self.__t1_teli_old:
            self.__t1_teli_old = self.t1_teli
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

    def t2_tolt_is_changed(self):
        if self.__t2_tolt != self.__t2_tolt_old:
            self.__t2_tolt_old = self.__t2_tolt
            return True
        return False

    def t2_adalek_is_changed(self):
        if self.__t2_adalek != self.__t2_adalek_old:
            self.__t2_adalek_old = self.__t2_adalek
            return True
        return False

    def t2_urit_is_changed(self):
        if self.__t2_urit != self.__t2_urit_old:
            self.__t2_urit_old = self.__t2_urit
            return True
        return False

    def t3_tolt_is_changed(self):
        if self.__t3_tolt != self.__t3_tolt_old:
            self.__t3_tolt_old = self.__t3_tolt
            return True
        return False

    def t3_adalek_is_changed(self):
        if self.__t3_adalek != self.__t3_adalek_old:
            self.__t3_adalek_old = self.__t3_adalek
            return True
        return False

    def t3_urit_is_changed(self):
        if self.__t3_urit != self.__t3_urit_old:
            self.__t3_urit_old = self.__t3_urit
            return True
        return False

    def uzem_is_changed(self):
        if self.__uzem != self.__uzem_old:
            self.__uzem_old = self.__uzem
            return True
        return False

    def t2_szint_is_changed(self, threshold=0):
        if self.__t2_szint < self.__t2_szint_old - threshold // 2 or \
                self.__t2_szint > self.__t2_szint_old + threshold // 2:
            self.__t2_szint_old = self.__t2_szint
            return True
        return False

    def t3_szint_is_changed(self, threshold=0):
        if self.__t3_szint < self.__t3_szint_old - threshold // 2 or \
                self.__t3_szint > self.__t3_szint_old + threshold // 2:
            self.__t3_szint_old = self.__t3_szint
            return True
        return False
