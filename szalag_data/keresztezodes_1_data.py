from _plc_data.plc_data import PLC_Address


class Keresztezodes1_Address(PLC_Address):

    A_PIROS = 'Q0.0'
    A_SARGA = 'Q0.1'
    A_ZOLD = 'Q0.2'
    B_PIROS = 'Q0.3'
    B_SARGA = 'Q0.4'
    B_ZOLD = 'Q0.5'

    READ_BYTES_TAG_ADDRESS = (('QB0', 1), )
    