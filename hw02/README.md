Buttons and LEDs
1. Wired up buttons and LEDs
2. LED can be controlled by buttons
Measuring GPIO using oscilloscope

Shell Script

Min voltage = -80mV	Max voltage = 3.52V
Period = 272ms
It is 172ms different from 100ms because we gave it a half period time. The extra 72ms comes from the software overhead and extra protocols
When I rum htop it tells me that debian is using 95.5% of my CPU (I have a very old computer)

argument	Actual period (ms)		Processor Usage (%)
0.1         269                     79.4
0.01        88.0                    52.2
0.005       80.0                    48.1
0.001       72.00                   45.1
0.0005      72.00                   44.2

As we get lower, the period becomes less stable. It jumps between 72ms to 76ms
When I launched vi my period became more stable and reduced drastically to 40.3ms

In the file I changed the word bash to sh and got my period down to 29ms

Python script

Min voltage = 320mV     Max voltage = 3.44V
Period = 101.4ms and I entered 100ms as the parameter
The difference is 1.4ms and I think this is because python takes that time to run the scripts. The system overheads along with the time it takes to decode the syntax and compile the script
When I run htop, it gives me a cpu usage of 2%

argument            Actual Period (ms)      Processor Usage (%)
0.1                 101.4                   2.7%
0.01                11.34                   9.9%
0.005               6.34ms                  18.1
0.0001              0.481                   92.6
No argument         0.155                   100


Fastest period = 155us (micro seconds)
As we reduce the period. the plot becomes 'shaky' and becomes very unstable
When I ran vi on terminal, it increased my period to 444us and increased the stability.

C script

argument            Actual Period (ms)      Processor Usage (%)
0                   0.290                   93.9
100                 0.600                   75.3
1000                3.000                   27

Fastest period = 280us
As we reduce the period, the plot becomes more jittery and unstable
When I ram vi in my terminal, it made my period momentarily unstable and then it stabilized 

Etch a Sketch

I re-made etch a sketch with curses. I added the gpio buttons as inputs to the etch a sketch. 
My etch a sketch also has a clear command that can be done by pressing all four buttons down at the same time
