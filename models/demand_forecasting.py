import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split

def create_lstm_model(input_shape):
    """
    Builds and compiles an LSTM model.
    """
    model = Sequential([
        LSTM(50, activation='relu', input_shape=input_shape, return_sequences=True),
        LSTM(50, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def train_model(data, target):
    """
    Trains the LSTM model with the given data.
    """
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
    input_shape = (X_train.shape[1], X_train.shape[2])
    model = create_lstm_model(input_shape)
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
    return model

if __name__ == "__main__":
    # Example usage with dummy data
    X = np.random.rand(100, 10, 1)
    y = np.random.rand(100)
    model = train_model(X, y)
