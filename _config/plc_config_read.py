"""
PLC config read

File format (xml):
    <plc_config>
        <ip>[PLC ip address (str)]</ip>
        <rack>[PLC rack id (int)]</rack>
        <slot>[PLC slot id (int)]</slot>
    </plc_config>

Example:
    <plc_config>
        <ip>127.0.0.1</ip>
        <rack>0</rack>
        <slot>1</slot>
    </plc_config>
"""

from xml.etree.ElementTree import parse


class PLC_ConfigXML_Exception(Exception):
    """
    PLC config read exception
    """
    pass


class PLC_Config:

    @staticmethod
    def read_plc_config(filename) -> tuple[str, int, int]:
        """
        PLC config read
        :param str filename: file name string
        :return: return PLC config [ip, rack, slot]
        """
        root = parse(filename).getroot()

        if root.tag == 'plc_config' and root[0].tag == 'ip' and root[1].tag == 'rack' and root[2].tag == 'slot':
            ip = root[0].text
            rack = root[1].text
            slot = root[2].text

            try:
                split_ip = [int(x) for x in ip.split('.')]
            except AttributeError:
                raise PLC_ConfigXML_Exception
            except ValueError:
                raise PLC_ConfigXML_Exception

            if len(split_ip) == 4 and\
                    0 <= split_ip[0] <= 255 and\
                    0 <= split_ip[1] <= 255 and\
                    0 <= split_ip[2] <= 255 and\
                    0 <= split_ip[3] <= 255:
                return ip, int(rack), int(slot)

        raise PLC_ConfigXML_Exception
