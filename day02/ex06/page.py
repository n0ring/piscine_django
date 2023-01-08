from elements import *

class Page:
	def __init__(self, root: Elem) -> None:
		self.root = root
		self.valid_nodes = [Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td , Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text]
		self.contains_dict = {
			Html: [Head, Body],
			Head: [Title],
			Body: [H1, H2, Div, Table, Ul, Ol, Span, Text],
			Div: [H1, H2, Div, Table, Ul, Ol, Span, Text],
			Title: [Text],
			H1: [Text],
			H2: [Text],
			Li: [Text],
			Tr: [Th, Td],
			Th: [Text],
			Td: [Text],
			P: [Text],
			Span: [P, Text],
			Ul: [Li],
			Ol: [Li],
			Table: [Tr]
		}

	def is_valid(self) -> bool:
		return self.__traverse(self.root)

	def __is_node_in_list(self, node: Elem) -> bool:
		if node.__class__ in self.valid_nodes:
			return True
		return False

	def __traverse(self, root: Elem):
		if root is None: 
			return True
		if self.__is_node_in_list(root) is False:
			return False
		if self.__check_classes(root, Html) and self.__check_html_tag(root) == False:
			return False
		if self.__check_classes(root, Head) and self.__check_contain_only(root, Title) == False:
			return False
		if root.__class__ in [Title, H1, H2, Li, Th, Td] and self.__check_contain_only(root, Text) == False:
			return False
		if root.__class__ in [Ol, Ul, Table, Tr] and len(root.content) < 1:
			return False
		if self.__check_classes(root, Tr) and self.__check_tr_contains(root) == False:
			return False
		for content_el in root.content:
			if content_el.__class__ not in self.contains_dict[root.__class__]:
				return False
			if isinstance(content_el, Elem):
				if self.__traverse(content_el) == False:
					return False
		return True
	
	def __check_classes(self, a: Elem, b: Elem) -> bool:
		return a.__class__ == b

	def __check_html_tag(self, el: Elem):
		if len(el.content) != 2:
			return False
		if self.__check_classes(el.content[0], Head) == False:
			return False
		if self.__check_classes(el.content[1], Body) == False:
			return False
		return True
	
	def __check_contain_only(self, el: Elem, must_contain: Elem):
		if len(el.content) != 1:
			return False
		if self.__check_classes(el.content[0], must_contain) == False:
			return False
		return True
	
	def __check_tr_contains(self, el: Elem):
		class_type = el.content[0].__class__
		for inner_el in el.content:
			if class_type != inner_el.__class__:
				return False
		return True

	def __str__(self) -> str:
		res = ''
		if self.__check_classes(self.root, Html):
			res += '<!DOCTYPE html>\n'
		return res + str(self.root)

	def write_to_file(self, filename: str):
		try:
			with open(filename, 'w') as output_file:
				output_file.write(str(self))
		except Exception as exp: 
			print(exp)

def valid_test():
	page = Page(
		Html(
			[
			Head(
				Title(
					Text('123123')
				)
			),
			Body(
				[
					Ol(Li(Text('123123'))),
					Table(Tr(Td(Text('sdfasdf'))))
				]
			)]
		)
	)

	assert page.is_valid() == True
	page.write_to_file('index.html')


def invalid_test_html():
	page = Page(
		Html(
			Body(),
			Head()
		)
	)
	assert page.is_valid() == False


def invalid_test_another_el():
	page = Page(
		Html(
			'some invalid text (because it is not a class Text'
		)
	)
	assert page.is_valid() == False


def invalid_test_head():
	page_no_title = Page(
		Html(
			Head()
		)
	)
	page_other_than_title = Page(
		Html(
			Head(Div())
		)
	)
	page_two_titles = Page(
		Html(
			Head(
				[Title(), Title()]
			)
		)
	)
	assert page_no_title.is_valid() == False
	assert page_other_than_title.is_valid() == False
	assert page_two_titles.is_valid() == False


def invalid_test_body_div():
	page_body_bad_els = Page(
		Html(
			Body(
				Head()
			)
		)
	)
	page_div_bad_els = Page(
		Html(
			Body(
				Div(
					Head()
				)
			)
		)
	)
	assert page_body_bad_els.is_valid() == False
	assert page_div_bad_els.is_valid() == False


def invalid_test_for_only_text():
	page_not_only_text = Page(
		Html(
			Head(
				Title(Div())
			)
		)
	)
	page_not_only_text2 = Page(
		Html(
			Body(
				Ul(
					Li(Text(Div()))
				)
			)
		)
	)
	page_not_only_text3 = Page(
		Html(
			Body(
				P(
					Div()
				)
			)
		)
	)
	page_not_only_text4 = Page(
		Html(
			Body(
				Span(
					Div()
				)
			)
		)
	)

	assert page_not_only_text.is_valid() == False
	assert page_not_only_text2.is_valid() == False
	assert page_not_only_text3.is_valid() == False
	assert page_not_only_text4.is_valid() == False


def invalid_test_lists():
	page_not_li = Page(
		Html(
			Body(
				Ol(

				)
			)
		)
	)
	assert page_not_li.is_valid() == False


def ivalid_test_table():
	page_table_with_no_tr = Page(
		Html(
			Body(
				Table(
					Td()
				)
			)
		)
	)
	page_table_with_td_and_th = Page(
		Html(
			Body(
				Table(
					[Td(), Th()]
				)
			)
		)
	)
	assert page_table_with_td_and_th.is_valid() == False



def main():
	valid_test()
	invalid_test_html()
	invalid_test_head()
	invalid_test_body_div()
	invalid_test_for_only_text()
	invalid_test_lists()
	ivalid_test_table()
	print("All test good")


if __name__ == '__main__':
	main()