# data-strip
Tool for stripping conductivity and pH vales from CSV files generated by an industrial monitor

The monitor records half-hourly values in this format:

01.10.2020 00:00:03;   2.2; ; ;  6.99; ; ; Inactive; Off; Off; Off; Off; 

Spacing is consistent. Conductivity comes after date/time, then pH.  One CSV per day. Normal line length is 74 chars. Blank line is 1 char - this is used to skip blank lines in source CSVs (I think generated when SD card is removed from instrument) to prevent script crashing.


Script iterates directory containing source CSVs. Then takes conductivity or pH (one script for each), averages the half-hourly values from each CSV, then adds to a new CSV with collated data. For pH, both an arithmetic mean and a mean converted via [H+] are calculated.  Finally writes the daily averages to a new CSV.

To-do:
Could combine pH and conductivity into one script
Implement Python CSV library (re: DH: "more robust")
