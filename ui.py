from tkinter import *
from tkinter.filedialog import askopenfilename


class Ui:
    def __init__(self):
        win = Tk()
        win.title("Maths and Stuff")

        root = Frame(win, padx=10, pady=10)
        root.pack()

        file_sel_frame = Frame(root, padx=10, pady=10)
        file_sel_frame.grid(row=0, column=0, sticky="W")

        Button(file_sel_frame, text="Select patient", command=askopenfilename).grid(row=0, sticky="W")
        Button(file_sel_frame, text="Select control", command=askopenfilename).grid(row=1, sticky="W")

        gps_calc_frame = Frame(root, padx=10, pady=10)
        gps_calc_frame.grid(row=0, column=1, sticky="W")

        Button(gps_calc_frame, text="Calculate GPS", width=8, wraplength=60).grid(column=0, rowspan=3, sticky="W")
        Label(gps_calc_frame, text="LGPS", padx=10, ).grid(column=1, row=0)
        Label(gps_calc_frame, text="RGPS", padx=10, ).grid(column=1, row=1)
        Label(gps_calc_frame, text="GPS", padx=10, ).grid(column=1, row=2)

        lgps_input = Text(gps_calc_frame, height=1, width=4)
        lgps_input.insert(END, "10")
        lgps_input.grid(column=2, row=0)

        rgps_input = Text(gps_calc_frame, height=1, width=4)
        rgps_input.insert(END, "10")
        rgps_input.grid(column=2, row=1)

        gps_input = Text(gps_calc_frame, height=1, width=4)
        gps_input.insert(END, "10")
        gps_input.grid(column=2, row=2)

        graph_control_frame = Frame(root, padx=10, pady=10)
        graph_control_frame.grid(row=1, column=0, sticky="W")

        graph_dropdown = OptionMenu(graph_control_frame, StringVar(graph_control_frame, "Select"), "option", "other option", "other other option")
        graph_dropdown.grid(column=0, row=0, sticky="W")

        graph_radio_frame = Frame(root)
        graph_radio_frame.grid(row=1, column=1, sticky="W")
        graph_radio = IntVar()

        Radiobutton(graph_radio_frame, text="Show graphs", value=1, variable=graph_radio, anchor="e").pack(anchor="w")
        Radiobutton(graph_radio_frame, text="Show GPS", value=2, variable=graph_radio, anchor="e").pack(anchor="w")

        graph_frame = Frame(root, width=400, height=300, padx=10, pady=10, background="black")
        graph_frame.grid(row=2, columnspan=2)

        root.mainloop()
