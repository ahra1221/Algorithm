#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N, B;
    cin >> N >> B;

    string result = "";
    while (N > 0)
    {
        int tmp = N % B;
        if (tmp < 10)
            result += ('0' + tmp);
        else
            result += ('A' + (tmp - 10));
        N /= B;
    }
    reverse(result.begin(), result.end());
    cout << result;
    return 0;
}