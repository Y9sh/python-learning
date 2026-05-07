# ✨ 🌟 Multiplication Table Generator with Nested Loops
# 💡 Concept Workflow
# Function input: A number n (user input).
# Nested loop: Outer loop = rows; inner loop = columns.
# Print formatted multiplication table (aligned, readable).

# ALL AI MAKE
def multiplication_table(n):
    print(f"Multiplication Table up to {n}")
    for i in range(1, n + 1): # rows 
        for j in range(1, n + 1): # columns
            print(f"{i*j:4}", end=" ")  #print each product with spacing (4 characters wide) and stay on same line
        print()  # New line after each row

# Run the function
num = int(input("Enter number for table: "))
multiplication_table(num)

def multi_table_list(n):
    table= []
    for i in range(1,n+1):
        row=[]
        for j in range(1,n+1):
            row.append(i*j)
        table.append(row)
    return table
print(multi_table_list(4))

def table_only_even(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            mltp = i+j
            if mltp % 2 == 0:
                print(f"{mltp:5}",end=" ")
            else: 
                print("  -", end=" ")
        print()
print(table_only_even(10))

def multiplication_table_even(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            product = i * j
            if product % 2 == 0:
                print(f"{product:4}", end=" ")
            else:
                print("   -", end=" ")  # dash for odd products
        print()
print(multiplication_table_even(10))



        
'''
Why learned this ? 
Nested loops are fundamental for:
Tables

Grids (like AI feature maps, matrix ops)

Multi-level data processing
'''