import sublime_plugin

opening_glyph = '{[('
closing_glyph = '}])'


class BetterAutoIndentCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        pos = view.sel()[0].begin()
        offset = self.get_last_unmatched_opening_glyph(pos)
        padding = self.calculate_padding(offset)
        view.run_command('insert', {'characters': '\n' + ' ' * padding})

    def get_last_unmatched_opening_glyph(self, point):
        view = self.view
        pos = view.sel()[0].begin()
        lhs = view.substr(view.line(pos))[:view.rowcol(pos)[1]]
        count = {'(': 0, '{': 0, '[': 0}
        for i in range(len(lhs))[::-1]:
            print(i)
            token = lhs[i]
            if token in opening_glyph:
                count[token] += 1
                if(count[token] > 0):
                    # Do a conversion back to point format
                    offset = i + 1
                    # print('line column: ', offset)
                    return view.text_point(view.rowcol(pos)[0], offset)
            elif token in closing_glyph:
                count[self.reverse_glyph(token)] -= 1
        return None

    def calculate_padding(self, offset):
        ''' Returns the number of spaces that will need added after the newline
        and autoindent are done.'''
        if not offset:
            return 0
        view = self.view
        s = view.substr(view.line(offset))
        leading_spaces = len(s) - len(s.lstrip())
        return view.rowcol(offset)[1] - leading_spaces

    def reverse_glyph(self, c):
        if c == ']':
            return '['
        elif c == '}':
            return '{'
        elif c == ')':
            return '('
        elif c == '[':
            return ']'
        elif c == '{':
            return '}'
        elif c == '(':
            return ')'
        else:
            raise ValueError('Invalid token entered')
