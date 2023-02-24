from _plc_data.plc_data import PLC_Address, PLC_data


class IO_View_Address(PLC_Address):

    INPUT1 = 'I0.0'
    INPUT2 = 'I0.1'
    INPUT3 = 'I0.2'
    INPUT4 = 'I0.3'
    INPUT5 = 'I0.4'
    INPUT6 = 'I0.5'
    INPUT7 = 'I0.6'
    INPUT8 = 'I0.7'

    OUTPUT1 = 'Q0.0'
    OUTPUT2 = 'Q0.1'
    OUTPUT3 = 'Q0.2'
    OUTPUT4 = 'Q0.3'
    OUTPUT5 = 'Q0.4'
    OUTPUT6 = 'Q0.5'
    OUTPUT7 = 'Q0.6'
    OUTPUT8 = 'Q0.7'
    OUTPUT9 = 'Q1.0'
    OUTPUT10 = 'Q1.1'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))

    ANALOG_IN_CH0 = 'IW64'
    ANALOG_IN_CH1 = 'IW66'

    ANALOG_OUT_CH0 = 'QW96'
    ANALOG_OUT_CH1 = 'QW98'

    READ_WORDS_TAG_ADDRESS = (('IW64', 2), ('QW96', 2))

    ANALOG_IN_CH0_RANGE = 27648
    ANALOG_IN_CH1_RANGE = 27648

    ANALOG_OUT_CH0_RANGE = 27648
    ANALOG_OUT_CH1_RANGE = 27648


