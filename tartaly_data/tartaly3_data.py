
from _config.plc_config_read import PLC_Config
from _plc_data.plc_data import PLC_Address, PLC_data


# noinspection SpellCheckingInspection
class Tartaly3_Address(PLC_Address):
    IP_LIST, RACK, SLOT = PLC_Config.read_plc_config('_config/config.xml')
    DEFAULT_IP = PLC_Config.read_plc_default_ip('_config/default.xml')

    T1_FELSO = 'I0.0'
    T1_ALSO = 'I0.1'
    T2_FELSO = 'I0.2'
    T2_ALSO = 'I0.3'
    T3_FELSO = 'I0.4'
    T3_ALSO = 'I0.5'

    START = 'I0.6'
    STOP = 'I0.7'

    T1_TOLT = 'Q0.0'
    T2_TOLT = 'Q0.1'
    T3_TOLT = 'Q0.2'

    BEKAPCSOLVA = 'Q4.0'
    KIKAPCSOLVA = 'Q4.1'

    READ_BYTES_ADDRESS = ('IB0', 'QB0', 'QB4')


# noinspection SpellCheckingInspection
class Tartaly3_data(PLC_data):

    __t1_felso_old = False
    __t1_also_old = False
    __t2_felso_old = False
    __t2_also_old = False
    __t3_felso_old = False
    __t3_also_old = False

    __start_old = False
    __stop_old = False

    __t1_tolt_old = False
    __t2_tolt_old = False
    __t3_tolt_old = False

    __bekapcsolva_old = False
    __kikapcsolva_old = False

    def __init__(self, ip, rack, slot):
        super().__init__(Tartaly3_Address(), ip, rack, slot)
        self.__t1_felso = False
        self.__t1_also = False
        self.__t2_felso = False
        self.__t2_also = False
        self.__t3_felso = False
        self.__t3_also = False

        self.__start = False
        self.__stop = False

        self.__t1_tolt = False
        self.__t2_tolt = False
        self.__t3_tolt = False

        self.__bekapcsolva = False
        self.__kikapcsolva = False

    @property
    def t1_felso(self):
        return self.__t1_felso

    @property
    def t1_also(self):
        return self.__t1_also

    @property
    def t2_felso(self):
        return self.__t2_felso

    @property
    def t2_also(self):
        return self.__t2_also

    @property
    def t3_felso(self):
        return self.__t3_felso

    @property
    def t3_also(self):
        return self.__t3_also

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
    def t3_tolt(self):
        return self.__t3_tolt

    @property
    def bekapcsolva(self):
        return self.__bekapcsolva

    @property
    def kikapcsolva(self):
        return self.__kikapcsolva

    def read_data(self):
        super().read_data()

        self.__t1_felso = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.T1_FELSO)][PLC_Address.bit_index(Tartaly3_Address.T1_FELSO)]
        self.__t1_also = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.T1_ALSO)][PLC_Address.bit_index(Tartaly3_Address.T1_ALSO)]
        self.__t2_felso = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.T2_FELSO)][PLC_Address.bit_index(Tartaly3_Address.T2_FELSO)]
        self.__t2_also = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.T2_ALSO)][PLC_Address.bit_index(Tartaly3_Address.T2_ALSO)]
        self.__t3_felso = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.T3_FELSO)][PLC_Address.bit_index(Tartaly3_Address.T3_FELSO)]
        self.__t3_also = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.T3_ALSO)][PLC_Address.bit_index(Tartaly3_Address.T3_ALSO)]
        self.__start = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.START)][PLC_Address.bit_index(Tartaly3_Address.START)]
        self.__stop = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.STOP)][PLC_Address.bit_index(Tartaly3_Address.STOP)]

        self.__t1_tolt = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.T1_TOLT)][PLC_Address.bit_index(Tartaly3_Address.T1_TOLT)]
        self.__t2_tolt = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.T2_TOLT)][PLC_Address.bit_index(Tartaly3_Address.T2_TOLT)]
        self.__t3_tolt = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.T3_TOLT)][PLC_Address.bit_index(Tartaly3_Address.T3_TOLT)]

        self.__bekapcsolva = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.BEKAPCSOLVA)][PLC_Address.bit_index(Tartaly3_Address.BEKAPCSOLVA)]
        self.__kikapcsolva = self.read_byte_data[
            PLC_Address.byte_address(Tartaly3_Address.KIKAPCSOLVA)][PLC_Address.bit_index(Tartaly3_Address.KIKAPCSOLVA)]

    def t1_felso_is_changed(self):
        if self.__t1_felso != self.__t1_felso_old:
            self.__t1_felso_old = self.__t1_felso
            return True
        return False

    def t1_also_is_changed(self):
        if self.__t1_also != self.__t1_also_old:
            self.__t1_also_old = self.__t1_also
            return True
        return False

    def t2_felso_is_changed(self):
        if self.__t2_felso != self.__t2_felso_old:
            self.__t2_felso_old = self.__t2_felso
            return True
        return False

    def t2_also_is_changed(self):
        if self.__t2_also != self.__t2_also_old:
            self.__t2_also_old = self.__t2_also
            return True
        return False

    def t3_felso_is_changed(self):
        if self.__t3_felso != self.__t3_felso_old:
            self.__t3_felso_old = self.__t3_felso
            return True
        return False

    def t3_also_is_changed(self):
        if self.__t3_also != self.__t3_also_old:
            self.__t3_also_old = self.__t3_also
            return True
        return False

    def start_is_change(self):
        if self.__start != self.__start_old:
            self.__start_old = self.__start
            return True
        return False

    def stop_is_change(self):
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

    def t3_tolt_is_changed(self):
        if self.__t3_tolt != self.__t3_tolt_old:
            self.__t3_tolt_old = self.__t3_tolt
            return True
        return False

    def bekapcsolva_is_changed(self):
        if self.__bekapcsolva != self.__bekapcsolva_old:
            self.__bekapcsolva_old = self.__bekapcsolva
            return True
        return False

    def kikapcsolva_is_changed(self):
        if self.__kikapcsolva != self.__kikapcsolva_old:
            self.__kikapcsolva_old = self.__kikapcsolva
            return True
        return False
