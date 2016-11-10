Better Auto Indent Sublime Text plugin
===============================================================================

An attempt to mirror the functionality of indent_to_bracket in sublime that
only works for parenthesis to '[' and '{' brackets/braces. This plugin is still
in development so there may be various issues you can run into.

The general idea is to indent arguments in a function call to the opening
bracket so that:

```
dict = {'a': 1, 'b': 2<enter>
```

aligns caret following way:

```
dict = {'a': 1, 'b': 2
        |
```

Installation Instructions
-------------------------------------------------------------------------------

1. Copy the better_auto_indent.py into your packages directory. On OS X this is
`~/Library/Application Support/Sublime Text 3/Packages/User`
2. Copy-Paste the *contents* of teh Defaults.sublime-keymap into your keymap
settings file. `Sublime Text > Prefernces > Key Bindings`
