from InstrumentsHandler import *
import Labber

class StartMeasurement:

    """Docstring for StartMeasurement. """

    def __init__(self, measurement_settings):
        self.measurement_settings = measurement_settings
        self.instruments = self.getInstruments(self.measurement_settings)


    def getInstruments(self, measurement_settings):
        instrs = readInstrumentSettings(measurement_settings)
        return instrs

    def turnOnInstruments(self, instruments, labber_client):
        instr_objs = []
        for instrument in instruments:
            instr_objs.append(activateInstrument(instrument, labber_client))
        return instr_objs

    def setInitialParameters(self, measurement_settings, instr_objs):
        initial_actions = measurement_settings["initial_actions"]
        for action in initial_actions:
            instr_obj = selectInstrument(action["var_name", instr_objs])
            performAction(instr_obj, action["action"], action["value"])

    def setMeasurementParamters(self, measurement_settings):
        raise NotImplementedError()


    def run(self):
        labber_client = Labber.connectToServer(timeout=None)
        live_intruments = self.turnOnInstruments(self.instruments, labber_client)

        setInitialParameters(self.measurement_settings, live_intruments)



