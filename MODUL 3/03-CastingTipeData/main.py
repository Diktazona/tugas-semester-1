#casting adalah cara mengubah tipe data variabel

#INTEGER
print("===INTEGER===")
data_int=9
print ("data", data_int, "tipe data = ", type(data_int))

#casting
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print ("data = ", data_float, "tipe data = ", type(data_float))
print ("data = ", data_str, "tipe data = ", type(data_str))
print ("data = ", data_bool, "tipe data = ", type(data_bool))


#FLOAT
print ("===FLOAT===")
float_data = 3.14
print("data = ", float_data, "tipe data = ", type(float_data))