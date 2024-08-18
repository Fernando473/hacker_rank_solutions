You're working on a customer service chat bot
which help to make life easier for the customer service
representatives of a new client.

The client is asking for an application which can extract order numbers from the
text which can extract order numbers from the 
text client sends.

Fortunately, there's a consistent format for order numbers.
They all look like the following:
    
    `NNN.NNNN.A`
    where `N` is a digit and `A` is a letter.

Note that the dots are optional.
The following are valid and invalid numbers

- `123.4567.A` is a valid order number
- `1234567A` is a valid order number
- `123.4567` is not a valid order number
- `123.4567.A.` is not a valid order number
- `039.1178.C` is a valid order number
- `RYZ.1187.C` is not a valid order number
- `877.2304` is not a valid order number

The client has a strict policy on not using 
booleans so the system must return a "1" if the text contains
a valid order numer, or a "0" otherwise.


Write a function which, given the text
provided by the client will return 1 when there is a valid
order number in the text, and 0 when there is not.

Some text input examples are:
- `The order number is 123.4567.A`
- `The order number is 1234567A`
- `Oh, I don't have an order number`
- `Yes I have an order number 1158686X`