import os
from xml.etree import ElementTree
from xml.etree.ElementTree import ElementTree


class CompareResult(object):
    def __init__(self):
        pass

def compare(mod_xml_path, ori_xml_path):
    mod_xml = ElementTree.parse(mod_xml_path)
    ori_xml = ElementTree.parse(ori_xml_path)
    _compare_node(mod_xml, ori_xml)


def _compare_node(mod_xml: ElementTree, ori_xml: ElementTree):
    if mod_xml.getroot() and ori_xml.getroot():
        mod_node_list = list(mod_xml.getroot())
        ori_node_list = list(ori_xml.getroot())
        if mod_node_list and ori_node_list:
            for mode_node in mod_node_list:
                if not mode_node in ori_node_list:
                    pass
    pass
