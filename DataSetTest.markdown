Test Data.

Tested various inputs for the expense tracking fields, namely \`date\`,
\`amount\`, \`category\`, and \`description\`. Here are some examples:

\- Test Case 1: \`date\` = 07/11/2023, \`amount\` = 200.50, \`category\`
= \"Groceries\", \`description\` = \"Weekly grocery shopping\"

\- Test Case 2: \`date\` = 07/12/2023, \`amount\` = 40.00, \`category\`
= \"Transportation\", \`description\` = \"Gas for car\"

\- Test Case 3: \`date\` = 07/13/2023, \`amount\` = 1200.00,
\`category\` = \"Rent\", \`description\` = \"Monthly rent\"

\- Test Case 4: \`date\` = empty, \`amount\` = 200.50, \`category\` =
\"Groceries\", \`description\` = \"Weekly grocery shopping\"

\- Test Case 5: \`date\` = 07/11/2023, \`amount\` = \"two hundred\",
\`category\` = \"Groceries\", \`description\` = \"Weekly grocery
shopping\"

2\. The data sets I tested against.

The above test cases were used to test the functionality of the program.
The results were as follows:

\- Test Case 1: The program correctly recorded the expense and displayed
the success message.

\- Test Case 2: The program correctly recorded the expense and displayed
the success message.

\- Test Case 3: The program correctly recorded the expense and displayed
the success message.

\- Test Case 4: The program correctly identified that the \`date\` field
was empty and displayed an error message.

\- Test Case 5: The program correctly identified that the \`amount\`
field was not a number and displayed an error message.

3\. A brief written explanation of the results of my tests and what I
had to fix.

The testing process revealed that the program works as intended for
valid input data. It correctly records expenses and displays a success
message. The input validation feature also works correctly, as it
identifies when required fields are left empty or when the \`amount\`
field does not contain a valid number. No fixes were required for these
features.

However, I encountered an issue with displaying a second image when the
\"Track Expenses\" button was clicked. With several attempts to fix
this, I was unable to resolve the issue. The code was left without the
second image.

![alt text](TestAttempt1.png)


![alt text](https://github.com/yourusername/your-repository/blob/main/TestAttempt2.png)

![alt text](https://github.com/yourusername/your-repository/blob/main/TestAttempt3.png)

![alt text](TestAttempt4.png)

![alt text](TestAttempt5.png)

