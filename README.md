# New Measurement Code Architecture:

## Requirements:

- Read the labber driver files (.ini) to get information about all instruments
- Take inputs from user for measurement parameters (bounds, init values, type of measurement, person running the experiment)
- Handles all physical instruments safely (safecheck parameters implement, pause and terminate if bad conditions, email for help)
- Logs all the required info
- Keyboard input monitoring to **safely terminate** a job
- Automated functionalities for various optimization (i.e. TWPA tune ups, JPA tune up, auto-JPA-TWPA tune up)

## Use Case and Flow:

1. *User creates a .json file with measurement parameters* or *User inputs all measurement parameters into a GUI* 
  a. The program creates a new prompt asking for confirmation before proceeding
2. The program then starts all the required instruments safely
3. The program then automatically tunes up amplifiers if user wanted it or proceeds with settings that user selected
4. The program shows visual bar for how long the measurement would take
5. The program safely stores log files, plots and any emissions file
6. The program will always have a **safe stop** button to safely terminate the job
7. At the end of measurement, the program will safely turn off the devices and email the person running the experiment

---

# To Do:

- [ ] json file creator
- [ ] GUI
- [ ] Unit Tests
- [ ] Test Run
- [ ] Document
