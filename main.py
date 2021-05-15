import PySimpleGUI as gui
import periodictable as pt


gui.theme("Black")
global_font = "Ariel 30"
layout = [
    [
        gui.Text("Welcome to Calculator",
                 font= global_font,
                 justification='centre')
    ],
    [
        gui.Text("Choose your Mode",
                 font= global_font,
                 justification='centre')
    ],
    [
        gui.Text("1.", font= global_font),
        gui.Button('Periodic Table', size=(50, 1))
    ],
]

win = gui.Window("Calculator", layout = layout)

while True:
    event, values = win.read(timeout = 10000)

    if event in (None, 'Exit'):
        win.close()
        break

    if event == 'Periodic Table':

        s_colour = '#48D1CC'
        p_colour = '#00FF7F'
        d_colour = '#1E90FF'
        f_colour = '#FF0000'

        periodictablelayout = [
            #1st period
            [
                gui.Button('H', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('He', font = global_font, size=(1, 1), button_color=('', p_colour)),
            ],
            #2nd period
            [
                gui.Button('Li', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('Be', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('',font = global_font, size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('B', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('C', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('N', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('O', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('F', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Ne', font = global_font, size=(1, 1), button_color=('', p_colour)),
            ],
            #3rd period
            [
                gui.Button('Na', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('Mg', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', font = global_font, size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('',font = global_font, size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('Al', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Si', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('P', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('S', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Cl', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Ar', font = global_font, size=(1, 1), button_color=('', p_colour))
            ],
            #4th period
            [
                gui.Button('K', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('Ca', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('Sc', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ti', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('V', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Cr', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Mn', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Fe', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Co', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ni', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Cu', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Zn', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ga', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Ge', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('As', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Se', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Br', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Kr', font = global_font, size=(1, 1), button_color=('', p_colour)),
            ],
            #5th period
            [
                gui.Button('Rb', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('Sr', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('Y', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Zr', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Nb', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Mo', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Tc', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ru', font = global_font, size=(1,1), button_color=('', d_colour)),
                gui.Button('Rh', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Pd', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ag', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Cd', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('In', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Sn', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Sb', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Te', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('I', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Xe', font = global_font, size=(1, 1), button_color=('', p_colour))
            ],
                #6th period
            [
                gui.Button('Cs', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('Ba', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('La', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Hf', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ta', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('W', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Re', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Os', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ir', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Pt', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Au', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Hg', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Tl', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Pb', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Bi', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Po', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('At', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Rn', font = global_font, size=(1, 1), button_color=('', p_colour))
            ],
            #7th period
            [
                gui.Button('Fr', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('Ra', font = global_font, size=(1, 1), button_color=('', s_colour)),
                gui.Button('Ac', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Rf', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Db', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Sg', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Bh', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Hs', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Mt', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ds', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Rg', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Cn', font = global_font, size=(1, 1), button_color=('', d_colour)),
                gui.Button('Nh', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Fl', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Mc', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Lv', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Ts', font = global_font, size=(1, 1), button_color=('', p_colour)),
                gui.Button('Og', font = global_font, size=(1, 1), button_color=('', p_colour))
            ],
            #lanthanide series
            [
                gui.Button('',font = global_font, size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('',font = global_font, size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('Ce', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Pr', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Nd', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Pm', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Sm', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Eu', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Gd', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Tb', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Dy', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Ho', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Er', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Tm', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Yb', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Lu', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('',font = global_font, size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('',font = global_font, size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
            ],
                #actinide series
            [
                gui.Button('',font = global_font, size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),gui.Button('',font = global_font, size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('Th', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Pa', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('U', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Np', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Pu', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Am', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Cm', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Bk', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Cr', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Es', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Fm', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Md', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('No', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('Lr', font = global_font, size=(1, 1), button_color=('', f_colour)),
                gui.Button('',font = global_font, size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('',font = global_font, size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
            ]
        ]        
        
        
        win.Hide()


        win1 = gui.Window("Periodic Table", layout = periodictablelayout)
        

        while True:
            event1, values1 = win1.read(timeout = 10000)

            if event1 in (None, 'Exit'):
                win1.close()
                win.UnHide()
                break

            if event1 in [str(elem) for elem in pt.elements]:
                elem = eval(f"pt.{event1}")
                info_win_layout = [
                    [
                        gui.Listbox(values=['name', 'number', 'symbol','mass', 'density', 'covalent_radius', 'interatomic_distance', 'ions', 'charge', 'isotopes', ], size=(30, 10), key = 'List'),
                        gui.Multiline( size = (30,10), font = global_font, key = 'info', do_not_clear=False, disabled=True)
                    ],
                    [
                        gui.Ok(size = (20, 2)), gui.Text("               "), gui.Exit(size = (20, 2))
                    ]

                ]
                
                

                info_win = gui.Window(str(elem), layout = info_win_layout)

                while True:
                    event1_info, values1_info = info_win.read(timeout = 10000)

                    if event1_info in (None, 'Exit'):
                        info_win.close()
                        break

                    
                    
                    if event1_info == "Ok":

                        line = ''

                        properties = info_win['List'].get()

                        for property in properties:
                            line += str('\n' + property + ' : ' + str(eval(f'elem.{property}')))
                        

                        info_win['info'].update(line)               
