# Helium
### Data acquisition system for sensors station

Helium uses Raspberry Pi for SSH communication and arduino as data acquisition system with sensors.

- Firmware loaded in arduino can be upgraded using arduino-cli.
- Raspberry can run python codes to read and store data through serial with arduino.

### Setting up arduino-cli
https://github.com/arduino/arduino-cli

### Install
Install arduino-cli
 > curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh

Make sure arduino-cli executable is in a PATH variable folder 
 > echo $PATH

Create config file folder
 > mkdir ~/.arduino15

Create config file
 > arduino-cli config init
 > Correct output: "Config file written: /home/user/.arduino15/arduino-cli.yaml"

### Connect board
Create packages folder
 > mkdir ~/.arduino15/packages

Install and update platforms and libraries
 > arduino-cli core update-index
 > Correct last line output: Updating index: package_index.json downloaded

List connected boards
 > arduino-cli board list
 > In case arduino UNO: (FQBN: arduino:avr:uno , Core: arduino:avr)

Install correct core for arduino UNO
 > arduino-cli core install arduino:avr
 > Check installation with: > arduino-cli core list

### Compile and upload an sketch
Create sketch
 > arduino-cli sketch new MyFirstSketch

Compile sketch
 > arduino-cli compile --fqbn arduino:avr:uno MyFirstSketch

Upload sketch
 > arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno MyFirstSketch