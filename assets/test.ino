/*
  nRF24L01+ Joystick Receiver for Robot Car
  nrf24l01-joy-rcv-car.ino
  nRF24L01+ Receiver and L298N driver for Robot Car
  Use with Joystick Transmitter for Robot Car
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

// Motor A Connections
int enA = 9;
int in1 = 14;
int in2 = 4;

// Motor B Connections
int enB = 5;
int in3 = 7;
int in4 = 6;

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
  
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
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

    {

      //Serial Print the values of joystick
      //Serial.print("got request from : 0x");
      //Serial.print(from, HEX);
      //Serial.print(": MotorA = ");
      //Serial.print(buf[0]);
      //Serial.print(" MotorB = ");
      //Serial.print(buf[1]);
      //Serial.print(" Dir = ");
      //Serial.println(buf[2]);
      
      // Set Motor Direction
      if (buf[2] == 1)
      {
    // Motors are backwards
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
    }else{
    // Motors are forwards
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
     }
 
      
      // Drive Motors
      analogWrite(enA, buf[1]);
      analogWrite(enB, buf[0]);
     
      // Send a reply back to the originator client, check for error
      if (!RadioManager.sendtoWait(ReturnMessage, sizeof(ReturnMessage), from))
        Serial.println("sendtoWait failed");
    }
  }              
}
