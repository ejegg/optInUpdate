import pywikibot
import dumper

site = pywikibot.Site('commons')

with open('filenames.txt', 'r') as namesfile:
    for name in namesfile:
        imgpage = pywikibot.Page(site, name)
        entityid = 'M' + str(imgpage.pageid)
        wbquery = site._simple_request(
            action='wbgetentities',
            ids=entityid)
        result = wbquery.submit()
        entity = result['entities'][entityid]

        dumper.dump(result)
