#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, B;
    cin >> N >> B;

    string s = "";

    if (N == 0)
    {
        cout << 0;
        return 0;
    }

    while (N > 0)
    {
        int tmp = N % B;
        if (tmp >= 10)
            s += 'A' + (tmp - 10);
        else
            s += '0' + tmp;
        N /= B;
    }
    reverse(s.begin(), s.end());
    cout << s;

    return 0;
}