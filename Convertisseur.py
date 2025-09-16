from tkinter import * 
import tkinter as tk
from tkinter import ttk 
import time 
from PIL import Image, ImageTk


#COLOR:
red = "#5f0916"
dark_green = "#3b4843"
light_green = "#536355"

#FONT: 
font_title = ('comic sans', 18)
font_txt = ('comic sans', 13)
font_txt_btn = ('comic sans', 11)

#WINDOW CONFIGURATION
window = Tk()
window.geometry("600x400")

window.minsize(500,300)
window.maxsize(700, 500)

window['bg'] = dark_green

window.columnconfigure(0, weight= 1)
window.columnconfigure(1, weight= 2)
window.columnconfigure(2, weight= 2)
window.columnconfigure(3, weight= 1)

window.rowconfigure(0, weight= 1)
window.rowconfigure(1, weight= 2)
window.rowconfigure(2, weight= 1)




#LIST TYPE OF UNIT
lst_type_unit = ['Lenght', 'Weight', 'Data', 'Time']
combobox_btn= ttk.Combobox(window, values = lst_type_unit, state='readonly', font= font_txt, width= 10)
combobox_btn.set('Type unit')
combobox_btn.grid(column = 0, columnspan=2, row= 0, sticky=E)



def Current_type_unit():
    current_type_unit_values = ''
    #TYPE OF UNIT
    type_of_unit = {'Lenght' : ['Inch', 'Kilometer', 'Meter', 'Centimeter', 'Feet'], 
                    'Weight' : ['Kilogram', 'Gram', 'Pound'], 
                    'Data' : ['Megawatt', 'Gigawatt', 'Kilowatt', 'Watt'], 
                    'Time' : ['Millisecond', 'Second', 'Minute', 'Hour', 'Day'] }


    combobox_btn_value = combobox_btn.get()
    print(combobox_btn_value)

    if combobox_btn_value not in lst_type_unit: 
        #default value 
        current_type_unit_values = type_of_unit['Weight']
    else: 
        current_type_unit_values = type_of_unit[f'{combobox_btn_value}']


    btn_combobox_value_to_convert['values'] = current_type_unit_values
    btn_combobox_value_to_convert.set(combobox_btn_value)

    btn_combobox_value_converted['values'] = current_type_unit_values
    btn_combobox_value_converted.set(combobox_btn_value)


btn_choose_type_unit = Button(window, text= 'Enter', font=font_txt_btn, bg=dark_green, fg='white', bd=3, relief='solid', activebackground=dark_green, activeforeground='white', command = Current_type_unit)
btn_choose_type_unit.grid(column=2,  row=0)


#BOUTON OFF
img_btn_off  = Image.open("icon_off.png")
img_btn_off_resized = img_btn_off.resize((50,50))
final_img_btn_off = ImageTk.PhotoImage(img_btn_off_resized)

btn_off = Button(window, image= final_img_btn_off, bg=red, borderwidth=3, relief='solid',  activebackground=red, command=window.destroy)
btn_off.grid(column=3, row=0)



#Global Values 
global unit_to_convert, unit_converted
unit_to_convert = 'M'
unit_converted = 'CM' 



#MAIN PAGE
main_page = Frame(window, bg= light_green)
main_page.grid(column = 1, columnspan=2, row= 1, sticky=NSEW)


main_page.columnconfigure(0, weight= 1)
main_page.columnconfigure((1,4), weight= 1)
main_page.columnconfigure(5, weight= 1)

main_page.rowconfigure((0,8), weight= 1)


lbl_type_to_convert = Label(main_page, text='VALUE TO CONVERT', font= font_txt, fg ='white', bg=light_green)
lbl_type_to_convert.grid(columnspan=6, row=1)


btn_combobox_value_to_convert = ttk.Combobox(main_page, font=font_txt_btn)
btn_combobox_value_to_convert.grid(column=0, row=2, pady= 15 )

entry_value_to_change = Entry(main_page,font = font_txt)
entry_value_to_change.grid(column=1, row = 2)

lbl_unit_to_convert = Label(main_page, text=unit_to_convert, font= font_txt, bg = light_green, fg='white')
lbl_unit_to_convert.grid(column=2, row= 2, sticky=EW)

btn_all_clear = Button(main_page, text='AC', font=font_txt_btn, bg = light_green, fg='white', borderwidth=2, relief='solid', activebackground=light_green, activeforeground='white')
btn_all_clear.grid(column=4, row = 2)




lbl_to = Label (main_page, text='TO', font= font_title, bg=light_green)
lbl_to.grid(columnspan=6, row=3, pady= 15 )




btn_combobox_value_converted = ttk.Combobox(main_page, font=font_txt_btn)
btn_combobox_value_converted.grid(column=0, row=5, pady= 15)

value_converted = Label (main_page, text="VALUE CONVERTED", font=font_txt , fg ='white',bg=light_green)
value_converted.grid(columnspan=6,  row = 4 )

entry_value_converted = Entry(main_page, font= font_txt)
entry_value_converted.grid(column=1, row= 5) 

lbl_unit_converted = Label(main_page, text=unit_converted, font= font_txt, bg = light_green, fg='white')
lbl_unit_converted.grid(column=2, row= 5, sticky=EW)




btn_enter = Button(main_page, text="CONVERT", font= font_txt, bg=red, fg='white',borderwidth=2, relief='solid', activebackground=red, activeforeground='white')
btn_enter.grid(columnspan= 6, row = 7 )




window.mainloop()