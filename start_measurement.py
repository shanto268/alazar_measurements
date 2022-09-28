from StartMeasurement import *
import StartUserGUI

def getMeasurementSettings():
    session = StartUserGUI()
    settings = session.get_settings()
    return settings


if __name__ == "__main__":
    meas_settings = getMeasurementSettings()
    StartMeasurement(meas_settings)
