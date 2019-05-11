import os

from google_images_search import GoogleImagesSearch

gis = GoogleImagesSearch('AIzaSyCcrhOwuC5TK_O18yjeSTCuXEHVxk-9LTQ', '005383774336154718355:xu2fzioh270')

partei_list = ['CDU', 'Alternative fuer Deutschland', 'Tierschutzpartei']

# define search params:
_search_params = {
    'q': 'wahlplakat 2019',
    'num': 2,
    'safe': 'off',
    'fileType': 'png',
    'searchType': 'image'
    # 'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow'
}

# search first, then download and resize afterwards
for partei in partei_list:

    _search_params.update({'q': partei + ' wahlplakat 2019'})

    picDir = '../Data/Raw/' + partei.replace(" ", "")

    if not os.path.exists(picDir):
        os.mkdir(picDir)

    gis.search(_search_params)
    for image in gis.results():
        image.download(picDir)
    gis.results().clear()
