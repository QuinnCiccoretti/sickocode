import language_check
tool = language_check.LanguageTool('en-US')

def fix_grammar(s):
    matches = tool.check(s)
    print(len(matches))
    return language_check.correct(s, matches)

text = u'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
sys.stdout.write(fix_grammar(text))
