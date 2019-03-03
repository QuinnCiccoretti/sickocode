import language_check
tool = language_check.LanguageTool('en-US')

<<<<<<< HEAD

def fix_grammar(s):
    matches = tool.check(s)
    print(len(matches))
    return language_check.correct(s, matches)
=======
def fix_grammar(str):
    matches = tool.check(str)
    # print(len(matches))
    return language_check.correct(str, matches)
>>>>>>> 4ea57dc2fb2bd04a0154c3c468b0612b58579e99

text = u'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
sys.stdout.write(fix_grammar(text))
