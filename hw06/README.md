Where does Julia Cartwright work?
National Instruments

What is PREEMT_RT? Hint: Google it
Linux real-time kernal development

What is mixed criticality?
Two different degrees of time sensitiveness

How can drivers misbehave?


What is delta in Figure 1?
Latency: time between the event and actual real time execution 

What is Cyclictest[2]?


What is plotted in Figure 2?
delta is plotted. This can be found by asking the program to sleep 
and then finding the actual sleep time and subtracting them.
====== (Yoder:  Details are missing)

What is dispatch latency? Scheduling latency?
Time between hardware actually firing and the relevant thread to actually be woken up.

What is mainline?
It is a plot against time of the different events such as interupt. It stacks based on priority.

What is keeping the External event in Figure 3 from starting?
Long running low priority interupts doing things that we don't necessarily care about

Why can the External event in Figure 4 start sooner?
The real time patch forces IRQ threads causing the low priority interupts to be cut out of the execution time.
This reduces dispatch latency

-------------------------------------
Update
-------------------------------------
When I ran the time sudo ./hist.gen > nort.hist for the first time, I got:

Real Time:

With Load:
real    1m44.878s
user    0m1.882s
sys     0m9.142s

With no Load
real    1m45.307s
user    0m0.488s
sys     0m4.256s

Non Real Time

With Load
real    1m45.108s
user    0m2.045s
sys     0m9.396s

With no Load
real    1m44.761s
user    0m1.077s
sys     0m3.247s


## Prof. Yoder's comments
Good start on the questions, though some answers are missing.  (-1)
Looking forward to seeing the plots. (-5)

Grade:  5/10
