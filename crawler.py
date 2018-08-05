import re


class htmltag:
    def __init__(self, tag='', text='', attrib={}):
        self.tag = tag
        self.text = text
        self.attrib = attrib
        self.child = None
        self.textChild = {}

    def append(self, child):
        self.child = child

    def serialize(self):
        attribs = ""
        for akey, aval in self.attrib.iteritems():
            attribs += ''' %s="%s"''' % (akey, aval)
        thisnode = '''<%s%s>%s</%s>'''
        if self.child is None:
            self.textHasChild()
            if not self.textChild:
                return thisnode % (self.tag, attribs, self.text, self.tag)
            else:
                return thisnode % (self.tag, attribs, self.textChild, self.tag)
        else:
            return thisnode % (self.tag, attribs, self.child.serialize(), self.tag)

    def textHasChild(self, incoming=None):
        # textpos - position of the textchild within text
        # textchild - htmltag object within textchild
        if incoming: self.text = incoming  # for testing only
        selftextlist = list(self.text)
        selftextdict = {}
        # 1 Find the text children
        reg = re.compile('(<[^>]*>[^<]+</[^>]*>)')
        for pos in reg.finditer(self.text):
            # print pos.group(), pos.start()
            if pos.start() not in selftextdict:
                selftextdict[pos.start()] = htmltag(pos.group())
        # 2 Remove them from text
        for pos in sorted(selftextdict.iterkeys(), reverse=True):
            # print pos,selftextdict[pos]
            selftextlist[pos:pos + len(selftextdict[pos])] = ''
        # 3 Store info in textChild dict
        self.text = ''.join(selftextlist)
        # print self.text
        self.textChild = selftextdict

    def deserialize(self, string):  # convert string to htmltag object
        pass


def print_script_tags(dependencies, rootfile):
    dps = ''
    for dependency in dependencies:
        dps += '<script src=' + dependency + ' />'
    return dps


def dependencies(file):
    return ['bar.js', 'baz.js', 'main.js']


def test():
    root = htmltag('html')
    root.textHasChild(
        'Birthday <span style="color:red">Party</span>! is here. And I am <span style="color:red">Ofcourse</span> too')


# root = htmltag('html')
# root.append(htmltag('Title','Heading',{'class':'hero','color':'blue'}))
# print root
# Q3
# d = dependencies('foo.js') #returns ['bar.js', 'baz.js', 'main.js']
# d += dependencies('bar.js') #returns ['b1.js','b2.js','b3.js',]
# rootfile = 'index.html'
# print print_script_tags(d,rootfile)

def main():
    test()


if __name__ == '__main__':
    main()