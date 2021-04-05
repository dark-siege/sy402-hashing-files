I stored the file by by first going through each file and hashing it with sha256.
There were some issues reading certain files throughout my path so I had to create a try and except
statement.
I read the data that I am looking at for each file in specified chunks and hash it.
After that, I hexdigest the file and write that into a new file that I created originally 
before my 'for' loop.
