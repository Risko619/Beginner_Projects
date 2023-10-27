# Client stored data in a 'data' variable
data = "14inch l@ptop,699|16inch l@ptop,999|sm@rtphone,1099|t@blet,499|g@ming pc,1999"
# I created a new variable to store the list, and used .split to use space instead of "|"
device_list = data.split("|")
# Here is where our correct info will append into later on
formatted_list = []

# Here we seperate the type and device price by further splitting device data within a 'for loop'
for device in device_list:
  device_info_list = device.split(",")
  name = device_info_list[0]
  price = int(device_info_list[1])

 # Here we add a 10% increase due to inflation by multiplying it by 1.1
  new_price = int(price * 1.1)
  
 # Format the information 
  formatted_device = f"Device Name: {name}, Device Price: ${price}"
 
 # Correct clients typing error 
  corrected_formatted_device = formatted_device.replace("@","a")
 
 #Finally we populate the data into the formatted list from earier 
  formatted_list.append(corrected_formatted_device)

print(formatted_list)

'''In this program we managed to convert strings of information that was difficult to read
into a more organized list of information.'''
# Cleaned and formatted ddata containing info about some devices.
# We can further play around by adding more info such as warranty etc into the data variable.