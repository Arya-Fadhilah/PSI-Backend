import requests

# Configuration settings
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8000
TOKEN_URL = f'http://{SERVER_IP}:{SERVER_PORT}/token/'
PATIENT_INFO_URL = f'http://{SERVER_IP}:{SERVER_PORT}/pasien/dataMCU/get_ID/'
UPDATE_URL = f'http://{SERVER_IP}:{SERVER_PORT}/new_sensor_data/'

# Login credentials
login_data = {
    'username': 'arya',
    'password': 'arya123456'
}

# Example sensor data template
sensor_data_template = {
    'temperature': 37.5,
    'alcohol': 0.1,
    'urine': 0,
    'berat': 60.5,
    'tinggi': 170
}

def login():
    """Attempts to log in and retrieve an authentication token."""
    print("Attempting to login...")
    response = requests.post(TOKEN_URL, data=login_data)
    if response.status_code == 200:
        token = response.json().get('access')
        print(f"Token: {token}")
        return token
    else:
        print(f"Login failed! Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        return None

def get_patient_id(token):
    """Fetches the patient information from the server."""
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(PATIENT_INFO_URL, headers=headers)
        if response.status_code == 200:
            patient_info = response.json()
            return patient_info.get('patient_id')
        else:
            print(f"Failed to fetch patient info. Status Code: {response.status_code}")
            print("Response Text:", response.text)
            return None
    else:
        print("No valid token available to fetch patient data.")
        return None

def send_sensor_data(token, patient_id):
    """Sends sensor data to the server."""
    if token and patient_id:
        # Update the sensor data with the patient_id
        sensor_data = sensor_data_template.copy()  # Make a copy of the template
        sensor_data['patient_id'] = patient_id

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(UPDATE_URL, data=sensor_data, headers=headers)
        if response.status_code == 200:
            print("Sensor data successfully sent to the server!")
        else:
            print(f"Failed to send data. Status Code: {response.status_code}")
            print("Response Text:", response.text)
    else:
        print("Unable to send sensor data due to missing token or patient ID.")

def main():
    """Main function to log in, get patient ID, and send sensor data."""
    token = login()
    if token:
        patient_id = get_patient_id(token)
        if patient_id:
            send_sensor_data(token, patient_id)

if __name__ == "__main__":
    main()
