import tensorflow as tf
import pandas as pd
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Lambda
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

data = pd.read_csv('vehicle_count.csv')
print(data)
X = data['Image Name']
Y = data['Vehicle Count']

def FuzzyController():
    vehicle_count = ctrl.Antecedent(np.arange(0, 51, 1), 'vehicle_count')
    green_light_time = ctrl.Consequent(np.arange(5, 61, 1), 'green_light_time')

    vehicle_count['Low'] = fuzz.trimf(vehicle_count.universe, [0, 0, 20])
    vehicle_count['Medium'] = fuzz.trimf(vehicle_count.universe, [10, 25, 40])
    vehicle_count['High'] = fuzz.trimf(vehicle_count.universe, [30, 50, 50])

    green_light_time['Short'] = fuzz.trimf(green_light_time.universe, [5, 10, 20])
    green_light_time['Medium'] = fuzz.trimf(green_light_time.universe, [15, 30, 45])
    green_light_time['Long'] = fuzz.trimf(green_light_time.universe, [40, 55, 60])

    rule1 = ctrl.Rule(vehicle_count['Low'], green_light_time['Short'])
    rule2 = ctrl.Rule(vehicle_count['Medium'], green_light_time['Medium'])
    rule3 = ctrl.Rule(vehicle_count['High'], green_light_time['Long'])

    traffic_light_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    traffic_light_sim = ctrl.ControlSystemSimulation(traffic_light_ctrl)

    green_times = []
    for _, row in data.iterrows():
        traffic_light_sim.input['vehicle_count'] = row['Vehicle Count']
        traffic_light_sim.compute()
        green_times.append(traffic_light_sim.output['green_light_time'])

    data['Green Light Time (seconds)'] = green_times
    output_file_path = 'output_with_green_times.csv'
    data.to_csv(output_file_path, index=False)
    print(f"Green light timings computed and saved to {output_file_path}.")