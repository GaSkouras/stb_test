# Stone Brunch-Dream Candies Tool
 A [test automation](./STB_DreamCandies_Tool.pdf) proccess that continuously verify correctness of Dream Candies implementation.
 
 ### Execution
 Execute the program by typing 
 ```bash
python tool.py
```
The program will request the path for the input file from the user. The user may press "Enter" in order to let the program run with the default input file.

### Explanation of functionallity

####  Initialize
Upon intantiating an object of Test_Toll Class the __init__() function takes the input file as argument and creates three lists that hold the information of full_data
that can be used later for searching an object.

### Run Tests

This public method is responsible for the core of the functionallity. At first it reads the input file and for each CUSTOMER_CODE it searches the ./full_data/costumer.csv file and if that CUSTOMER_CODE exist it writes it to the ./extracted_data/customer.csv file. Then for that CUSTOMER_CODE the function search the ./full_data/invoice.csv and writes to ./extracted_data/invoice.csv file the matching data. Finally a final search is being made for each INVOICE_CODE in the ./full_data/invoice_items.csv and the records that match this INVOICE_CODE are written in the extracted_data folder.

#### Time Complexity
Lists has O(n) complexity for search. Although that this is not a problem if the number of records are not too high, an optimize has been made when the program searches
for invoice_item records. While reading the input_item.csv file the records are being placed in a dictionary that each key holds "INVOICE_CODE" element and the value holds a list of lists with the full information of that record. If an INVOICE_CODE is present more than, we append the data of that record in the corresponding list.

As a result the final dict has te following format
 ```bash
 {
 "INVOICE_CODE_1": [["INVOICE_CODE_1", "ITEM_CODE_1", "AMOUNT_1", "QUANTITY_1"], [["INVOICE_CODE_2", "ITEM_CODE_2", "AMOUNT_2", "QUANTITY_2"]]],
 "INVOICE_CODE_2": [["INVOICE_CODE", "ITEM_CODE", "AMOUNT", "QUANTITY"],]
 } 
 ```
Because python dictionaries are implemented as hash tables, this represantation offers an immense boost when searching for an object, as the time complexity is constant O(1).



