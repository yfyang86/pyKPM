Keyword: shell, awk
Function: Column Sum per line

# Prefered Answer

```bash
awk '{s+=$1} END {printf "%.0f", s}' mydatafile
```

# Default Answer

```bash
I=0

for N in `cat numbers.txt`
do
    I=`expr $I + $N`
	done

	echo $I
```


