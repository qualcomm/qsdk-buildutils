## Board Setup Requirements

## Requirements for Board Bringup
*	12V Power adapter
*	UART adapter with ribbon cable (TB39)
*	USB to UART adapter	(https://www.cadyce.com/shop/cables-adapters/usb-2-0/ca-us9/)
*	Ethernet cable
*	Host PC to connect the UART and Ethernet cable to.
*	UART settings should be 115200 8N1

       	+-------------------+                +----------------------+
        |       PC          |                |   Device Under Test  |
        |                   |                |                      |
        |                   |                |                      |
        |  	     [Ethernet] |<---Ethernet--->| [Ethernet]           |
        |	       [Port]   |                | [Port]               |
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

## Requirements for Board Recovery
*	USB A to A cable with the VCC pin cut
*	Windows PC 
*	The needed Software are listed in the USB EDL recovery section. 
