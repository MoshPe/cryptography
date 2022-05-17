

int isPrime(n)
{
    int i, flag = 0;
    int m = n / 2;
    for (i = 2; i <= m; i++)
    {
        if (n % i == 0)
        {
            flag = 1;
            break;
        }
    }
    if (flag == 0)
    {
        printf("Number is prime");
        return 1;
    }

    return 0;
}