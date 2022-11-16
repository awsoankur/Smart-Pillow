For Windows: (During the process, you may encounter several errors dependin gupon the configurations of your system. Please refer to the error messages and fix them accordingly.)
# Install NPM and Node
Download Node LTS from this website : [Download](https://nodejs.org/en/download/)

Check installation by running command
```
npm
```
in the terminal.
### Install yarn
Open a new terminal and run :
```bash
npm install --global yarn
```

### Install concurrently
```bash
npm install --global concurrently
```

### Install dependencies for the project
In the terminal, change the working directory to the project directory i.e. WebApp
Run the following command to install the dependencies.
```bash
yarn
```

### Run the project
Run the following command to run the project to **localhost**
```bash
yarn dev
```


This will run the display api on the browser on going to the link
```
localhost:3000
```

# To run the server

Run the following with the `pip install` command to install modules
```
pip install "module_name"
```
```
http.server
socketserver
pyqrcode
statistics
tensorflow
matplotlib 
tensorflow_io
seaborn
librosa
```
If still any module is missing try the same with that module name
 
### Run the sensors

Run the files `sensor.py` and `sensor_ecg.py` in the pillow folder.

### Run the server

Run the file `server.py` in the server folder.
Note the server ip shown in the output.

### Run the pillow
copy the above noted ip in the `pillow.py` file as the value to the variable url followed by a `//` , sample url `url="http://172.17.76.7:8000//"` 
Run the `pillow` file in the pillow folder.