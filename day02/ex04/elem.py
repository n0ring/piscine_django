#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().__str__()\
            .replace('"', '&quot;')\
            .replace('>', '&gt;')\
            .replace('<', '&lt;')\
            .replace('\n', '\n<br />\n')


class Elem:
    """
    ValidationError is a Exception sub class
    """

    class ValidationError(Exception):
        def __init__(self, ) -> None:
            super().__init__('Incorrect params for Elem class')


    """
    Elem will permit us to represent our HTML elements.
    """

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        if content is not None and not self.check_type(content):
            raise self.ValidationError()
        if tag_type != 'double' and tag_type != 'simple':
            raise self.ValidationError()
        self.tag = tag
        self.attr = attr
        self.content = []
        self.tag_type = tag_type

        if type(content) == list:
            self.content = content
        elif content is not None: 
            self.content.append(content)

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = ''
        if self.tag_type == 'double':
            result = f'<{self.tag}{self.__make_attr()}>{ self.__make_content() }</{self.tag}>'
        elif self.tag_type == 'simple':
            result = f'<{self.tag}{self.__make_attr()}>'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        result = ''
        for elem in self.content:
            if len(str(elem)) > 0:
                result += str(elem)
                result += '\n'
        els = result.strip().splitlines()
        if len(els) == 0:
            return ''
        string = '\n'
        for el in els:
            string += ('  ' + el + '\n')
        return string

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


def main():
    html = Elem('html')
    head  = Elem('head')
    body = Elem('body')
    body.add_content(Elem('h1', content=Text('Oh no, not again!')))
    body.add_content(Elem('img', attr={'src' : 'http://i.imgur.com/pfp3T.jpg"'}, tag_type='simple'))
    head.add_content(Elem('title', content=Text('Hello ground!')))
    html.add_content(head)
    html.add_content(body)
    print(html)


if __name__ == '__main__':
    main()
