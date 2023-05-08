import PySimpleGUI as sg

layout = [  [sg.Button( 'OK' , key = "santi" ) ],
            [sg.Button('Cancelar' , key= 'exit')] ]

window = sg.Window ( 'Un titulo ', layout, margins=(300,300),background_color= '#000')

while True:

    events, values = window.read();

    print ( f" evneto {events} valor {values}") 

    if ( events == 'exit' ) or ( events == sg.WIN_CLOSED ):

        break

    if ( events == 'santi' ):

        sg.popup('santi es un capo')