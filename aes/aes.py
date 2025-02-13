# write code to shift rows in a matrix (ith row gets shifted by i circularly towards left)
state=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def shift_rows(state):
    for i in range(len(state)):
        state[i] = state[i][i:] + state[i][:i]
    return state 
print(shift_rows(state))

# Precomputed Galois Field multiplication tables
mul2 = [i << 1 ^ (0x1B if i & 0x80 else 0) for i in range(256)]
mul3 = [mul2[i] ^ i for i in range(256)]

def mixColumns(state):
    for c in range(4):  # Iterate over columns
        a = state[0][c]
        b = state[1][c]
        c_ = state[2][c]
        d = state[3][c]

        state[0][c] = mul2[a] ^ mul3[b] ^ c_ ^ d
        state[1][c] = a ^ mul2[b] ^ mul3[c_] ^ d
        state[2][c] = a ^ b ^ mul2[c_] ^ mul3[d]
        state[3][c] = mul3[a] ^ b ^ c_ ^ mul2[d]

    return state