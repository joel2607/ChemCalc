import PySimpleGUI as gui
import periodictable as pt
import layouts

gui.theme("Black")

#I have stored all the layouts in the layoutss.py file. Please refer to that for the same.

win = gui.Window("Calculator", layout = layouts.layout)

while True:
    event, values = win.read(timeout = 10000)

    if event in (None, 'Exit'):
        win.close()
        break

    if event == 'Periodic Table':

        win.Hide()

        win1 = gui.Window("Periodic Table", layout = layouts.periodictablelayout)
        

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
                        gui.Listbox(values=['name', 'number', 'symbol','mass', 'density', 'covalent_radius', 'interatomic_distance', 'ions', 'charge', 'isotopes', ], size=(30, 10)),
                        gui.Multiline( size = (30,10), key = 'info', do_not_clear=False, disabled=True)
                    ],

                ]
                info_win = gui.Window(str(elem), layout = info_win_layout)

                while True:
                    event1_info, values1_info = info_win.read(timeout = 10000)

                    if event1_info in (None, 'Exit'):
                        info_win.close()
                        del info_win
                        break
                    
                    

                    


