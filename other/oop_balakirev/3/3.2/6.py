class RenderList:
    def __init__(self, type_list):
        if type_list == 'ul':
            self.type_list = 'ul'
        elif type_list == 'ol':
            self.type_list = 'ol'
        else:
            self.type_list = 'ul'

    def __call__(self, lst):
        lst_new = [f'<li>{val}</li>\n' for val in lst]
        lst_ret = [f'<{self.type_list}>\n'] + lst_new + [f'</{self.type_list}>']
        return ''.join(lst_ret)


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
