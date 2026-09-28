# Name Formatter and Collector

A simple Python script that takes user inputs for first, middle, and last names, formats them into a single full name, and displays the result. It runs in a loop to collect multiple names.

## Features

- **Optional Middle Name:** Smartly handles cases where a user does not have a middle name without leaving extra spaces.
- **Automated Counter:** Keeps track of the number of entries processed.
- **Clean Output:** Formats each entry with a clear separator line.

## How it Works

1. The script initializes a counter at `0`.
2. It prompts the user to enter a **First Name**, **Middle Name** (optional), and **Last Name**.
3. It combines the inputs cleanly depending on whether a middle name was provided.
4. It prints the combined **Full Name**.
5. The loop repeats until the counter reaches the specified limit.

> **Note on Loop Limit:** In the current code, the loop stops after collecting **3 names**, although the success message text says *"Collected 5 names"*. You can change `if count == 3:` to `if count == 5:` if you want to collect exactly 5 names.


## Example Output

```text
Enter First Name: Rahul
Enter Middle Name (optional): Kumar
Enter Last Name: Sharma
Full Name: Rahul Kumar Sharma
----------
Enter First Name: Priya
Enter Middle Name (optional): 
Enter Last Name: Patel
Full Name: Priya Patel
----------
```
