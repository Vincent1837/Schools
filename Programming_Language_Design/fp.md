# Final Project

# Collaborative Sheets

- In this assignment, you are asked to implement a collaborative sheets like Google Sheets.
- Requirements:
    1. Able to create users
    2. Let users can create their new sheet
    3. Let users can print out their sheet
    4. Let users can change the content of their sheet
    5. Let sheet has two access rights, read-only or editable, for every user
    6. Let users can share their sheet with other users
    7. Let sheets can deal with rational arithmetic `+` , `-` , `*` , `/`
        
        Possible input: rational number like `123.456` , `123` and operators like `+` , `-` , `*` , `/`
        
    - Furthermore, please make the requirements 5. & 6. can be easily switched on/off.
        
        For instance, to switch off the requirement 5. , you can remove some code, not inherit some class, or not generate some object, etc.
        
- This is a group assignment. Each group submits one copy to ee-class.
- There is no constraint on what language you use. But…
    - Bonus points if you use Scala, Haskell or Lisp
    - Bonus points if you use functional programming
- The details of each requirement are up to you.

# Submission

- Your source code
- The report
    - File format `.pdf`
    - If it is convenient, write it in Chinese to be friendly to TA
    1. Overview of your source code
        - How does it work
        - Data structures you defined
        - Specify how you switch on/off some functionalities
    2. Programming paradigm you used
        - What are the features
        - How to use it in your source code
    3. Programming paradigm you did not use (choose one)
        - What are the features
        - What is the difference using it in source code
    4. Idioms or Design Patterns you used
        - What are the features
        - How to use it in your source code
    5. Idioms or Design Patterns you did not use (choose one)
        - What are the features
        - What is the difference using it in source code
    6. Errors encountered during programming
        - What happened
        - How to use Debugger to solve it

# Example

```
---------------Menu---------------
1. Create a user
2. Create a sheet
3. Check a sheet
4. Change a value in a sheet
5. Change a sheet's access right.
6. Collaborate with an other user
----------------------------------
> 1
> Kevin
Create a user named "Kevin".

---------------Menu---------------
1. Create a user
2. Create a sheet
3. Check a sheet
4. Change a value in a sheet
5. Change a sheet's access right.
6. Collaborate with an other user
----------------------------------
> 2
> Kevin SheetA
Create a sheet named "SheetA" for "Kevin".

---------------Menu---------------
1. Create a user
2. Create a sheet
3. Check a sheet
4. Change a value in a sheet
5. Change a sheet's access right.
6. Collaborate with an other user
----------------------------------
> 3
> Kevin SheetA

0, 0, 0,
0, 0, 0,
0, 0, 0,

---------------Menu---------------
1. Create a user
2. Create a sheet
3. Check a sheet
4. Change a value in a sheet
5. Change a sheet's access right.
6. Collaborate with an other user
----------------------------------
> 4
> Kevin SheetA

0, 0, 0,
0, 0, 0,
0, 0, 0,

> 1 2 3

0, 0, 0,
0, 0, 3,
0, 0, 0,

---------------Menu---------------
1. Create a user
2. Create a sheet
3. Check a sheet
4. Change a value in a sheet
5. Change a sheet's access right.
6. Collaborate with an other user
----------------------------------
> 4
> Kevin SheetA

0, 0, 0,
0, 0, 0,
0, 0, 0,

> 1 2 1.5+2

0, 0, 0,
0, 0, 3.5,
0, 0, 0,

---------------Menu---------------
1. Create a user.
2. Create a sheet.
3. Check a sheet.
4. Change a value in a sheet.
5. Change a sheet's access right.
6. Collaborate with an other user.
----------------------------------
> 5
> Kevin SheetA ReadOnly

---------------Menu---------------
1. Create a user.
2. Create a sheet.
3. Check a sheet.
4. Change a value in a sheet.
5. Change a sheet's access right.
6. Collaborate with an other user.
----------------------------------
> 4
> Kevin SheetA

0, 0, 0,
0, 0, 3.5,
0, 0, 0,

> 1 2 2
This sheet is not accessible.

0, 0, 0,
0, 0, 3.5,
0, 0, 0,

---------------Menu---------------
1. Create a user
2. Create a sheet
3. Check a sheet
4. Change a value in a sheet
5. Change a sheet's access right.
6. Collaborate with an other user
----------------------------------
> 6
> Kevin SheetA Ray
Share "Kevin"'s "SheetA" with "Ray".
```