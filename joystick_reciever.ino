/*nrf24l01-joy-rcv-demo.ino
  nRF24L01+ Receiver with Joystick Decode
  Use with Joystick Transmitter Demo
  DroneBot Workshop 2018
  https://dronebotworkshop.com
*/
 
// Include RadioHead ReliableDatagram & NRF24 Libraries
#include <RHReliableDatagram.h>
#include <RH_NRF24.h>
 
// Include dependant SPI Library 
#include <SPI.h>
 
// Define addresses for radio channels
#define CLIENT_ADDRESS 1   
#define SERVER_ADDRESS 2
 
// Create an instance of the radio driver
RH_NRF24 RadioDriver;
 
// Sets the radio driver to NRF24 and the server address to 2
RHReliableDatagram RadioManager(RadioDriver, SERVER_ADDRESS);
 
// Define a message to return if values received
uint8_t ReturnMessage[] = "JoyStick Data Received"; 
 
// Define the Message Buffer
uint8_t buf[RH_NRF24_MAX_MESSAGE_LEN];
 
void setup()
{
  // Setup Serial Monitor
  Serial.begin(9600);
  
  // Initialize RadioManager with defaults - 2.402 GHz (channel 2), 2Mbps, 0dBm
  if (!RadioManager.init())
    Serial.println("init failed");
} 
 
void loop()
{
  if (RadioManager.available())
  {
 // Wait for a message addressed to us from the client
    uint8_t len = sizeof(buf);
    uint8_t from;
    if (RadioManager.recvfromAck(buf, &len, &from))
 //Serial Print the values of joystick
    {
      Serial.print("got request from : 0x");
      Serial.print(from, HEX);
      Serial.print(": X = ");
      Serial.print(buf[0]);
      Serial.print(" Y = ");
      Serial.print(buf[1]);
      Serial.print(" Z = ");
      Serial.println(buf[2]);
 
      // Send a reply back to the originator client, check for error
      if (!RadioManager.sendtoWait(ReturnMessage, sizeof(ReturnMessage), from))
        Serial.println("sendtoWait failed");
    }
  }              
}
