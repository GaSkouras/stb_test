import csv

class Test_Tool:
	def __init__(self, file_name):
		self.customer_sample_csv = file_name

	def _read_csv_row(self, file_name: str) -> list:
		row_list = []
		with open(file_name, "r") as csv_file:
			reader_variable = csv.reader(csv_file, delimiter=",")
			for row in reader_variable: 
				row_list.append(row)
			return row_list # The first row is the header

	def _write_to_csv_file(self, file_name: str, record: list) -> None:
		with open(file_name, 'a', encoding='UTF8') as f:
			writer = csv.writer(f)
			writer.writerow(record)

	def _read_customer_sample_csv(self) -> list:
		"""
		Read the file that contains the customers that we are interested in and save their id to a list

		return: The list of customers
		rtype: list
		"""
		customer_list = self._read_csv_row(self.customer_sample_csv)
		return customer_list

	def _search_customer_record_from_csv(self, customer_id: str):
		customer_record_lists = self._read_csv_row("./full_data/customer.csv")
		# print(customer_record_lists)
		for ls in customer_record_lists:
			if customer_id in ls:
				return ls


	def run_test(self):
		customer_id_list = self._read_customer_sample_csv()
		# print(customer_id_list)
		for customer_id in customer_id_list:
			customer_record = self._search_customer_record_from_csv(customer_id[0])
			if customer_record:
				self._write_to_csv_file("./extracted_data/customer.csv", customer_record)

		


if __name__ == "__main__":
    
	tool = Test_Tool("./customer_sample.csv")
	tool.run_test()
	