From makefile exercise on linux page
1. Target:      app.o
2. Dependancy:  app.c
3. Command:     gcc
-c only assembles and combines. it does not link

output from running helloWorld.c on the bone:
Hello, World! Main is executing at 0x1040c
This address (0xbece4b84) is in our stack frame
This address (0x21030) is in our bss section
This address (0x21028) is in our data section

When I run it on the host however, it does not run and gives me the following message:
dasrs@dasrs-VirtualBox:~$ ./a.out 
bash: ./a.out: cannot execute binary file: Exec format error

Cross compile successful.

A makefile has been created as per the instructions on the makefile page. 
Included in the folder "make". A copy of the makefile is also in the main hw05 folder.

I installed the kernal and compiled it successfully

Is this proof of the updated kernal?
debian@beaglebone:/var/lib/cloud9/ECE434/hw05$ head -3 /boot/uEnv.txt
#Docs: http://elinux.org/Beagleboard:U-boot_partitioning_layout_2.0

uname_r=5.4.0-rc2-bone1

-------------------------------------------------------------
revisions
-------------------------------------------------------------

went back to kernal 4.14:
    debian@beaglebone:/var/lib/cloud9/ECE434$ uname -a
    Linux beaglebone 4.14.108-ti-r115 #1 SMP PREEMPT Mon Aug 26 01:42:24 UTC 2019 armv7l GNU/Linux

The led toggle works now!
Here is a snippet from dmesg:
    [  +0.210604] GPIO_TEST: Interrupt! (button state is 0)
    [  +0.143341] GPIO_TEST: Interrupt! (button state is 1)
    [  +0.163158] GPIO_TEST: Interrupt! (button state is 0)
    [  +0.130146] GPIO_TEST: Interrupt! (button state is 1)
    [  +1.295746] GPIO_TEST: Interrupt! (button state is 0)
    [  +0.105358] GPIO_TEST: Interrupt! (button state is 1)
    [  +6.239852] GPIO_TEST: The button state is currently: 1
    [  +0.000019] GPIO_TEST: The button was pressed 46 times
    [  +0.015016] GPIO_TEST: Goodbye from the LKM!


The hellp folder has been copied from exploringBB folder into the hw05 folder.
The hello.c file make works perfectly Here is a snippet of the output from 
inserting and removing hello.ko. I added my name to the name parameter:
    [Oct14 19:52] EBB: Hello Rahul from the BBB LKM!
    [ +22.209633] EBB: Goodbye Rahul from the BBB LKM!

## Prof. Yoder's comments

If you cross compiled helloWorld.c it shouldn't run on your host.  Copy it to
your bone and try it.
Your kernel proof is good.  Better proof is the output of uname -a

Looks like the kernel modules aren't done yet.

Grade:  5/10