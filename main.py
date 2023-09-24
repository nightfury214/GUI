from ui import Ui, UiElement
import pandas as pd ### not in requirements file - need to add this
import matplotlib.pyplot as plt
import numpy as np

LGPS_list=['LPelTilt','LHipFlex','LKneeFlex','LAnkDors',
           'LPelObl','LHipAbd','LPelRot','LHipRot','LFootProg']
RGPS_list=['RPelTilt','RHipFlex','RKneeFlex','RAnkDors',
           'RPelObl','RHipAbd','RPelRot','RHipRot','RFootProg']

GPS_list=['LPelTilt','LHipFlex','LKneeFlex','LAnkDors',
           'LPelObl','LHipAbd','LPelRot','LHipRot','LFootProg',
           'RHipFlex','RKneeFlex','RAnkDors',
           'RHipAbd','RHipRot','RFootProg']


class State:
    patient = []
    control = [] 
    map_GPS = []
    ui=[]
        
def GPS(data):
    sq_sum=0
    for i in range(len(data)):
        sq_sum=sq_sum+ np.power((data[i]),2)
    return np.power(sq_sum/len(data),0.5)
    

def load_patient_file(path):
    # code to load data goes here
    pass

    
def load_control_file(path):
    # code to load data goes here
    pass

    
def calc_GPS():

    data=[]
    col=[]
    for angle in State.control.columns:
        for side in ['L','R']:
            sq_sum=0
            for i in range(len(State.patient[side+angle])):
                sq_sum=sq_sum+ np.power((State.patient[side+angle][i]- State.control[angle][i]),2)
            print(sq_sum)
            data.append(np.power(sq_sum/len(State.patient[side+angle]),0.5))
            col.append(side+angle)
    State.map_GPS=pd.DataFrame([data],columns=col)
    print(State.map_GPS)
    
    total=0
    for angle in LGPS_list:
        total=total + np.power(State.map_GPS[angle],2)
    data.append(np.power(total/len(LGPS_list),0.5)[0])
    col.append('LGPS')
    
    total=0
    for angle in RGPS_list:
        total=total + np.power(State.map_GPS[angle],2)
    data.append(np.power(total/len(RGPS_list),0.5)[0])
    col.append('RGPS')
    
    total=0
    for angle in GPS_list:
        total=total + np.power(State.map_GPS[angle],2)
    data.append(np.power(total/len(GPS_list),0.5)[0])
    col.append('GPS')
    
    State.map_GPS=pd.DataFrame([data],columns=col)

    State.ui.set_element(UiElement.OUT_GPS,"{:.2f}".format(State.map_GPS['GPS'][0]))
    State.ui.set_element(UiElement.OUT_LGPS,"{:.2f}".format(State.map_GPS['LGPS'][0]))
    State.ui.set_element(UiElement.OUT_RGPS,"{:.2f}".format(State.map_GPS['RGPS'][0]))

    
def show_graph(path):
    # path is the name of the angle from the drop down list
    fig,ax = plt.subplots()
    # your code to plot 3 line (patient left in red, patient right in green, control in blue)

    State.ui.plot(fig) # this will send the plot to the canvas
    
def radio_choice(choice):
    if choice == 1:
        print("you selected graph")
    if choice == 2:
        print("you selected GPS")
        left=[]
        right=[]
        angles=[]
        for angle in State.control.columns:
            left.append(State.map_GPS['L'+angle][0])
            right.append(State.map_GPS['R'+angle][0])
            angles.append(angle)
        
        x=np.arange(9)

        GPS = {
            'Left': left,
            'Right': right,
        }
        
        width = 0.25  # the width of the bars
        multiplier = 0
        
        fig, ax = plt.subplots(layout='constrained')
        
        for attribute, measurement in GPS.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
#            ax.bar_label(rects, padding=3)
            multiplier += 1
        
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('GPS')
        ax.set_title('GPS map')
        ax.set_xticks(x + width, angles)
        ax.legend(loc='upper left', ncols=2)
        ax.set_ylim(0, 20)
        
        
        State.ui.plot(fig)

if __name__ == '__main__':
    ui = Ui()
    State.ui=ui
    ui.add_select_callback(UiElement.SELECT_PATIENT, load_patient_file)
    ui.add_select_callback(UiElement.SELECT_CONTROL, load_control_file)
    ui.add_button_callback(UiElement.BUTTON_CALC, calc_GPS)
    
    ui.add_select_callback(UiElement.SELECT_GRAPH, show_graph)
    
    ui.add_radio_callback(UiElement.RADIO_PLOT, radio_choice)
    
    
    ui.mainloop()
