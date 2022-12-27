
def aryabhata_integer_square(n):
	n = [int(m) for m in n]
	print(n)
	result = [0]*(len(n)*2+1)
	r = n[0] * n[0]
	result[0] = r % 10
	result[1] = r // 10
	base_idx = 1
	for k in range(1, len(n)):
		for i in range(0, k):
			r = result[base_idx + i] + 2 * n[i] * n[k]
			result[base_idx + i] = (r % 10)
			result[base_idx + i + 1] += (r // 10)
		r = result[base_idx + k] + n[k] * n[k]
		result[base_idx + k]  = (r%10)
		result[base_idx + k + 1] += (r // 10)
		base_idx += 1
	return result


def str_reverse(s):
    return "".join(reversed(s) )     

if __name__ == "__main__":
    import sys
    import math
    n = int(sys.argv[1])
    n_str = str_reverse(sys.argv[1])
    res = aryabhata_integer_square(n_str)
    res = int("".join(str(s) for s in reversed(res)))
    print(res)
    if n**2 == res:
    	print("Success")
    else:
    	print("Failed")
