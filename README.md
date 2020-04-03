# LL-first-follow
First and Follow functions are used to aid the LL algorithm in parsing.

And then use First and Follow functions to compute the parsing table  

# How to use 

1. Compute First as follows
```
from  first import getFirst
firstMap = getFirst(input)
```

2. Compute Follow as follows

```
from  follow import  getFollow
       
followMap = getFollow(input)

```

3. Compute Parsing Table as follows

```

from parsingtable import  createParseTable

input = "./expression"
table = createParseTable(input)
```