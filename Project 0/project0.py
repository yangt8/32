n=int(input())
s=' '
def downward_block_diagonal(n:int):
    print("+-+")
    for i in range(n-1):
        print(s*i*2 + "| |")
        print(s*i*2 + "+-+-+")
    print(s*2*(n-1) + "| |")
    print(s*2*(n-1)+ "+-+")
downward_block_diagonal(n)


