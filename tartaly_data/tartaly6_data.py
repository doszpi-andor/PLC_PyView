from _plc_data.plc_data import PLC_Address


# noinspection SpellCheckingInspection,PyPep8Naming
class Tartaly6_Address(PLC_Address):

    T1_TELI = 'I0.0'
    START = 'I0.6'
    STOP = 'I0.7'

    T1_TOLT = 'Q0.0'
    T2_TOLT = 'Q0.1'
    T2_ADALEK = 'Q0.2'
    T2_URIT = 'Q0.3'
    T3_TOLT = 'Q0.4'
    T3_ADALEK = 'Q0.5'
    T3_URIT = 'Q0.6'
    UZEM = 'Q0.7'

    READ_BYTES_TAG_ADDRESS = (('IB0', 1), ('QB0', 5))

    T2_SZINT = 'IW64'
    T3_SZINT = 'IW66'

    READ_WORDS_TAG_ADDRESS = (('IW64', 2),)

    T2_SZINT_RANGE = 24000
    T3_SZINT_RANGE = 24000