import PySimpleGUI as sg

label1 = sg.Text("Enter feet")
label2 = sg.Text("Enter inches")

input1 = sg.Input()
input2 = sg.Input()

button = sg.Button("Convert")
window = sg.Window("Converter" , layout = [[label1, input1], [label2, input2], [button]])
window.read()
window.close()