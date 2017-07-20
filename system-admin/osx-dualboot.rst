install ubuntu alongisde osx



boot into osx and paritition the disk
----------------------------------------

   1. applications --> utilities --> disk utility
   2. partition disk as fat

Install rEFInd
-------------------

   1. Download it
      cd ~/Downloads
      https://sourceforge.net/projects/refind/
      unzip refind-bin-0.10.8.zip
     
   2. Power off
   3. Hold down Command+R as the chime sounds
   4. When the OS has booted, select Utilities->Terminal
   5. cd  /Volumes/my_mac/Users/adam/Downloads/refind-bin-0.10.8
   6. sudo ./refind-install

   you should see 'Installation has completed successfully'     
   when you reboot it should show refind at boot

troubleshooting
-------------------

   * mount it to efi partition
      diskutil list
      mount /dev/disk0s1        # or whatever the device and partition
      sudo ./refind-instal

   * sometimes when a new version of osx is installed you will need to repeat this process


palm detection
^^^^^^^^^^^^^^^^^^^

you can change the sensitivity of what is considered a touch with

   $ synclient PalmMinZ=100

   
funny key mapping
^^^^^^^^^^^^^^^^^^^^

https://askubuntu.com/questions/530325/tilde-key-on-mac-air-with-ubuntu
