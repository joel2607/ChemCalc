import PySimpleGUI as gui
import periodictable as pt
import chemlib as c


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
    [
        gui.Text("2."),
        gui.Button('Compounds', size=(50,1))
    ],
    [
        gui.Text("3."),
        gui.Button('Reactions', size=(50,1))
    ],
##    [
##        gui.Text("4."),
##        gui.Button('Instructions',size = (50,1))
##    ]
]


win = gui.Window("Calculator", layout = layout, size = (500,300))
while True:
    event, values = win.read(timeout = 10000)

    if event in (None, 'Exit'):
        win.close()
        break

    #PeriodicTable-Window

    if event == 'Periodic Table':

        s_colour = '#48D1CC'
        p_colour = '#00FF7F'
        d_colour = '#1E90FF'
        f_colour = '#FF0000'

        periodictablelayout = [
            #1st period
            [
                gui.Button('H', size=(2, 1), button_color=('', s_colour)),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('He', size=(2, 1), button_color=('', p_colour)),
            ],
            #2nd period
            [
                gui.Button('Li', size=(2, 1), button_color=('', s_colour)),
                gui.Button('Be', size=(2, 1), button_color=('', s_colour)),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('B', size=(2, 1), button_color=('', p_colour)),
                gui.Button('C', size=(2, 1), button_color=('', p_colour)),
                gui.Button('N', size=(2, 1), button_color=('', p_colour)),
                gui.Button('O', size=(2, 1), button_color=('', p_colour)),
                gui.Button('F', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Ne', size=(2, 1), button_color=('', p_colour)),
            ],
            #3rd period
            [
                gui.Button('Na', size=(2, 1), button_color=('', s_colour)),
                gui.Button('Mg', size=(2, 1), button_color=('', s_colour)),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('', size=(2, 1), button_color=(gui.theme_background_color(), gui.theme_background_color())),
                gui.Button('Al', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Si', size=(2, 1), button_color=('', p_colour)),
                gui.Button('P', size=(2, 1), button_color=('', p_colour)),
                gui.Button('S', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Cl', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Ar', size=(2, 1), button_color=('', p_colour))
            ],
            #4th period
            [
                gui.Button('K', size=(2, 1), button_color=('', s_colour)),
                gui.Button('Ca', size=(2, 1), button_color=('', s_colour)),
                gui.Button('Sc', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Ti', size=(2, 1), button_color=('', d_colour)),
                gui.Button('V', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Cr', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Mn', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Fe', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Co', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Ni', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Cu', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Zn', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Ga', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Ge', size=(2, 1), button_color=('', p_colour)),
                gui.Button('As', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Se', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Br', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Kr', size=(2, 1), button_color=('', p_colour)),
            ],
            #5th period
            [
                gui.Button('Rb', size=(2, 1), button_color=('', s_colour)),
                gui.Button('Sr', size=(2, 1), button_color=('', s_colour)),
                gui.Button('Y', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Zr', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Nb', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Mo', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Tc', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Ru', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Rh', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Pd', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Ag', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Cd', size=(2, 1), button_color=('', d_colour)),
                gui.Button('In', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Sn', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Sb', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Te', size=(2, 1), button_color=('', p_colour)),
                gui.Button('I', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Xe', size=(2, 1), button_color=('', p_colour))
            ],
                #6th period
            [
                gui.Button('Cs', size=(2, 1), button_color=('', s_colour)),
                gui.Button('Ba', size=(2, 1), button_color=('', s_colour)),
                gui.Button('La', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Hf', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Ta', size=(2, 1), button_color=('', d_colour)),
                gui.Button('W', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Re', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Os', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Ir', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Pt', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Au', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Hg', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Tl', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Pb', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Bi', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Po', size=(2, 1), button_color=('', p_colour)),
                gui.Button('At', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Rn', size=(2, 1), button_color=('', p_colour))
            ],
            #7th period
            [
                gui.Button('Fr', size=(2, 1), button_color=('', s_colour)),
                gui.Button('Ra', size=(2, 1), button_color=('', s_colour)),
                gui.Button('Ac', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Rf', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Db', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Sg', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Bh', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Hs', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Mt', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Ds', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Rg', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Cn', size=(2, 1), button_color=('', d_colour)),
                gui.Button('Nh', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Fl', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Mc', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Lv', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Ts', size=(2, 1), button_color=('', p_colour)),
                gui.Button('Og', size=(2, 1), button_color=('', p_colour))
            ],
            #lanthanide series
            [
                gui.Button('', size=(2, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('', size=(2, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('Ce', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Pr', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Nd', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Pm', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Sm', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Eu', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Gd', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Tb', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Dy', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Ho', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Er', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Tm', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Yb', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Lu', size=(2, 1), button_color=('', f_colour)),
                gui.Button('', size=(2, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('', size=(2, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
            ],
                #actinide series
            [
                gui.Button('', size=(2, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),gui.Button('', size=(2, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('Th', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Pa', size=(2, 1), button_color=('', f_colour)),
                gui.Button('U', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Np', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Pu', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Am', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Cm', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Bk', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Cr', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Es', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Fm', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Md', size=(2, 1), button_color=('', f_colour)),
                gui.Button('No', size=(2, 1), button_color=('', f_colour)),
                gui.Button('Lr', size=(2, 1), button_color=('', f_colour)),
                gui.Button('', size=(2, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
                gui.Button('', size=(2, 1),button_color=(gui.theme_background_color(),gui.theme_background_color())),
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

                elem = c.Element(event1)
                #txt = f"name : {elem.name} \nnumber : {elem.number} \nsymbol : {elem.symbol} \nmass : {elem.mass} \ndensity : {elem.density} \ncovalent radius : {elem.covalent_radius} \ninteratomic distance : {elem.interatomic_distance} \nions : {elem.ions} \ncharge : {elem.charge} \nisotopes : {elem.isotopes} \n"

                #Periodic Table InfoBox
                laycol = [
                        [gui.Text("Element:"),gui.Text(elem.Element)],
                        [gui.Text("Symbol:"),gui.Text(elem.Symbol)],
                        [gui.Text("Atomic Number:"),gui.Text(int(elem.AtomicNumber))],
                        [gui.Text("Atomic Mass:"),gui.Text(elem.AtomicMass)],
                        [gui.Text("Period:"),gui.Text(int(elem.Period))],
                        [gui.Text("Group:"),gui.Text(int(elem.Group))],
                        [gui.Text("Mass Number:"),gui.Text(elem.MassNumber)],
                        [gui.Text("Neutrons:"),gui.Text(elem.Neutrons)],
                        [gui.Text("Protons:"),gui.Text(elem.Protons)],
                        [gui.Text("Electrons:"),gui.Text(elem.Electrons)],
                        [gui.Text("Phase:"),gui.Text(elem.Phase)],
                        [gui.Text("Radioactive:"),gui.Text(elem.Radioactive)],
                        [gui.Text("Natural:"),gui.Text(elem.Natural)],
                        [gui.Text("Metal:"),gui.Text(elem.Metal)],
                        [gui.Text("Non-Metal:"),gui.Text(elem.Nonmetal)],
                        [gui.Text("Metalloid:"),gui.Text(elem.Metalloid)],
                        [gui.Text("Type:"),gui.Text(elem.Type)],
                        [gui.Text("Atomic Radius:"),gui.Text(elem.AtomicRadius)],
                        [gui.Text("First Ionization:"),gui.Text(elem.FirstIonization)],
                        [gui.Text("Density:"),gui.Text(elem.Density)],
                        [gui.Text("Melting Point:"),gui.Text(elem.MeltingPoint)],
                        [gui.Text("Boiling Point:"),gui.Text(elem.BoilingPoint)],
                        [gui.Text("Isotopes:"),gui.Text(elem.Isotopes)],
                        [gui.Text("Discovered by:"),gui.Text(elem.Discoverer)],
                        [gui.Text("Year:"),gui.Text(elem.Year)],
                        [gui.Text("Specific Heat:"),gui.Text(elem.SpecificHeat)],
                        [gui.Text("Shells:"),gui.Text(elem.Shells)],
                        [gui.Text("Valency:"),gui.Text(elem.Valence)],
                        [gui.Text("Electronic Configuration:"),gui.Text(elem.Config)],
                        ]
                info_win_layout = [
                    [gui.Column(laycol,scrollable = True,)
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

    #Compounds-Window

    if event == "Compounds":
        compoundlayout = [

            [gui.Text('Enter the Compound (Formula)', size = (30,1))],
            [gui.InputText(key = "molecule", size = (30,1))],
            [gui.Button('Molecular mass', size = (25, 1))],
            [gui.Button('Occurences', size = (25, 1))],
            [gui.Button('Composition by mass', size = (25, 1))],
            [gui.Button('Stoichiometry', size = (25, 1))],
            [gui.Button('Cancel', size = (25, 1))]

            ]

        win.Hide()
        win2 = gui.Window("Compounds", layout = compoundlayout)

        while True:

                event2, values2 = win2.read(timeout = 10000)

                if event2 in (None, 'cancel'):
                    win2.close()
                    win.UnHide()
                    break

                if event2 == 'Molecular mass':

                    try:
                        mole_mass = c.Compound(values2['molecule']).molar_mass()

                    except IndexError:
                        gui.popup('Invalid input.',keep_on_top=True)
                    else:
                        gui.popup('The molecular mass =', mole_mass, keep_on_top=True)

                if event2 == 'Occurences':

                    try:
                        Occ=c.Compound(values2['molecule']).occurences
                    except AttributeError:
                        gui.popup('Invalid input.')
                    else:
                        gui.popup('The occurences are:', Occ, keep_on_top=True )

                if event2 == 'Composition by mass':
                    try:
                        txt = ''
                        for i in c.Compound(values2['molecule']).occurences.keys():
                            comp = c.Compound(values2['molecule']).percentage_by_mass(i)
                            txt += f'Composition of element {i} is: {comp} \n'

                    except IndexError:
                        gui.popup('Invalid input.')
                    else:
                        gui.popup(txt)

                if event2 == 'Stoichiometry':
                    try:
                        molecule = c.Compound(values2['molecule'])

                    except IndexError:
                        gui.popup("Enter Valid Formula")

                    else:
                        colA = [
                                [gui.Text("Amount")],
                                [gui.Input(size=(20,1), key= 'amt' )],
                            ]

                        colB = [
                                [gui.Text("Unit of measurement:")],
                                [gui.Radio("Grams", "Units", default = True, key='grm')],
                                [gui.Radio("Moles", "Units", key='mol')],
                                [gui.Radio("Molecules", "Units", key='mole')]
                            ]

                        stoichlayout = [
                                [gui.Text("Stoichiometry")],
                                [gui.Column(colA,justification='left'),gui.Column(colB,justification='right')],
                                [gui.Button("Apply"), gui.Button("Cancel")],
                            ]

                        win2.Hide()
                        winstoich= gui.Window("Stoichiometry",layout = stoichlayout)

                        while True:
                            eventstoich, valuesstoich = winstoich.read(timeout = 10000)

                            try:
                                amt = int(valuesstoich['amt'])
                            except ValueError:
                                gui.Popup("Enter a numerical Value.")
                            else:

                                if valuesstoich['grm']:
                                    stoich = molecule.get_amounts(grams= amt)

                                elif valuesstoich['mol']:
                                    stoich = molecule.get_amounts(moles= amt)

                                elif valuesstoich['mole']:
                                    stoich = molecule.get_amounts(molecules= amt)


                                if eventstoich=='Apply':
                                    stoichtxt = ''
                                    for k in stoich:
                                        stoichtxt += f'{stoich[k]} {k}\n'
                                    gui.popup(stoichtxt)

                                if eventstoich=='Cancel':
                                    winstoich.close()
                                    win2.UnHide()
                                    break




    #Reactions-Window

    if(event == "Reactions"):
        font3 = "Helvetica 20"
        col1 = [
            [gui.Text('Reactants:',font = font3)],

            [gui.Input(tooltip = "Enter reactant here", size = (20,1), key = "rinp",font = font3)],
            [gui.Button("Add Reactant",font = font3,key='update1'), gui.Button("Clear", font = font3,key='clear1')],
            [gui.Text("Your Reactants:", font = font3)],
            [gui.Multiline(disabled = True, size = (20,5), key = "reactants",font = font3, do_not_clear=False)],
            ]
        col2 = [
            [gui.Text('Products:',font = font3)],
            [gui.Input(tooltip = "Enter product here", size = (20,1), key = "pinp",font = font3)],
            [gui.Button("Add Product",font = font3, key='update2'), gui.Button("Clear", font = font3,key='clear2')],
            [gui.Text("Your Products:", font = font3)],
            [gui.Multiline(disabled = True, size = (20,5), key = "products",font = font3, do_not_clear=False)],
            ]
        reactionwindowlayout = [
			[gui.Column(col1,justification='left'), gui.Text('--->', font = 'Helvetica 40'),gui.Column(col2,justification='right')],
            [gui.Ok(font = font3), gui.Exit(font = font3)]
            ]
        win.Hide()
       	win3 = gui.Window("Reactions", layout = reactionwindowlayout)

        reactants = []
        products = []

        while True:
            event3, values3 = win3.read(timeout = 10000)

            if event3 in (None, 'Exit'):
                win3.close()
                win.UnHide()
                break

            if event3 == "update1":

                win3["rinp"].update('')
                try:
                    if values3["rinp"] not in ("Enter reactant here", ""):
                        reac = c.Compound(values3["rinp"])
                except IndexError:
                    gui.popup("Enter valid Molecular Formula.")
                else:
                    if values3["rinp"] not in ("Enter reactant here", ""):
                        reactants.append(reac)
                        win3["reactants"].print(reac)


            if event3 == "update2":
                win3["pinp"].update('')

                try:
                    if values3["pinp"] not in ("Enter product here", ""):
                        prod = c.Compound(values3["pinp"])
                except IndexError:
                    gui.popup("Enter valid Molecular Formula.")
                else:
                    if values3["pinp"] not in ("Enter product here", ""):
                        products.append(prod)
                        win3["products"].print(prod)

            if event3 == "clear1":
                win3["reactants"].update('')
                reactants = []

            if event3 == "clear2":
                win3["products"].update('')
                products = []

            #Reaction new-Window

            if event3 == "Ok":

                rxn = c.Reaction(reactants, products)
                reactionwindowlayout2 = [
                    [gui.Text("Your reaction is:", font = font3)],
                    [gui.Text(rxn,key='rxnbox',text_color='white', font = font3)],
                    [gui.Button("Balance", font = font3), gui.Button("Limiting Reagent", font = font3)],
                    ]
                win3.Hide()
                win31 = gui.Window("Reactions", layout = reactionwindowlayout2)

                while True:
                    event31, values31 = win31.read(timeout = 10000)

                    if event31 == None:
                        win31.close()
                        win3.UnHide()
                        reactants = []
                        products = []
                        win3["reactants"].update('')
                        win3["products"].update('')
                        break

                    #Balance Button
                    if event31 == "Balance":
                        if not rxn.is_balanced:
                            rxn.balance()
                            win31.Element('rxnbox').Update(value=rxn)
                        else:
                            gui.popup("Equation is Balanced")

                    #Limiting Reagent Window
                    if event31 == "Limiting Reagent":

                        col3=[
                            [gui.Text("Unit of Reagent:")],
                            [gui.Radio("Grams","Units",default = True,key='gm')],
                            [gui.Radio("Moles","Units",key='m')],
                            [gui.Radio("Molecules","Units",key='mol')],
                        ]
                        col4=[
                            [gui.Text("Amount")],
                            [gui.Text("Reactant 1:")],
                            [gui.Input(size=(20,1),key='R1')],
                            [gui.Text("Reactant 2:")],
                            [gui.Input(size=(20,1),key='R2')],
                        ]
                        lrlayout=[
                            [gui.Text("Limiting Reagent",justification='centre')],
                            [gui.Text(rxn,key='lrbox')],
                            [gui.Column(col3,justification='left'),gui.Column(col4,justification='right')],
                            [gui.Button("Apply")],
                            [gui.Text('            ',key='lr')],
                        ]

                        win31.close()
                        winlr = gui.Window("Reactions",layout = lrlayout)
                        if len(reactants)!=2 :
                            gui.popup("This function works only for reactions with two reactants")
                            win31.UnHide()
                            winlr.Close()

                        else:

                            while True:
                                eventlr, valueslr = winlr.read(timeout = 10000)

                                if valueslr['gm'] == True:
                                    type='grams'
                                elif valueslr['m'] == True:
                                    type='moles'
                                elif valueslr['mol'] == True:
                                    type='molecules'

                                try:
                                    if eventlr == 'Apply':
                                        x=float(valueslr['R1'])
                                        y=float(valueslr['R2'])
                                        lr = rxn.limiting_reagent(x, y, mode = type)
                                        winlr['lr'].Update(value=lr.formula)
                                except ValueError:
                                    gui.popup("Please enter a numerical value")

                                if eventlr == (None,'cancel'):
                                    winlr.close()
                                    win31.UnHide()
                                    break