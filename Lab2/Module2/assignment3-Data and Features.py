import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
df = pd.read_csv(r'servo.data', sep = ',', 
                 names = ['motor', 'screw', 'pgain', 'vgain', 'class'])


# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
#print(df.shape)
row = (df[df.vgain == 5])
print(len(row))
#print(row)

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
soc = (df[(df.motor == 'E') & (df.screw == 'E')])
#print (soc)
print(len(soc))


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
bro = (df[df.pgain == 4])
#print(bro)
print(bro['vgain'].mean(axis = 0))
#print(bro['vgain'].mean())
#print(bro.describe())


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
print(df.dtypes)


