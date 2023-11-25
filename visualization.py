data = [
    {'https://en.wikipedia.org/wiki/Omnipotence': 10},
    {'https://plato.stanford.edu/entries/omnipotence/': 10},
    {'https://www.newworldencyclopedia.org/entry/Omnipotence': 8},
    {'https://www.newadvent.org/cathen/11251c.htm': 7},
    {'https://www.biblestudytools.com/bible-study/topical-studies/what-does-it-mean-that-god-is-omnipotent-omnipotence.html': 5},
    {'https://plato.stanford.edu/Archives/Sum2019/Entries/omnipotence/': 5},
    {'https://heirtothestars.com/omnipotence/': 5},
    {'https://www.jstor.org/stable/23260033': 4},
    {'https://en.wikipedia.org/wiki/Crataegus': 4},
    {'https://brainly.in/question/52063290': 4},
    {'https://biblehub.com/topical/t/thousand-fold.htm': 4},
    {'https://www.biblestudytools.com/classics/warfield-the-power-of-god-unto-salvation/the-paradox-of-omnipotence.html': 3},
    {'https://www.freesundayschoollessons.org/systematic-theology/attributes-of-god-lesson-3-god-is-omnipotent/': 3},
    {'https://whatibelievethisweek.com/omnipotence-and-the-infinite-attribute-are-these-ideas-coherent/': 3},
    {'https://en.wikipedia.org/wiki/Crataegus_monogyna': 3},
    {'https://thecontentauthority.com/blog/eternal-vs-imperishable': 2},
    {'https://www.gotquestions.org/God-omnipotent.html': 2},
    {'https://cslectures.org/palmer/cs-the-science-of-omnipotent-mind-2-palmer.htm': 2},
    {'https://www.vocabulary.com/dictionary/omnipotent': 2},
    {'https://qrius.com/explained-when-an-unstoppable-force-meets-an-immovable-object/': 1},
    {'https://powerlisting.fandom.com/wiki/Omni-Protection': 1},
    {'https://www.facebook.com/stccbelleview/videos/daily-mass-devotion-for-november-14-2023/360562019963564/': 1}]


import pandas as pd
links = [list(entry.keys())[0] for entry in data]
counts = [list(entry.values())[0] for entry in data]

# Create a DataFrame from the extracted data
df = pd.DataFrame({'links': links, 'counts': counts})
df.to_excel('output.xlsx', index=False)