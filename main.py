from ui import Ui, UiElement
import pandas as pd ### not in requirements file - need to add this
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

if __name__ == '__main__':
    ui = Ui()
    ui.add_select_callback(UiElement.SELECT_PATIENT, load_patient_file)
    ui.add_select_callback(UiElement.SELECT_CONTROL, load_control_file)
    ui.mainloop()
