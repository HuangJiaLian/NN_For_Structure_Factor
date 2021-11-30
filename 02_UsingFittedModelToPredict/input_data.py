"""
@author: Jack Huang
"""
import numpy as np 
import os

class DataWrapper:
    def __init__(self):
        # Path stored structured data 
        # Change if needed 
        self.path = './structured_data/'
        if os.path.exists(self.path) != True:
            print("Ooops, structured data not exist. Existing ...")
            exit()
        self.file_list = os.listdir(self.path)
        self.all_data = np.load(self.path+self.file_list[-1])
        self.labelBits = 1
        self.labelBFlag = -1*self.labelBits

    # Return the TrainInputs, TrainLabels
    # which will be used in Nerual Network 
    def read_data_sets(self, data_combined):
        np.random.shuffle(data_combined)
        TrainInputs = data_combined[:, :self.labelBFlag]
        TrainLabels = data_combined[:, self.labelBFlag:]
        return TrainInputs, TrainLabels


    
    # def data_filter(self):
    #     Data = [0]*5
    #     for i in range(0,len(self.all_data)):
    #         if self.all_data[i][1] <= 0.1 and self.all_data[i][0] <= 0.1:
    #             Data[0] = np.append(Data[0], self.all_data[i])
    #         elif self.all_data[i][1] <= 1 and self.all_data[i][0] <= 1:
    #             Data[1] = np.append(Data[1], self.all_data[i])
    #         elif self.all_data[i][1] <= 10 and self.all_data[i][0] <= 10:
    #             Data[2] = np.append(Data[2], self.all_data[i])
    #         elif self.all_data[i][1] <= 100 and self.all_data[i][0] <= 100:
    #             Data[3] = np.append(Data[3], self.all_data[i])
    #         else:
    #             Data[4] = np.append(Data[4], self.all_data[i])
    #     for j in range(len(Data)):
    #         # Remove the first 0
    #         Data[j] = Data[j][1:]
    #         Data[j] = Data[j][:,np.newaxis]
    #         Data[j] = Data[j].reshape(-1,3)
    #     return Data


