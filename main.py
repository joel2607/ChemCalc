import PySimpleGUI as gui
import periodictable as pt


gui.theme("Black")
layout = [
    [
        gui.Text("Welcome to Calculator",
                 justification='centre')
    ],
    [
        gui.Text("Choose your Mode",
                 justification='centre')
    ],
    [
        gui.Text("1."),
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
                gui.Button('H', size=(1, 1), button_color=('', s_colour)),
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
                gui.Button('He', size=(1, 1), button_color=('', p_colour)),
            ],
            #2nd period
            [
                gui.Button('Li', size=(1, 1), button_color=('', s_colour)),
                gui.Button('Be', size=(1, 1), button_color=('', s_colour)),
                gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('B', size=(1, 1), button_color=('', p_colour)),
                gui.Button('C', size=(1, 1), button_color=('', p_colour)),
                gui.Button('N', size=(1, 1), button_color=('', p_colour)),
                gui.Button('O', size=(1, 1), button_color=('', p_colour)),
                gui.Button('F', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Ne', size=(1, 1), button_color=('', p_colour)),
            ],
            #3rd period
            [
                gui.Button('Na', size=(1, 1), button_color=('', s_colour)),
                gui.Button('Mg', size=(1, 1), button_color=('', s_colour)),
                gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1), button_color=(gui.theme_background_color(), gui.theme_background_color()))
                ,gui.Button('', size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('Al', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Si', size=(1, 1), button_color=('', p_colour)),
                gui.Button('P', size=(1, 1), button_color=('', p_colour)),
                gui.Button('S', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Cl', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Ar', size=(1, 1), button_color=('', p_colour))
            ],
            #4th period
            [
                gui.Button('K', size=(1, 1), button_color=('', s_colour)),
                gui.Button('Ca', size=(1, 1), button_color=('', s_colour)),
                gui.Button('Sc', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ti', size=(1, 1), button_color=('', d_colour)),
                gui.Button('V', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Cr', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Mn', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Fe', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Co', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ni', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Cu', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Zn', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ga', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Ge', size=(1, 1), button_color=('', p_colour)),
                gui.Button('As', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Se', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Br', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Kr', size=(1, 1), button_color=('', p_colour)),
            ],
            #5th period
            [
                gui.Button('Rb', size=(1, 1), button_color=('', s_colour)),
                gui.Button('Sr', size=(1, 1), button_color=('', s_colour)),
                gui.Button('Y', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Zr', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Nb', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Mo', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Tc', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ru', size=(1,1), button_color=('', d_colour)),
                gui.Button('Rh', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Pd', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ag', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Cd', size=(1, 1), button_color=('', d_colour)),
                gui.Button('In', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Sn', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Sb', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Te', size=(1, 1), button_color=('', p_colour)),
                gui.Button('I', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Xe', size=(1, 1), button_color=('', p_colour))
            ],
                #6th period
            [
                gui.Button('Cs', size=(1, 1), button_color=('', s_colour)),
                gui.Button('Ba', size=(1, 1), button_color=('', s_colour)),
                gui.Button('La', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Hf', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ta', size=(1, 1), button_color=('', d_colour)),
                gui.Button('W', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Re', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Os', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ir', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Pt', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Au', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Hg', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Tl', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Pb', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Bi', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Po', size=(1, 1), button_color=('', p_colour)),
                gui.Button('At', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Rn', size=(1, 1), button_color=('', p_colour))
            ],
            #7th period
            [
                gui.Button('Fr', size=(1, 1), button_color=('', s_colour)),
                gui.Button('Ra', size=(1, 1), button_color=('', s_colour)),
                gui.Button('Ac', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Rf', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Db', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Sg', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Bh', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Hs', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Mt', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Ds', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Rg', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Cn', size=(1, 1), button_color=('', d_colour)),
                gui.Button('Nh', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Fl', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Mc', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Lv', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Ts', size=(1, 1), button_color=('', p_colour)),
                gui.Button('Og', size=(1, 1), button_color=('', p_colour))
            ],
            #lanthanide series
            [
                gui.Button('', size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('', size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('Ce', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Pr', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Nd', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Pm', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Sm', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Eu', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Gd', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Tb', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Dy', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Ho', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Er', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Tm', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Yb', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Lu', size=(1, 1), button_color=('', f_colour)),
                gui.Button('', size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('', size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
            ],
                #actinide series
            [
                gui.Button('', size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),gui.Button('', size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('Th', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Pa', size=(1, 1), button_color=('', f_colour)),
                gui.Button('U', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Np', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Pu', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Am', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Cm', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Bk', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Cr', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Es', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Fm', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Md', size=(1, 1), button_color=('', f_colour)),
                gui.Button('No', size=(1, 1), button_color=('', f_colour)),
                gui.Button('Lr', size=(1, 1), button_color=('', f_colour)),
                gui.Button('', size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('', size=(1, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
            ]
        ]        
        
        win.Hide()
        loadingscreen = gui.Window("Loading...", layout = [[gui.Text("\n\n\t\tLoading...\t\t\n\n")]])


        win1 = gui.Window("Periodic Table", layout = periodictablelayout)

        loadingscreen.close()
        del loadingscreen
        

        while True:
            event1, values1 = win1.read(timeout = 10000)

            if event1 in (None, 'Exit'):
                win1.close()
                win.UnHide()
                break

            if event1 in [str(elem) for elem in pt.elements]:
                elem = eval(f"pt.{event1}")
                txt = "name : {elem.name} \nnumber : {elem.number} \nsymbol : {elem.symbol} \nmass : {elem.mass} \ndensity : {elem.density} \ncovalent radius : {elem.covalent_radius} \ninteratomic distance : {elem.interatomic_distance} \nions : {elem.ions} \ncharge : {elem.charge} \nisotopes : {elem.isotope} \n"

                info_win_layout = [
                    [
                        gui.Text(txt, size = (30,10))
                    ],
                    [
                        gui.Exit(size = (10, 1))
                    ]

                ]
                
                

                info_win = gui.Window(str(elem), layout = info_win_layout)

                while True:
                    
                    event1_info, values1_info = info_win.read(timeout = 10000)

                    if event1_info in (None, 'Exit'):
                        info_win.close()
                        break                    
                    
                        
                        


                    
                    

                    


