#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<pair<long long, long long>> p(n);

    for (int i = 0; i < n; i++)
    {
        cin >> p[i].first >> p[i].second;
    }

    long long sum1 = 0;
    long long sum2 = 0;
    for (int i = 0; i < n; i++)
    {
        int next = (i + 1) % n;
        sum1 += p[i].first * p[next].second;
        sum2 += p[i].second * p[next].first;
    }

    double area = abs(sum1 - sum2) / 2.0;
    cout << fixed << setprecision(1) << area;
}