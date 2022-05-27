import csv

class Test_Tool:
	def __init__(self, file_name):
		self.customer_sample_csv = file_name
		self.customer_lists = self._read_csv_rows("./full_data/customer.csv")
		self.invoice_lists = self._read_csv_rows("./full_data/invoice.csv")
		self.invoice_item_dict = self._read_csv_file_as_dict("./full_data/invoice_item.csv")

	def _read_csv_rows(self, file_name: str) -> list:
		"""
		Read a csv file and put the result into a list

		:param file_name: The file to read
		:return: A list of lists containing all the records of the file. Each list represents a record
		:rtype: list
		"""
		row_list = []
		with open(file_name, "r") as csv_file:
			reader = csv.reader(csv_file, delimiter=",")
			for row in reader: 
				row_list.append(row)
			return row_list

	def _read_csv_file_as_dict(self, file_name:str) -> dict:
		"""
		Read a csv file and put the result into a dictionary. The dictionary can later
		be used for better search capabillities.

		:param file_name: The file to read
		:return: A dictionary containing all the records of the file. Keys are unique elements of a record
		and the values a list of lists containing all the information of a record
		:rtype: dict
		"""
		record_dict = {} 
		with open(file_name, "r") as csv_file:
			reader = csv.reader(csv_file, delimiter=",")
			for record in reader:
			    if record[0] in record_dict.keys():
			    	record_dict.get(record[0]).append([record[0], record[1], record[2], record[3]])
			    	continue
			    record_dict[record[0]] = [[record[0], record[1], record[2], record[3]]]

		return record_dict

	def _write_to_csv_file(self, file_name: str, record_lists: list) -> None:
		"""
		Write a list to a csv file

		:param file_name: The file to write
		:param record_lists: The lists of records to be written
		"""
		with open(file_name, 'a', encoding='UTF8') as f:
			writer = csv.writer(f)
			for record in record_lists:
				writer.writerow(record)

	def _search_patient_record(self, record_id: str) -> list:
		"""
		Search if a specific customer exist in customer_lists

		:param record_id: The customer id to be found
		:return: A list containing all the information of the specific customer
		:rtype: list
		"""
		for customer_record in self.customer_lists:
			if record_id in customer_record:
				return customer_record		

	def _search_invoice_record(self, record_id: str) -> list:
		"""
		Search if a specific invoice exist in invoice_lists

		:param record_id: The customer id to be found
		:return: A list containing all the invoices of a specific customer
		:rtype: list
		"""
		temp_list = []
		for invoice_record in self.invoice_lists:
			if record_id in invoice_record:
				temp_list.append(invoice_record)
		return temp_list

	def _search_invoice_item_records(self, record_id: str, file_name:str) -> list:
		"""
		Search if a specific invoice exist in invoice_lists

		:param record_id: The customer id to be found
		:return: A list containing all the invoices of a specific customer
		:rtype: list
		"""
		record_dict = self._read_csv_file_as_dict(file_name)
		if record_id in record_dict:
			return record_dict.get(record_id)


	def run_test(self):
		"""
		Run the required test and write the results in 3 seperate files

		"""
		customer_id_list = self._read_csv_rows(self.customer_sample_csv)

		for customer_id in customer_id_list:
			customer_record = self._search_patient_record(customer_id[0])
			if customer_record:
				self._write_to_csv_file("./extracted_data/customer.csv", [customer_record])
				invoice_records = self._search_invoice_record(customer_id[0])
				if invoice_records:
					self._write_to_csv_file("./extracted_data/invoice.csv", invoice_records)
					for invoice_record in invoice_records:
						invoice_item_records = self._search_invoice_item_records(invoice_record[1], "./full_data/invoice_item.csv")
						self._write_to_csv_file("./extracted_data/invoice_item.csv", invoice_item_records)


if __name__ == "__main__":

	print("Please provide the path of the customer sample file.Press 'Enter' to run the program with the default file")
	value = input()

	if value:
		tool = Test_Tool(value)
	else:
		tool = Test_Tool("./customer_sample.csv")

	tool.run_test()
	