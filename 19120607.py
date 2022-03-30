def nhapMaTran(hang, cot):
    ma_tran = []
    for i in range(hang):
        a = []
        for j in range(cot):
            print("\tPhan tu thu [{0}][{1}] la:".format(i+1, j+1), end=" ")
            a.append(float(input()))
        ma_tran.append(a)
    return ma_tran

def row_Switch(A,i,j):
    # Hoan vi dong
    c=len(A[0])
    for k in range(c):
        temp=A[i][k]
        A[i][k]=A[j][k]
        A[j][k]=temp
    return A

def mul_scalar(A,i,t):
    # Nhan 1 dong voi 1 hang so
    c=len(A[0])
    for k in range(c):
        A[i][k]= t*A[i][k]
    return A

def add_row(A,i,j,t):
    # Cong dong i voi K lan dong j
    c=len(A[0])
    for k in range(c):
        A[i][k]=A[i][k]+ t*A[j][k]
    return A

def col_leading(A):
    # Tim cot khac 0 dau tien cua ma tran
    c= len(A[0])
    r= len(A)
    for i in range(c):
        for j in range(r):
            if A[i][j]!=0:
                return j


def Gauss(A):
    a=col_leading(A)
    c=len(A[0])
    r= len(A)

    if A[0][0]==0:
        for i in range(r):
            if A[0][i]!=0:
                row_Switch(A,0, i)
    mul_scalar(A,0, 1/A[0][0])

    for i in range(0,c-1):
        for j in range(1,r):
            add_row(A,j,i,-A[j][i])
            # mul_scalar(A,i,1/A[i][i])


    return A
        
hang=(int(input("Nhap so hang: ")))
cot= (int(input("Nhap so cot: ")))
print("Nhap ma tran: ")
matrix=(nhapMaTran(hang, cot))
# print(matrix)

print(len(matrix))
print(len(matrix[0]))
Gauss(matrix)
print(matrix)
print("abc")
