
import pandas

mag_file_name = "amplifier_measured.csv"

file_data = pandas.read_csv(mag_file_name, sep=',', skiprows=13, header=None)
freq = file_data[0].to_numpy()
amplitude = file_data[1].to_numpy() 

#open out file
f = open("vsource.txt", "w")

f.write("V10 1 0 DC 0 AC 1\n")
f.write("Efreq1 ref 0  FREQ {V(1,0)}=\n")

for index in range(len(freq)):
	f.write("+(%f, %f, 0)\n" %(freq[index], amplitude[index]))


#V10 1 0 DC 0 AC 1
#* MAG requires  (freq, magnitude, degree)
#Efreq1 ref 0  FREQ {V(1,0)}= MAG
#+(1e6, 0.893, -26.7)
#+(2e6, 0.705, -45.2)  
#+(5e6, 0.37, -68.3)
#+(10e6, 0.195, -78.7)