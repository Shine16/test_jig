#!/bin/bash
echo "insert driver"
sleep 1
sudo insmod /home/biqmind/Downloads/AX99100_SP_PP_SPI_LINUX_Driver_v1.4.0_Source/ax99100.ko 
echo "change baud rate"
sleep 1
sudo /home/biqmind/Downloads/AX99100_SP_PP_SPI_LINUX_Driver_v1.4.0_Source/select_BR
echo "start wpantund"
sleep 1
sudo wpantund &
xdotool key alt+ctrl+t & sleep 1
xdotool type "wpanctl scan -c 25"



