 import PySimpleGUI as gui

gui.theme("Black")

layout = [
    [
        gui.Text("Welcome to Calculator",
                 font='Timesnewroman',
                 justification='centre')
    ],
    [
        gui.Text("Choose your Mode",
                 font='Timesnewroman',
                 justification='centre')
    ],
    [
        gui.Text("1.", font='Timesnewroman'),
        gui.Button('Periodic Table', size=(50, 1))
    ],
]

periodictablelayout = [
    [
        gui.Button('H', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
        gui.Button('He', size=(1, 1), button_color=('', '#48D1CC')),
    ],
    [
        gui.Button('Li', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('Be', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
        gui.Button('',size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
        gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
        gui.Button('B', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('C', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('N', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('O', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('F', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Ne', size=(1, 1), button_color=('', '#00FF7F')),
    ],
    [
        gui.Button('Na', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('Mg', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
        ,gui.Button('',size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
        gui.Button('Al', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Si', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('P', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('S', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Cl', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Ar', size=(1, 1), button_color=('', '#00FF7F'))
    ],
    [
        gui.Button('K', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('Ca', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('Sc', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Ti', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('V', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Cr', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Mn', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Fe', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Co', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Ni', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Cu', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Zn', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Ga', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Ge', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('As', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Se', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Br', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Kr', size=(1, 1), button_color=('', '#00FF7F')),
    ],
    [
        gui.Button('Rb', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('Sr', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('Y', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Zr', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Nb', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Mo', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Tc', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Ru', size=(1,1), button_color=('', '#1E90FF')),
        gui.Button('Rh', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Pd', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Ag', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Cd', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('In', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Sn', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Sb', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Te', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('I', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Xe', size=(1, 1), button_color=('', '#00FF7F'))
    ],
    [
        gui.Button('Cs', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('Ba', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('La', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Hf', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Ta', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('W', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Re', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Os', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Ir', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Pt', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Au', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Hg', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Tl', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Pb', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Bi', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Po', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('At', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Rn', size=(1, 1), button_color=('', '#00FF7F'))
    ],
    [
        gui.Button('Fr', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('Ra', size=(1, 1), button_color=('', '#48D1CC')),
        gui.Button('Ac', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Rf', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Db', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Sg', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Bh', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Hs', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Mt', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Ds', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Rg', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Cn', size=(1, 1), button_color=('', '#1E90FF')),
        gui.Button('Nh', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Fl', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Mc', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Lv', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Ts', size=(1, 1), button_color=('', '#00FF7F')),
        gui.Button('Og', size=(1, 1), button_color=('', '#00FF7F'))
    ],
    [
        gui.Button('',size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
        gui.Button('',size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
        gui.Button('Ce', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Pr', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Nd', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Pm', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Sm', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Eu', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Gd', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Tb', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Dy', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Ho', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Er', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Tm', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Yb', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Lu', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('',size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
        gui.Button('',size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
    ],
    [
        gui.Button('',size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),gui.Button('',size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
        gui.Button('Th', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Pa', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('U', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Np', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Pu', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Am', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Cm', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Bk', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Cr', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Es', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Fm', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Md', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('No', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('Lr', size=(1, 1), button_color=('', '#FF0000')),
        gui.Button('',size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
        gui.Button('',size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
    ]
]




