## Board Setup Requirements

## Requirements for Board Bringup
*	12V Power adapter
*	UART adapter with ribbon cable (TB39)
*	USB to UART adapter	(https://www.cadyce.com/shop/cables-adapters/usb-2-0/ca-us9/)
*	Ethernet cable
*	Host PC to connect the UART and Ethernet cable to.
*	TFTP Server installed in Host PC
*	UART settings should be 115200 8N1
*	
## Additional Requirements for USB Based Board Recovery
*	USB A to A cable with the VCC pin cut
*	Windows PC 
*	The needed Software are listed in the [USB EDL](usb_edl.md) recovery section. 

## The Setup
        +-------------------+                +----------------------+
        |       PC          |                |   Device Under Test  |
        |                   |                |                      |
        |  	     [Ethernet] |<---Ethernet--->| [Ethernet]           |
        |	       [Port]   |                | [Port]               |
        |                   |                |                      |
        |  	        [USB]   |<--USB A to A-->| [USB]                |
        |	        [Port]  |                | [Port]               |
        |                   |                |                      |
        |                   |                |                      |
        |  [USB Port]       |                |     [UART Port]      |
        +---------+---------+                +----------+-----------+
                  |                                     |
                  |                                     |
              USB Cable                             Ribbon Cable
                  |                                     |
                  |                                     |
                  +-------------USB--<>--TB39-----------+
                                to       Dongle
                               Serial
                               Adapter
                               
**Note**: The USB A to A connection is neeeded only for USB recovery mode
