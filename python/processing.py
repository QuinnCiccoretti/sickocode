import language_check
tool = language_check.LanguageTool('en-US')


def fix_grammar(s):
    matches = tool.check(s)
    print(len(matches))
    return language_check.correct(s, matches)


text = u'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
sys.stdout.write(fix_grammar(text))

from datamuse import datamuse
api = datamuse.Datamuse()
orange_rhymes = api.words(rel_rhy='orange', max=5)
sys.stdout.write(orange_rhymes)
orange_near_rhymes = api.words(rel_nry='orange', max=5)
sys.stdout.write(orange_near_rhymes)

foo_complete = api.suggest(s='foo', max=10)
sys.stdout.write(foo_complete)
from datamuse import scripts
foo_df = scripts.dm_to_df(foo_complete)
sys.stdout.write(foo_df)
