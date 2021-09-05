#include <wiringPi.h>
#include <signal.h>

#define GREEN 25
#define RED 24

int blink = 1;

void cleanup(int signo) {
    blink = 0;
}

int main(void){
    signal(SIGINT, cleanup);
    signal(SIGTERM, cleanup);
    signal(SIGHUP, cleanup);

    wiringPiSetup();
    pinMode(GREEN, OUTPUT);
    pinMode(RED, OUTPUT);

    while (blink) {
	digitalWrite(GREEN, HIGH);
	delay(500);
	digitalWrite(GREEN,LOW);
	digitalWrite(RED, HIGH);
	delay(500);
	digitalWrite(RED, LOW);
    }

pinMode(GREEN, INPUT);
pinMode(RED, INPUT);
digitalWrite(GREEN, LOW);
digitalWrite(RED, LOW);

    return 0;
}
