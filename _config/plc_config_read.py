"""
PLC config read

config.xml file format:
    <plc_config>
         <ip_list>
            <ip>[PLC ip address 1 (str)]</ip>
            <ip>[PLC ip address 2 (str)]</ip>
            ...
            <ip>[PLC ip address n (str)]</ip>
        </ip_list>
        <rack>[PLC rack id (int)]</rack>
        <slot>[PLC slot id (int)]</slot>
    </plc_config>

default.xml file format:
    <default>
        <ip>[PLC ip address (str)]</ip>
    </default>

config.xml example:
    <plc_config>
        <ip>192.168.0.1</ip>
        <ip>192.168.0.2</ip>
        <ip>192.168.0.3</ip>
        <rack>0</rack>
        <slot>1</slot>
    </plc_config>

default.xml example:
    <default>
        <ip>127.0.0.1</ip>
    </default>
"""

from xml.etree.ElementTree import parse


# noinspection PyPep8Naming
class PLC_ConfigXML_Exception(Exception):
    """
    PLC config read exception
    """
    pass


# noinspection PyPep8Naming
class PLC_Config:

    @staticmethod
    def read_plc_config(filename):
        """
        PLC config read
        :param str filename: file name string
        :return: return PLC config [ip, rack, slot]
        """
        root = parse(filename).getroot()

        if root.tag == 'plc_config' and root[0].tag == 'ip_list' and root[1].tag == 'rack' and root[2].tag == 'slot':

            for ip in root[0]:
                if ip.tag != 'ip':
                    raise PLC_ConfigXML_Exception

            ip_list = [ip.text for ip in root[0]]
            rack = int(root[1].text)
            slot = int(root[2].text)

            try:
                for ip in ip_list:
                    split_ip = [int(x) for x in ip.split('.')]
                    if len(split_ip) != 4 or\
                            split_ip[0] > 255 or split_ip[0] < 0 or \
                            split_ip[1] > 255 or split_ip[1] < 0 or \
                            split_ip[2] > 255 or split_ip[2] < 0 or\
                            split_ip[3] > 155 or split_ip[3] < 0:
                        raise PLC_ConfigXML_Exception
            except AttributeError:
                raise PLC_ConfigXML_Exception
            except ValueError:
                raise PLC_ConfigXML_Exception

            return ip_list, int(rack), int(slot)

        raise PLC_ConfigXML_Exception

    @staticmethod
    def read_plc_default_ip(filename) -> str:
        """
        PLC default ip read
        :param str filename: file name string
        :return: return PLC ip [str]
        """
        try:
            root = parse(filename).getroot()
        except FileNotFoundError:
            return ''

        if root.tag == 'default' and root[0].tag == 'ip':
            ip = root[0].text
            split_ip = [int(x) for x in ip.split('.')]
            if len(split_ip) == 4 and\
                    0 <= split_ip[0] <= 255 and\
                    0 <= split_ip[1] <= 255 and\
                    0 <= split_ip[2] <= 255 and\
                    0 <= split_ip[3] <= 255:
                return ip

        raise PLC_ConfigXML_Exception


if __name__ == '__main__':
    print(PLC_Config.read_plc_config('config.xml'))
    print(PLC_Config.read_plc_default_ip('default.xml'))
