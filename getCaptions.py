import pywikibot
import urllib.parse

site = pywikibot.Site('commons')

captions = {
    'en': {},
    'qqq': {}
}
with open('filenames.txt', 'r') as namesfile:
    for name in namesfile:
        name = name.rstrip()
        imgpage = pywikibot.Page(site, name)
        entityid = 'M' + str(imgpage.pageid)
        wbquery = site._simple_request(
            action='wbgetentities',
            ids=entityid)
        result = wbquery.submit()
        entity = result['entities'][entityid]
        if 'labels' in entity:
            for language in entity['labels']:
                if language not in captions:
                    captions[language] = {}
                captions[language][entityid] = entity['labels'][language]['value']
                if language == 'en':
                    url = 'https://commons.wikimedia.org/wiki/' + urllib.parse.unquote(name)
                    captions['qqq'][entityid] = 'Photo caption from commons for entity ' + entityid + \
                        ', can be translated at ' + url

for language in captions:
    filename = language + '.json'
    with open(filename, 'w') as i18nfile:
        for entityid in captions[language]:
            message = 'fundraisersubscribe-photo-caption-' + entityid
            value = captions[language][entityid]
            i18nfile.write('\t"' + message + '": "' + value + '",\n')

