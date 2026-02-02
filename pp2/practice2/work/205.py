n=int(input())
def is_power_of_two (n):

    if n<=0:

        print("NO")
    else:

       while n%2==0:

        n//=2

    if n==1:

        print("YES")

    else:

        print("NO")

is_power_of_two(n)
 