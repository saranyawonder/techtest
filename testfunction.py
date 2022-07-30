
def custExtract(inputfile,outputfile):
    import pandas as pd
    data = pd.read_csv(inputfile)
    np_filter = data.values[(data.age >= 40) & (data.age <= 59)]
    df_out = pd.DataFrame(np_filter, columns=['Name', 'Age', 'Address', 'Phone', 'Email Address'])
    df_result = df_out[['Name', 'Phone', 'Email Address']]
    df_result.to_csv(outputfile, index=False)
    print("Customer's data who paid incorrect amount created at: "+ outputfile)

#Invoke the fuction by providing two parameters, where first parameter should be Inputfilepath and second parameter output filepath
custExtract('C:\\temp\\latest-customers.txt','C:\\temp\\affected-customers.txt')
