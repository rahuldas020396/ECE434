From makefile exercise on linux page
1. Target:      app.o
2. Dependancy:  app.c
3. Command:     gcc
-c only assembles and combines. it does not link

output from running helloWorld.c on the bone:
debian@beaglebone:~$ ./a.out 
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

When I follow the steps on Maloy's website and compile my LED.c (which is the toggle function),
I get an error pointing me to the linux/ header files saything that they do not exist.