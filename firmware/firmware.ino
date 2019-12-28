/* INFO
  Temperature sensor:
    ADC = 10 bits.
    S   = 10mV/C
    Vcc = 5V 

*/

#include <string.h>

// Constants
#define s_temp      0.01            // Temperature sensor sensibility 10mV/C
#define vcc_temp    5               // 5 Vcc
#define scale       1023            // Full scale
#define INT_SIZE    (size_t) 2      // Int size : 2 Bytes
#define FLOAT_SIZE  (size_t) 4      // Float size : 4 Bytes

// Types
union FloatStruct{
   float data;
   byte  b[4];
};

// Functions
int serialfwrite(FloatStruct data);
int serialswrite(char *data, int size);

// Variables
  // Temperature
float rdata=0;
float vdata=0;
float tdata=0;
  // Humidity
float hdata=0;
  // Light
float ldata=0;

// Setup
void setup(){
  
  Serial.begin(115200);

}

// Loop
void loop(){

  // Temperature
  rdata = analogRead(A0);            // Raw data
  vdata = rdata * vcc_temp / scale;  // Voltage data
  tdata = vdata / s_temp;       // Temperature data
  
  // Humidity
  hdata = 0.0;

  // Light data
  ldata = 0.0;

  Serial.print(tdata, 1);
  Serial.print(',');
  Serial.print(hdata, 1);
  Serial.print(',');
  Serial.print(ldata, 1);
  Serial.println(',');

  delay(1000);

}

int serialfwrite(FloatStruct data){
  int i = 0;
  while(i < 4){
    Serial.write(data.b[i]);
    i++;
  }
  return 0;
}

int serialswrite(char *data, int size){
  int i = 0;
  while(i < size){
    Serial.write(data[i]);
    i++;
  }
  Serial.write('\0');
  return 0;
}
