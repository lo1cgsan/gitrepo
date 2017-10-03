/*
 * petle.cpp
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int i;
    
    for (i = 0; i < 101; i++)
    {
        if (i % 10 == 0)
        {
            cout << i << endl;
            ;
        }
            
        // cout << '*' << endl;
    }
    
    return 0;
}

