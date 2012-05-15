from xlwt.Style import easyxf

__author__ = 'thacdu'

FIRST_COL = 6000
SECOND_COL = 10000

h1 = easyxf(
    'font:name Arial, bold on,height 1000 ;align: vert centre, horz center')
h2 = easyxf(
    'font:name Arial, bold on,height 1000 ;align: vert centre, horz center')
h3 = easyxf(
    'font:name Arial, bold on,height 400 ;align: vert centre, horz center')
h4 = easyxf(
    'font    :name Arial, bold on,height 260 ;align:wrap on, vert centre, horz center;'
    'borders : top thin ,right thin, left thin, bottom thin')
h5 = easyxf(
    'font:name Arial, bold on,height 240 ;align: wrap on, vert centre, horz center;'
    'borders : top thin ,right thin, left thin, bottom thin;'
    'pattern: pattern solid, fore_colour light_green;')
f1 = easyxf(
    'font: name Arial, height 220; align: wrap on, vert centre, horz center;'
)
f2 = easyxf(
    'font    :name Arial ,height 220 ;align:wrap on, vert centre, horz center;'
    'borders : top thin ,right thin, left thin, bottom thin')
