 # Define a pytest test method **'test_creating_empty_inventory'**, which creates an empty inventory and checks if its 'balance_inventory' is an empty dict using assert.
    def test_creating_empty_inventory(self):
        c1 = MobileInventory()
        assert c1.balance_inventory == {}

    # Define a pytest test method **'test_creating_specified_inventory'**, which checks if inventory instance with input {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}.
    def test_creating_specified_inventory(self):
        c_dict = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        assert c_dict.balance_inventory() == {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25} 

    # Define a pytest test method  **'test_creating_inventory_with_list'**, which checks if the  method raises a TypeError with the message "Input inventory must be a dictionary" when a list "['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z']" is passed as input using assert.
    def test_creating_inventory_with_list(self):
        with pytest.raises(TypeError) as e:
          c_list = MobileInventory(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
        assert str(e.value) == 'Input inventory must be a dictionary'

    # Define a pytest test method **'test_creating_inventory_with_numeric_keys'**, which checks if the  method raises a ValueError with the message "Mobile model name must be a string" using assert, when the dict {1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'} is passed as input.
    def test_creating_inventory_with_numeric_keys(self):
        with pytest.raises(TypeError) as e:
          c2 = MobileInventory({1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'})
        assert str(e.value) == 'Mobile model name must be a string'

    # Define a pytest test method **'test_creating_inventory_with_nonnumeric_values'**, which checks if the  method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert, when the dict {'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'} is passed as input.
    def test_creating_inventory_with_nonnumeric_values(self):
        with pytest.raises(TypeError) as e:
          c2 = MobileInventory({'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'})
        assert str(e.value) == 'No. of mobiles must be a positive integer'

    # Define a pytest test method **'test_creating_inventory_with_negative_value'**, which checks if the  method raises a ValueError with the message "No. of mobiles must be a positive integer" using assert, when the dict {'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25} is passed as input.
    def test_creating_inventory_with_negative_value(self):
        with pytest.raises(ValueError) as excinfo:
            c3 = MobileInventory({'iPhone Model X': -45, 'Xiaomi Model Y': 200, 'Nokia Model Z': 25})
        assert  str(excinfo.value) == "No. of mobiles must be a positive integer"
	# Define another pytest test class **'TestInventoryAddStock'**, which tests the behavior of the **'add_stock'** method, with the following tests