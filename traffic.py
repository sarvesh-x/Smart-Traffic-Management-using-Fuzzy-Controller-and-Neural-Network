import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def ANN():
    file_path = 'output_with_green_times.csv'  
    data = pd.read_csv(file_path)

    X = data[['Vehicle Count']].values
    y = data[['Green Light Time (seconds)']].values

    scaler_X = MinMaxScaler()
    scaler_y = MinMaxScaler()
    X_scaled = scaler_X.fit_transform(X)
    y_scaled = scaler_y.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

    model = Sequential([
        Dense(64, activation='relu', input_dim=X_train.shape[1]),
        Dense(32, activation='relu'),
    Dense(1, activation='linear') 
])

    model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    model.fit(X_train, y_train, epochs=100, batch_size=16, validation_split=0.2, verbose=1)

    loss, mae = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss: {loss:.4f}, Test MAE: {mae:.4f}")

    new_vehicle_counts = np.array([[2], [30], [50], [17]])  # Replace with actual values
    new_vehicle_counts_scaled = scaler_X.transform(new_vehicle_counts)
    predicted_times_scaled = model.predict(new_vehicle_counts_scaled)
    predicted_times = scaler_y.inverse_transform(predicted_times_scaled)

    for i, count in enumerate(new_vehicle_counts):
        print(f"Vehicle Count: {count[0]}, Predicted Green Time: {predicted_times[i][0]:.2f} seconds")
