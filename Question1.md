# Question #1:
The programmer wants to count down from 10 to 0.  What is wrong and how to fix it? 

```python 
i = 10
while i == 0:
  print(i) 
  i -= 1
```

Write your answer below:
------------------------
The while loop condition never evaluates to True so the body of the loop will never execute.
To fix this, we need to change the condition to i >= 0.