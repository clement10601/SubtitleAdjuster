SubtitleAdjuster
================

Adjust Subtitle's time line with specific Frame numbers &amp; Frame rate

Ver 1.0.0

EXE: https://drive.google.com/file/d/0B0mK4iRZOQuXbVVQLWtJUnB5WEE/view?usp=sharing


  Options:
  
    --version : Prints the version number
    
    --help    : Display the help
    
  Arguments:
  
    -i        {str}[Full Path of the ASS subfile]  
    
    -f        {int}[frame]               
    
    -r  	    {float}[frame rate]     
    
  Usage:
  
    SubtitleAdjuster.exe -f 50 -r 23.976 -i C:/test.ass
    
      Output:
      
        C:/new.test.ass    (+50 frames)
        

by DHR動研 CL
