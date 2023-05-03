# Queue Analyzer

This standalone app is the Graphical user interface version of the python program written to generate a distribution for arrival and analyse the results from the Dosimis software. The app is written in python version 3.10 and GUI is enabled with GTK 3.5 with Glide software.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Installation

The App can be run in three ways.    
  
1. Download .exe windows executable file.  
[Download Link](https://drive.google.com/file/d/112hH66TlmQ7xwqi7EwZhJhfROGHBMQms/view?usp=share_link)  
https://drive.google.com/file/d/112hH66TlmQ7xwqi7EwZhJhfROGHBMQms/view?usp=share_link


  
2. Build the .exe file using pyinstaller.  
run 'pyinstaller -w --onefile Queue Analyzer.py' in terminal.
find executable in dist folder. 
  
3. Run python script file.  
make sure the following dependencies are met before running Queue Analyzer.py file  
• Python 3.10 or newer  
• Gtk version 3.0  
• numpy  
• matplotlib  
• pandas  
• datetime  



## Usage

The App has Two functions, one is to generate arrival distribution for the Dosimis model and second is to analyse the results from the simulation of Dosimis model. 
The top left corner shows the group of widgets to enter details for generating the arrival distribution. The first four text entries are for entering the persons/time slot for four different cases. The next row entries are simulation time and time slot value (time interval) respectively. Hovering mouse pointer shows which text entries for which. The Button next to it enables to save the .txt files at desired location. Once everything in order, clicking generate button will generate the data files for the Dosimis model, simultaneously appearing completion message.
The analyse part uses the rest of the widgets. Use file chooser button to load .tra files and input .txt files (arrival data) for the four cases. These files are in Dosimis model directory. Also note the module number of each module when modelling the model in Dosimis. Enter the module number at which object enter and exits in corresponding text entries. Once the details are loaded click the generate statistics to display the results. 
The results will contain the following items.    
  
    • Statistical data of total time spend and queue length (the time) at entrance for four cases.  
    • Graph plotted between time spend vs number of peoples for four cases.  
    • Second graph plotted between max time spend across each module and corresponding modules for four cases.  
    
Subsequently a local directory is created and filled with data used for the results including the .png files of graphs.

## Contributing

Optimizing the project with size and run speed.

## License

GNU General Public License v3.0

## Author  

Dipson  

---

