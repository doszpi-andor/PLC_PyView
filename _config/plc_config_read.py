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
    def read_plc_config(filename) -> tuple[list, int, int]:
        """
        PLC config read
        :param str filename: file name string
        :return: return PLC config [ip, rack, slot]
        """
        root = parse(filename).getroot()

        if root.tag == 'plc_config' and root[0].tag != 'ip_list' and root[1].tag != 'rack' and root[2].tag != 'slot':
            raise PLC_ConfigXML_Exception

        for ip in root[0]:
            if ip.tag != 'ip':
                raise PLC_ConfigXML_Exception

        ip_list = [ip.text for ip in root[0]]
        rack = int(root[1].text)
        slot = int(root[2].text)

        try:
            for ip in ip_list:
                split_ip = [int(x) for x in ip.split('.')]
                if len(split_ip) != 4 and\
                        0 > split_ip[0] > 255 and\
                        0 > split_ip[0] > 255 and\
                        0 > split_ip[0] > 255 and\
                        0 > split_ip[0] > 255:
                    raise PLC_ConfigXML_Exception
        except AttributeError:
            raise PLC_ConfigXML_Exception
        except ValueError:
            raise PLC_ConfigXML_Exception

        return ip_list, int(rack), int(slot)


if __name__ == '__main__':
    print(PLC_Config.read_plc_config('config.xml'))

