# noinspection SpellCheckingInspection
from _plc_data.plc_data import PLC_Address, PLC_data


# noinspection SpellCheckingInspection,PyPep8Naming
class Tartaly4_Address(PLC_Address):

    T1_TELI = 'I0.0'
    T2_TELI = 'I0.1'
    T3_FELSO = 'I0.2'
    T3_KOZEP = 'I0.3'
    T3_ALSO = 'I0.4'
    START_URIT = 'I0.5'
    START = 'I0.6'
    STOP = 'I0.7'

    T1_TOLT = 'Q0.0'
    T1_FUT = 'Q0.1'
    T1_URIT = 'Q0.2'
    T2_TOLT = 'Q0.3'
    T2_FUT = 'Q0.4'
    T2_URIT = 'Q0.5'
    T3_KEVER = 'Q4.0'
    T3_URIT = 'Q4.1'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))

    T1_HOMERSEKLET = 'IW64'
    T2_HOMERSEKLET = 'IW66'

    READ_WORDS_TAG_ADDRESS = (('IW64', 2),)

    T1_HOMERSEKLET_RANGE = 24000
    T2_HOMERSEKLET_RANGE = 24000


# noinspection SpellCheckingInspection,PyPep8Naming
class Tartaly4_data(PLC_data):

    __t1_teli_old = False
    __t2_teli_old = False
    __t3_felso_old = False
    __t3_kozep_old = False
    __t3_also_old = False
    __start_urit_old = False
    __start_old = False
    __stop_old = False

    __t1_tolt_old = False
    __t1_fut_old = False
    __t1_urit_old = False
    __t2_tolt_old = False
    __t2_fut_old = False
    __t2_urit_old = False
    __t3_kever_old = False
    __t3_urit_old = False

    __t1_homerseklet_old = 0
    __t2_homerseklet_old = 0

    def __init__(self, ip, rack, slot):
        super().__init__(Tartaly4_Address(), ip, rack, slot)
        self.__t1_teli = False
        self.__t2_teli = False
        self.__t3_felso = False
        self.__t3_kozep = False
        self.__t3_also = False
        self.__start_urit = False
        self.__start = False
        self.__stop = False

        self.__t1_tolt = False
        self.__t1_fut = False
        self.__t1_urit = False
        self.__t2_tolt = False
        self.__t2_fut = False
        self.__t2_urit = False
        self.__t3_kever = False
        self.__t3_urit = False

        self.__t1_homerseklet = 0
        self.__t2_homerseklet = 0

    @property
    def t1_teli(self):
        return self.__t1_teli

    @property
    def t2_teli(self):
        return self.__t2_teli

    @property
    def t3_felso(self):
        return self.__t3_felso

    @property
    def t3_kozep(self):
        return self.__t3_kozep

    @property
    def t3_also(self):
        return self.__t3_also

    @property
    def start_urit(self):
        return self.__start_urit

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
    def t2_tolt(self):
        return self.__t2_tolt

    @property
    def t2_fut(self):
        return self.__t2_fut

    @property
    def t2_urit(self):
        return self.__t2_urit

    @property
    def t3_kever(self):
        return self.__t3_kever

    @property
    def t3_urit(self):
        return self.__t3_urit

    @property
    def t1_homerseklet(self):
        return self.__t1_homerseklet

    @property
    def t1_homerseklet_percent(self):
        return int(self.__t1_homerseklet / Tartaly4_Address.T1_HOMERSEKLET_RANGE * 100)

    @property
    def t2_homerseklet(self):
        return self.__t2_homerseklet

    @property
    def t2_homerseklet_percent(self):
        return int(self.__t2_homerseklet / Tartaly4_Address.T2_HOMERSEKLET_RANGE * 100)

    def read_data(self):
        super().read_data()

        self.__t1_teli = self.get_bit_tag_page(Tartaly4_Address.T1_TELI)
        self.__t2_teli = self.get_bit_tag_page(Tartaly4_Address.T2_TELI)
        self.__t3_felso = self.get_bit_tag_page(Tartaly4_Address.T3_FELSO)
        self.__t3_kozep = self.get_bit_tag_page(Tartaly4_Address.T3_KOZEP)
        self.__t3_also = self.get_bit_tag_page(Tartaly4_Address.T3_ALSO)
        self.__start_urit = self.get_bit_tag_page(Tartaly4_Address.START_URIT)
        self.__start = self.get_bit_tag_page(Tartaly4_Address.START)
        self.__stop = self.get_bit_tag_page(Tartaly4_Address.STOP)

        self.__t1_tolt = self.get_bit_tag_page(Tartaly4_Address.T1_TOLT)
        self.__t1_fut = self.get_bit_tag_page(Tartaly4_Address.T1_FUT)
        self.__t1_urit = self.get_bit_tag_page(Tartaly4_Address.T1_URIT)
        self.__t2_tolt = self.get_bit_tag_page(Tartaly4_Address.T2_TOLT)
        self.__t2_fut = self.get_bit_tag_page(Tartaly4_Address.T2_FUT)
        self.__t2_urit = self.get_bit_tag_page(Tartaly4_Address.T2_URIT)
        self.__t3_kever = self.get_bit_tag_page(Tartaly4_Address.T3_KEVER)
        self.__t3_urit = self.get_bit_tag_page(Tartaly4_Address.T3_URIT)

        self.__t1_homerseklet = self.get_int_tag_page(Tartaly4_Address.T1_HOMERSEKLET)
        self.__t2_homerseklet = self.get_int_tag_page(Tartaly4_Address.T2_HOMERSEKLET)

    def t1_teli_is_changed(self):
        if self.__t1_teli != self.__t1_teli_old:
            self.__t1_teli_old = self.t1_teli
            return True
        return False

    def t2_teli_is_changed(self):
        if self.__t2_teli != self.__t2_teli_old:
            self.__t2_teli_old = self.t2_teli
            return True
        return False

    def t3_felso_is_changed(self):
        if self.__t3_felso != self.__t3_felso_old:
            self.__t3_felso_old = self.__t3_felso
            return True
        return False

    def t3_kozep_is_changed(self):
        if self.__t3_kozep != self.__t3_kozep_old:
            self.__t3_kozep_old = self.__t3_kozep
            return True
        return False

    def t3_also_is_changed(self):
        if self.__t3_also != self.__t3_also_old:
            self.__t3_also_old = self.__t3_also
            return True
        return False

    def start_urit_is_changed(self):
        if self.__start_urit != self.__start_urit_old:
            self.__start_urit_old = self.__start_urit
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

    def t2_tolt_is_changed(self):
        if self.__t2_tolt != self.__t2_tolt_old:
            self.__t2_tolt_old = self.__t2_tolt
            return True
        return False

    def t2_fut_is_changed(self):
        if self.__t2_fut != self.__t2_fut_old:
            self.__t2_fut_old = self.__t2_fut
            return True
        return False

    def t2_urit_is_changed(self):
        if self.__t2_urit != self.__t2_urit_old:
            self.__t2_urit_old = self.__t2_urit
            return True
        return False

    def t3_kever_is_changed(self):
        if self.__t3_kever != self.__t3_kever_old:
            self.__t3_kever_old = self.__t3_kever
            return True
        return False

    def t3_urit_is_changed(self):
        if self.__t3_urit != self.__t3_urit_old:
            self.__t3_urit_old = self.__t3_urit
            return True
        return False

    def t1_homerseklet_is_changed(self, threshold=0):
        if self.__t1_homerseklet < self.__t1_homerseklet_old - threshold // 2 or \
                self.__t1_homerseklet > self.__t1_homerseklet_old + threshold // 2:
            self.__t1_homerseklet_old = self.__t1_homerseklet
            return True
        return False

    def t2_homerseklet_is_changed(self, threshold=0):
        if self.__t2_homerseklet < self.__t2_homerseklet_old - threshold // 2 or \
                self.__t2_homerseklet > self.__t2_homerseklet_old + threshold // 2:
            self.__t2_homerseklet_old = self.__t2_homerseklet
            return True
        return False
