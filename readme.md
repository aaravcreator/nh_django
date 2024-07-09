## TERMINAL COMMANDS REVIEW(POWERSHELL AND GITBASH / LINUX)
- `cd dir_name` to go to dir_name
- `cd ..` to go to parent directory
- `ls` to list files in current directory
- `pwd` to print working directory
- `mkdir dir_name` to make a new directory
- `touch file_name` to make a new file
- `rm file_name` to remove a file
- `rm -r dir_name` to remove a directory

## CREATING VIRTUAL ENVIRONMENT AND ACTIVATING AND DEACTIVATING 
```bash
# Step 1: Navigate to your project directory
cd path/to/your/project

# Step 2: Create a virtual environment
python -m venv venv

# Step 3: Activate the virtual environment
# On Windows
.\venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate

(venv) will be shown after activation
# Your virtual environment is now active.
# You can install packages using pip and work on your project.

# To deactivate the virtual environment when you're done
deactivate
```

Sure, here is a simple task involving variables and lists in Python to help you practice.

### Task: 
Write a Python script that performs the following:

1. **Create and assign variables:**
   - Create three variables `a`, `b`, and `c` and assign them the values `5`, `10`, and `15` respectively.
   
2. **Perform arithmetic operations:**
   - Calculate the sum of `a` and `b` and store the result in a variable called `sum_ab`.
   - Calculate the product of `b` and `c` and store the result in a variable called `product_bc`.
   
3. **Create and manipulate a list:**
   - Create a list called `numbers` containing the variables `a`, `b`, and `c`.
   - Append the value of `sum_ab` to the list.
   - Insert the value of `product_bc` at the second position in the list.
   - Remove the first element from the list.
   
4. **Print the results:**
   - Print the values of `sum_ab` and `product_bc`.
   - Print the final state of the list `numbers`.

### Example Output:
```
Sum of a and b: 15
Product of b and c: 150
Final list: [150, 10, 15, 15]
```

### Solution:

Here is a Python script that accomplishes the task:

```python
# Step 1: Create and assign variables
a = 5
b = 10
c = 15

# Step 2: Perform arithmetic operations
sum_ab = a + b
product_bc = b * c

# Step 3: Create and manipulate a list
numbers = [a, b, c]
numbers.append(sum_ab)
numbers.insert(1, product_bc)
numbers.pop(0)

# Step 4: Print the results
print("Sum of a and b:", sum_ab)
print("Product of b and c:", product_bc)
print("Final list:", numbers)
```

Try running this script in your Python environment and observe the output to ensure you understand how variables and lists work in Python.