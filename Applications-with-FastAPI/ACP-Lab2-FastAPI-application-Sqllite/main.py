from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

# Define the NetworkActivity BaseModel
class NetworkActivity(BaseModel):
    activityID: Optional[int]  # Optional for POST requests
    tBodyAcc_mean_X: float
    tBodyAcc_mean_Y: float
    tBodyAcc_mean_Z: float
    tBodyAcc_std_X: float
    tBodyAcc_std_Y: float
    tBodyAcc_std_Z: float
    Access_Point_ID_1: float
    Network_Latency_1: float
    Data_Transfer_Rate_1: float
    Network_Jitter_1: float
    Packet_Loss_Rate_1: float
    Device_Connectivity_Duration_1: float

# Initialize FastAPI
app = FastAPI()

# Function to get database connection
def get_db_connection():
    conn = sqlite3.connect('network_activity_data.db')
    conn.row_factory = sqlite3.Row  # Allows us to return rows as dictionaries
    return conn

# Insert the first 10 rows during initialization
def initialize_database():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS network_activity_data (
        activityID INTEGER PRIMARY KEY,
        tBodyAcc_mean_X REAL,
        tBodyAcc_mean_Y REAL,
        tBodyAcc_mean_Z REAL,
        tBodyAcc_std_X REAL,
        tBodyAcc_std_Y REAL,
        tBodyAcc_std_Z REAL,
        Access_Point_ID_1 REAL,
        Network_Latency_1 REAL,
        Data_Transfer_Rate_1 REAL,
        Network_Jitter_1 REAL,
        Packet_Loss_Rate_1 REAL,
        Device_Connectivity_Duration_1 REAL
    )
    ''')

    # Data to insert
    data_to_insert = [
        (1, 0.29, -0.02, -0.13, -1.00, -0.98, -0.91, 10, 29.82, 23.37, 8.53, 0.71, 431.80),
        (2, 0.28, -0.02, -0.12, -1.00, -0.98, -0.96, 19, 71.16, 7.13, 3.02, 0.48, 326.75),
        (3, 0.28, -0.02, -0.11, -1.00, -0.97, -0.98, 2, 89.65, 20.42, 4.16, 0.53, 299.58),
        (4, 0.28, -0.03, -0.12, -1.00, -0.98, -0.99, 14, 57.45, 49.92, 1.90, 0.19, 298.06),
        (5, 0.28, -0.02, -0.12, -1.00, -0.98, -0.99, 9, 66.96, 9.06, 1.84, 0.11, 462.33),
        (6, 0.28, -0.01, -0.11, -1.00, -0.99, -1.00, 6, 14.63, 39.32, 9.04, 0.94, 450.95),
        (7, 0.28, -0.02, -0.11, -1.00, -0.97, -0.98, 8, 78.07, 49.19, 1.69, 0.57, 492.55),
        (8, 0.28, -0.03, -0.13, -1.00, -0.97, -0.98, 11, 25.69, 24.07, 6.59, 0.30, 489.06),
        (9, 0.28, -0.02, -0.12, -1.00, -0.96, -0.98, 13, 46.20, 19.59, 6.68, 0.92, 258.80),
        (10, 0.28, -0.01, -0.11, -0.99, -0.97, -0.99, 14, 37.29, 29.47, 7.26, 0.59, 113.63),
    ]

    # Insert data into the database if not already present
    cursor.executemany('''
    INSERT OR IGNORE INTO network_activity_data 
    (activityID, tBodyAcc_mean_X, tBodyAcc_mean_Y, tBodyAcc_mean_Z, tBodyAcc_std_X, tBodyAcc_std_Y, tBodyAcc_std_Z,
     Access_Point_ID_1, Network_Latency_1, Data_Transfer_Rate_1, Network_Jitter_1, Packet_Loss_Rate_1, Device_Connectivity_Duration_1)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data_to_insert)

    conn.commit()
    conn.close()

# Call database initialization function
initialize_database()

# Get all records
@app.get("/activities/", response_model=List[NetworkActivity])
def read_activities():
    conn = get_db_connection()
    activities = conn.execute("SELECT * FROM network_activity_data").fetchall()
    conn.close()
    return [dict(activity) for activity in activities]

# Get a specific record by ID
@app.get("/activities/{activityID}", response_model=NetworkActivity)
def read_activity(activityID: int):
    conn = get_db_connection()
    activity = conn.execute("SELECT * FROM network_activity_data WHERE activityID = ?", (activityID,)).fetchone()
    conn.close()
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return dict(activity)

# Add a new record
@app.post("/activities/", response_model=NetworkActivity)
def create_activity(activity: NetworkActivity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO network_activity_data (tBodyAcc_mean_X, tBodyAcc_mean_Y, tBodyAcc_mean_Z, tBodyAcc_std_X, tBodyAcc_std_Y, tBodyAcc_std_Z, Access_Point_ID_1, Network_Latency_1, Data_Transfer_Rate_1, Network_Jitter_1, Packet_Loss_Rate_1, Device_Connectivity_Duration_1) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (activity.tBodyAcc_mean_X, activity.tBodyAcc_mean_Y, activity.tBodyAcc_mean_Z, activity.tBodyAcc_std_X, activity.tBodyAcc_std_Y, activity.tBodyAcc_std_Z, activity.Access_Point_ID_1, activity.Network_Latency_1, activity.Data_Transfer_Rate_1, activity.Network_Jitter_1, activity.Packet_Loss_Rate_1, activity.Device_Connectivity_Duration_1)
    )
    conn.commit()
    conn.close()
    return activity

# Update an existing record
@app.put("/activities/{activityID}", response_model=NetworkActivity)
def update_activity(activityID: int, activity: NetworkActivity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE network_activity_data SET tBodyAcc_mean_X = ?, tBodyAcc_mean_Y = ?, tBodyAcc_mean_Z = ?, tBodyAcc_std_X = ?, tBodyAcc_std_Y = ?, tBodyAcc_std_Z = ?, Access_Point_ID_1 = ?, Network_Latency_1 = ?, Data_Transfer_Rate_1 = ?, Network_Jitter_1 = ?, Packet_Loss_Rate_1 = ?, Device_Connectivity_Duration_1 = ? WHERE activityID = ?",
        (activity.tBodyAcc_mean_X, activity.tBodyAcc_mean_Y, activity.tBodyAcc_mean_Z, activity.tBodyAcc_std_X, activity.tBodyAcc_std_Y, activity.tBodyAcc_std_Z, activity.Access_Point_ID_1, activity.Network_Latency_1, activity.Data_Transfer_Rate_1, activity.Network_Jitter_1, activity.Packet_Loss_Rate_1, activity.Device_Connectivity_Duration_1, activityID)
    )
    conn.commit()
    conn.close()
    return activity

# Delete a record
@app.delete("/activities/{activityID}")
def delete_activity(activityID: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM network_activity_data WHERE activityID = ?", (activityID,))
    conn.commit()
    conn.close()
    return {"detail": "Activity deleted successfully"}
