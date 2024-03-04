#include <iostream>
using namespace std;

int main() {
	int i = 1;
	cout << --i << endl;
	i = 1;
	cout << i-- << endl;
	i = 1;
	cout << ++i << endl;
	i = 1;
	cout << i++ << endl;
	cerr << "Test Error" << endl;
	delete i;
	cout << i << endl;
}
