#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

#define PRUN 1_1
//#define PRU0_DRAM 0x00000 // Offset to DRAM
volatile register uint32_t __R30;
volatile register uint32_t __R31;
//volatile unsigned int *pru0_dram = PRU0_DRAM;

void main(void)
{
    uint32_t gpio;

    /* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
    CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

    gpio = P9_31;   // Select which pin to toggle.

    pru0_dram[ch] = on[ch];         // Copy to DRAM0 so the ARM can change it
    pru0_dram[ch+MAXCH] = off[ch];  // Copy after the on array
    
    while (1) {
        //onCount[ch] = pru0_dram[2*ch];      // Read from DRAM0
        
        __R30 |= gpio;      // Set the GPIO pin to 1
        __delay_cycles(1);
        __R30 &= ~gpio;     // Clearn the GPIO pin
        __delay_cycles(0);
    }
}
