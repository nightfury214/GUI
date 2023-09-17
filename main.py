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
        
    

def load_patient_file(path):
    # code to load data goes here
    State.patient=pd.read_excel(path)
    print(State.patient['LKneeFlex'])
    # end of your code
    print(path)
    
def load_control_file(path):
    # code to load data goes here
    State.control=pd.read_excel(path)
    print(State.control['KneeFlex'])
    # end of your code
    print(path)
    
def calc_GPS():
    # code to load data goes here
    # State.control=pd.read_excel(path)
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
#    print(State.map_GPS)
#    print(State.map_GPS['GPS'])
#    print(str(State.map_GPS['GPS']))
#    print("{:.2f}".format(State.map_GPS['GPS'][0]))
#   
#    GPS = State.patient['LKneeFlex'] - State.control['KneeFlex']
#    State.mapGPS = [5,9,3,5]
    State.ui.set_element(UiElement.OUT_GPS,"{:.2f}".format(State.map_GPS['GPS'][0]))
    State.ui.set_element(UiElement.OUT_LGPS,"{:.2f}".format(State.map_GPS['LGPS'][0]))
    State.ui.set_element(UiElement.OUT_RGPS,"{:.2f}".format(State.map_GPS['RGPS'][0]))
#    # end of your code
    # print(path)
    
def show_graph(path):
    
    fig,ax = plt.subplots()
    # need to choose which graph to plot
    ax.plot(State.control[path],'b')
    ax.plot(State.patient['L'+path],'r')
    ax.plot(State.patient['R'+path],'g')
    print(path)

    State.ui.plot(fig)
    
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
