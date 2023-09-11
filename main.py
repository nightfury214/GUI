from ui import Ui, UiElement
import pandas as pd ### not in requirements file - need to add this
import matplotlib.pyplot as plt




class State:
    patient = []
    control = [] 
    map_GPS = []
    ui=[]
        
    

def load_patient_file(path):
    # code to load data goes here
    State.patient=pd.read_excel(path)
    print(State.patient.LKneeFlex_x)
    # end of your code
    print(path)
    
def load_control_file(path):
    # code to load data goes here
    State.control=pd.read_excel(path)
    print(State.control.LKneeFlex_x)
    # end of your code
    print(path)
    
def calc_GPS():
    # code to load data goes here
    # State.control=pd.read_excel(path)
    GPS = State.patient.LKneeFlex_x - State.control.LKneeFlex_x
    State.mapGPS = [5,9,3,5]
    State.ui.set_element(UiElement.OUT_GPS,str(GPS[0]))
    State.ui.set_element(UiElement.OUT_LGPS,str(GPS[0]))
    State.ui.set_element(UiElement.OUT_RGPS,str(GPS[0]))
    # end of your code
    # print(path)
    
def show_graph(path):
    fig,ax = plt.subplots()

    ax.plot(State.control.LKneeFlex_x)
    ax.plot(State.patient.LKneeFlex_x)

    State.ui.plot(fig)

if __name__ == '__main__':
    ui = Ui()
    State.ui=ui
    ui.add_select_callback(UiElement.SELECT_PATIENT, load_patient_file)
    ui.add_select_callback(UiElement.SELECT_CONTROL, load_control_file)
    ui.add_button_callback(UiElement.BUTTON_CALC, calc_GPS)
    
    ui.add_select_callback(UiElement.SELECT_GRAPH, show_graph)
    ui.mainloop()
