import os
from xml.etree import ElementTree


class CompareResult(object):
    def __init__(self):
        pass


def compare(modxmlpath, orixmlpath=None):
    modxml = ElementTree.parse(modxmlpath)
    if orixmlpath:
        orixml = ElementTree.parse(orixmlpath)
    for node in modxml.getroot():
        for child in list(node):
            print(child.attrib["name"])

    pass
