#include<iostream>
#include<list>
using namespace std;

int main() {
  int N;
  list<int> l1;
  cin >> N;
  for (int i = 0;i < N;i++) {
    int usage;
    cin >> usage;
    l1.push_back(usage);
  }
}