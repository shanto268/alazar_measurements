import Labber

def readInstrumentSettings(measurement_settings):
    """
    Reads the JSON file and only returns the instruments used and their activation settings

    Parameters
    ----------
    measurement_settings : dict
        JSON object read from disk/memory as defined by user

    Raises
    ------
    NotImplementedError:
        [TODO:description]
    """
    instrs = measurement_settings["instruments"]
    instr_settings = []
    for instr in instrs:
        instr_settings.append(instr["name"],instr["labber_info"],instr["var_name"])
    return instr_settings

def activateInstrument(instr_settings, labber_client):
    """
    TO DO:
        - ensure instr_settings[1] is parsed in the required way
    """
    var_name = instr_settings[2]
    instr_obj = labber_client.connectToInstrument(instr_settings[0],dict(instr_settings[1]))
    return dict("var_name"=var_name, "instr_obj"=instr_obj)


def selectInstrument(var_name, instr_objs):
    raise NotImplementedError()

def performAction(instr_obj, action, value):
    raise NotImplementedError()

