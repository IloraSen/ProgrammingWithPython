import numpy as np
sales = [0,5,155,0,518,0,1827,616,317,325]
sales_array=np.array(sales)
print(sales_array)

my_list= np.arange(1,11)
print(f"ndim:  {my_list.ndim}")
print(f"shape:  {my_list.shape}")
print(f"size:  {my_list.size}")
print(f"dtype:  {my_list.dtype}")

array_random = np.random.random(9).reshape(3,3)
print(array_random[:2,:])
