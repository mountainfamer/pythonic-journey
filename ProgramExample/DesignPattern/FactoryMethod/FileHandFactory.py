# !/usr/bin/env python
# coding:utf-8
import xml.etree.ElementTree as etree
import json


class JSONConnector(object):

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector(object):

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith('json'):
        connect = JSONConnector
    elif filepath.endswith('xml'):
        connect = XMLConnector
    else:
        raise ValueError('cannot connect to %s' % filepath)
    return connect(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print ve
    return factory


def main():
    sqlite_factory = connect_to('data/person.sq3')
    print

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))

    print 'found:%d persons' % (len(liars))

    for liar in liars:
        print 'first name:%s' % liar.find('firstName').text
        print 'last name name:%s' % liar.find('lastName').text
        # [print ('phone number (%s)' p.attrib['tyhpe'], p.text) for p in liar.find('phoneNumbers')]
    print

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print 'find %d donuts.' % len(json_data)

    for donut in json_data:
        print 'name: %s, price: %s' % (donut['name'], donut['ppu'])
        # [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]


if __name__ == '__main__':
    main()