class IO_View_Data(PLC_data):

    __input1_old = False
    __input2_old = False
    __input3_old = False
    __input4_old = False
    __input5_old = False
    __input6_old = False
    __input7_old = False
    __input8_old = False

    __output1_old = False
    __output2_old = False
    __output3_old = False
    __output4_old = False
    __output5_old = False
    __output6_old = False
    __output7_old = False
    __output8_old = False
    __output9_old = False
    __output10_old = False

    __analog_in_ch0_old = 0
    __analog_in_ch1_old = 0

    __analog_out_ch0_old = 0
    __analog_out_ch1_old = 0

    def __init__(self, ip, rack, slot):
        super().__init__(IO_View_Address(), ip, rack, slot)

        self.__input1 = False
        self.__input2 = False
        self.__input3 = False
        self.__input4 = False
        self.__input5 = False
        self.__input6 = False
        self.__input7 = False
        self.__input8 = False

        self.__output1 = False
        self.__output2 = False
        self.__output3 = False
        self.__output4 = False
        self.__output5 = False
        self.__output6 = False
        self.__output7 = False
        self.__output8 = False
        self.__output9 = False
        self.__output10 = False

        self.__analog_in_ch0 = 0
        self.__analog_in_ch1 = 0

        self.__analog_out_ch0 = 0
        self.__analog_out_ch1 = 0

    @property
    def input1(self):
        return self.__input1

    @property
    def input2(self):
        return self.__input2

    @property
    def input3(self):
        return self.__input3

    @property
    def input4(self):
        return self.__input4

    @property
    def input5(self):
        return self.__input5

    @property
    def input6(self):
        return self.__input6

    @property
    def input7(self):
        return self.__input7

    @property
    def input8(self):
        return self.__input8

    @property
    def output1(self):
        return self.__output1

    @property
    def output2(self):
        return self.__output2

    @property
    def output3(self):
        return self.__output3

    @property
    def output4(self):
        return self.__output4

    @property
    def output5(self):
        return self.__output5

    @property
    def output6(self):
        return self.__output6

    @property
    def output7(self):
        return self.__output7

    @property
    def output8(self):
        return self.__output8

    @property
    def output9(self):
        return self.__output9

    @property
    def output10(self):
        return self.__output10

    @property
    def analog_in_ch0(self):
        return self.__analog_in_ch0

    @property
    def analog_in_ch0_percent(self):
        return int(self.__analog_in_ch0 / IO_View_Address.ANALOG_IN_CH0_RANGE * 100)

    @property
    def analog_in_ch1(self):
        return self.__analog_in_ch1

    @property
    def analog_in_ch1_percent(self):
        return int(self.__analog_in_ch1 / IO_View_Address.ANALOG_IN_CH1_RANGE * 100)

    @property
    def analog_out_ch0(self):
        return self.__analog_out_ch0

    @property
    def analog_out_ch0_percent(self):
        return int(self.__analog_out_ch0 / IO_View_Address.ANALOG_OUT_CH0_RANGE * 100)

    @property
    def analog_out_ch1(self):
        return self.__analog_out_ch1

    @property
    def analog_out_ch1_percent(self):
        return int(self.__analog_out_ch1 / IO_View_Address.ANALOG_OUT_CH1_RANGE * 100)

    def read_data(self):
        super().read_data()

        self.__input1 = self.get_bit_tag_page(IO_View_Address.INPUT1)
        self.__input2 = self.get_bit_tag_page(IO_View_Address.INPUT2)
        self.__input3 = self.get_bit_tag_page(IO_View_Address.INPUT3)
        self.__input4 = self.get_bit_tag_page(IO_View_Address.INPUT4)
        self.__input5 = self.get_bit_tag_page(IO_View_Address.INPUT5)
        self.__input6 = self.get_bit_tag_page(IO_View_Address.INPUT6)
        self.__input7 = self.get_bit_tag_page(IO_View_Address.INPUT7)
        self.__input8 = self.get_bit_tag_page(IO_View_Address.INPUT8)

        self.__output1 = self.get_bit_tag_page(IO_View_Address.OUTPUT1)
        self.__output2 = self.get_bit_tag_page(IO_View_Address.OUTPUT2)
        self.__output3 = self.get_bit_tag_page(IO_View_Address.OUTPUT3)
        self.__output4 = self.get_bit_tag_page(IO_View_Address.OUTPUT4)
        self.__output5 = self.get_bit_tag_page(IO_View_Address.OUTPUT5)
        self.__output6 = self.get_bit_tag_page(IO_View_Address.OUTPUT6)
        self.__output7 = self.get_bit_tag_page(IO_View_Address.OUTPUT7)
        self.__output8 = self.get_bit_tag_page(IO_View_Address.OUTPUT8)
        self.__output9 = self.get_bit_tag_page(IO_View_Address.OUTPUT9)
        self.__output10 = self.get_bit_tag_page(IO_View_Address.OUTPUT10)

        self.__analog_in_ch0 = self.get_int_tag_page(IO_View_Address.ANALOG_IN_CH0)
        self.__analog_in_ch1 = self.get_int_tag_page(IO_View_Address.ANALOG_IN_CH1)

        self.__analog_out_ch0 = self.get_int_tag_page(IO_View_Address.ANALOG_OUT_CH0)
        self.__analog_out_ch1 = self.get_int_tag_page(IO_View_Address.ANALOG_OUT_CH1)

    def input_is_changed(self):
        if self.__input1 != self.__input1_old or self.__input2 != self.__input2_old or \
                self.__input3 != self.__input3_old or self.__input4 != self.__input4_old or \
                self.__input5 != self.__input5_old or self.__input6 != self.__input6_old or \
                self.__input7 != self.__input7_old or self.__input8 != self.__input8_old:
            self.__input1_old = self.__input1
            self.__input2_old = self.__input2
            self.__input3_old = self.__input3
            self.__input4_old = self.__input4
            self.__input5_old = self.__input5
            self.__input6_old = self.__input6
            self.__input7_old = self.__input7
            self.__input8_old = self.__input8
            return True
        return False

    def output_is_changed(self):
        if self.__output1 != self.__output1_old or self.__output2 != self.__output2_old or \
                self.__output3 != self.__output3_old or self.__output4 != self.__output4_old or \
                self.__output5 != self.__output5_old or self.__output6 != self.__output6_old or \
                self.__output7 != self.__output7_old or self.__output8 != self.__output8_old or \
                self.__output9 != self.__output9_old or self.__output10 != self.__output10_old:
            self.__output1_old = self.__output1
            self.__output2_old = self.__output2
            self.__output3_old = self.__output3
            self.__output4_old = self.__output4
            self.__output5_old = self.__output5
            self.__output6_old = self.__output6
            self.__output7_old = self.__output7
            self.__output8_old = self.__output8
            self.__output9_old = self.__output9
            self.__output10_old = self.__output10
            return True
        return False

    def analog_in_ch0_is_changed(self, threshold=0):
        if self.__analog_in_ch0 < self.__analog_in_ch0_old - threshold // 2 or \
                self.__analog_in_ch0 > self.__analog_in_ch0_old + threshold // 2:
            self.__analog_in_ch0_old = self.__analog_in_ch0
            return True
        return False

    def analog_in_ch1_is_changed(self, threshold=0):
        if self.__analog_in_ch1 < self.__analog_in_ch1_old - threshold // 2 or \
                self.__analog_in_ch1 > self.__analog_in_ch1_old + threshold // 2:
            self.__analog_in_ch1_old = self.__analog_in_ch1
            return True
        return False

    def analog_out_ch0_is_changed(self, threshold=0):
        if self.__analog_out_ch0 < self.__analog_out_ch0_old - threshold // 2 or \
                self.__analog_out_ch0 > self.__analog_out_ch0_old + threshold // 2:
            self.__analog_out_ch0_old = self.__analog_out_ch0
            return True
        return False

    def analog_out_ch1_is_changed(self, threshold=0):
        if self.__analog_out_ch1 < self.__analog_out_ch1_old - threshold // 2 or \
                self.__analog_out_ch1 > self.__analog_out_ch1_old + threshold // 2:
            self.__analog_out_ch1_old = self.__analog_out_ch1
            return True
        return False
